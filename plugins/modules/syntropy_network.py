#!/usr/bin/python

# Copyright: (c) 2020, Syntropy Network
# MIT License
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: syntropy_network
version_added: "0.1.0"
short_description: Manages networks and connections on Syntropy Platform.
description: 
    - Allows to create/delete networks between endpoints using configuration embedded in the playbook.
author:
    - Andrius Mikonis (@foxis)
requirements: ["syntropynac"]
options:
    api_url:
        description:
            - URL Of the Platform API.
            - This parameter is required if SYNTROPY_API_SERVER environment variable is not set.
        required: false
        default: null
        type: str
    api_token:
        description:
            - API Authorization token string.
            - This parameter is required if SYNTROPY_API_TOKEN environment variable is not set.
        required: false
        default: null
        type: str
    name:
        description: Name of the network.
        required: true
        type: str
    id:
        description: ID of the network. Has precedence before network name.
        required: false
        default: null
        type: int
    topology:
        description: Network topology.
        required: true
        choices: ['p2p', 'p2m', 'mesh']
        type: str
    ignore_configured_topology:
        description: 
            - Instructs the platform to ignore currently configured network topology and
            - create/update connections between endpoints specified in connections according to the
            - topology specified in this config.
            - This parameter is mainly used to configure complex topologies consisting of multiple topologies.
        required: false
        default: false
        type: bool
    connections:
        description:
            - A dictionary specifying network connections. A key represents the name of the endpoint or tag name of a set of endpoints.
            - Each endpoint has a mandatory option 'type' which is one of 'endpoint' or 'tag' and a 'state' option that is one of 'present' or 'absent'.
            - For p2p or p2m networks a connections supports 'connect_to' option which is a dictionary containing endpoint names/tags as keys.
        required: false
        default: null
        type: dict
    state:
        description: A desired state of the API key.
        required: false
        choices: ['present', 'absent']
        default: 'present'
        type: str
"""  # NOQA

EXAMPLES = """
-   name: Create a Point to point network
    syntropynetwork:
        name: p2p-network
        topology: p2p
        use_sdn: no
        state: present
        connections:
            endpoint-1:
                state: present
                connect_to:
                    endpoint-2
            endpoint-3:
                state: present
                connect_to:
                    endpoint-4

-   name: Create a Point to multi-point network using tags
    syntropynetwork:
        name: p2m-network
        topology: p2m
        use_sdn: no
        state: present
        connections:
            endpoint-1:
                state: present
                type: endpoint
                connect_to:
                    iot-devices:
                        type: tag
                        state: present

-   name: Create a mesh network using tags
    syntropynetwork:
        name: mesh-network
        topology: mesh
        use_sdn: yes
        state: present
        connections:
            dns-servers:
                state: present
                type: tag
"""  # NOQA

RETURN = """
error:
    description: Error message upon unsuccessful configuration.
    type: str
    returned: always
    sample: 'Syntropy API call resulted in an error'
"""

import traceback
from datetime import datetime, timedelta

from ansible.module_utils.basic import AnsibleModule, missing_required_lib

try:
    from ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy import (
        HAS_SDK,
        SDK_IMP_ERR,
        ApiException,
        ConfigFields,
        ConfigureNetworkError,
        configure_network,
        get_platform_api,
    )
except ImportError:
    pass


def main():
    argument_spec = {
        "api_url": dict(type="str", default=None),
        "api_token": dict(type="str", default=None, no_log=True),
        "name": dict(type="str", required=True),
        "id": dict(type="int", required=False, default=None),
        "state": dict(
            default="present",
            required=False,
            choices=["present", "absent"],
        ),
        "topology": dict(type="str", required=True, choices=["p2p", "p2m", "mesh"]),
        "ignore_configured_topology": dict(type="bool", default=False),
        "connections": dict(type="dict", required=False),
    }

    result = dict(
        changed=False,
        error="",
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    if not HAS_SDK:
        result["error"] = SDK_IMP_ERR
        module.fail_json(msg=missing_required_lib("syntropynac"), exception=SDK_IMP_ERR)

    api = get_platform_api(
        api_url=module.params["api_url"], api_key=module.params["api_token"]
    )

    try:
        params = {
            ConfigFields.NAME: module.params["name"],
            ConfigFields.ID: module.params["id"],
            ConfigFields.STATE: module.params["state"],
            ConfigFields.TOPOLOGY: module.params["topology"],
            ConfigFields.IGNORE_NETWORK_TOPOLOGY: module.params[
                "ignore_configured_topology"
            ],
            ConfigFields.CONNECTIONS: module.params["connections"],
        }
        result["changed"] = configure_network(
            api, params, module.check_mode, silent=True
        )
    except (ApiException, ConfigureNetworkError) as err:
        result["error"] = repr(err)
        module.fail_json(
            msg="Syntropy API call resulted in an error",
            exception=traceback.format_exc(),
        )
    finally:
        del api.api_client

    module.exit_json(**result)


if __name__ == "__main__":
    main()
