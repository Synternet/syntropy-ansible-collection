#!/usr/bin/python

# Copyright: (c) 2020, Syntropy Network
# MIT License
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: syntropy_template
version_added: "0.1.0"
short_description: Manages networks and connections on Syntropy Platform.
description:
    - Allows to create/delete networks between endpoints using Jinja configuration template.
    - Configuration file format can be either YAML or JSON and templating is done using Jinja language.
author:
    - Andrius Mikonis (@foxis)
requirements: ["syntropynac", "jinja2"]
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
    template_path:
        description:
            - The local path of the Syntropy configuration template.
            - This must be the full path to the file, relative to the working directory. If using roles this may look
            - like C(roles/syntropy/files/config-example.yaml).
        required: true
        type: path
    template_params:
        description: ID of the network. Has precedence before network name.
        required: false
        default: {}
        type: dict
"""  # NOQA

EXAMPLES = """
-   name: Create a Point to point network
    syntropy_template:
        template_path: "files/configuration.yaml"
        template_params:
            network_name: "custom name"
            network_state: present

-   name: Delete the network
    syntropy_template:
        template_path: "files/configuration.yaml"
        template_params:
            network_name: "custom name"
            network_state: absent
"""  # NOQA

RETURN = """
error:
    description: Error message upon unsuccessful configuration.
    type: str
    returned: always
    sample: 'Syntropy API call resulted in an error'
"""

import json
import traceback
from datetime import datetime, timedelta

from ansible.module_utils.basic import AnsibleModule, missing_required_lib

try:
    import jinja2
    import yaml
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
        "template_path": dict(type="path", required=True),
        "template_params": dict(type="dict", required=False, default={}),
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
        cfg_path = module.params["template_path"]
        with open(cfg_path, "r") as cfg_file:
            template = jinja2.Template(cfg_file.read())
            config_contents = template.render(**module.params["template_params"])
            if cfg_path.lower().endswith(".yaml") or cfg_path.lower().endswith(".yml"):
                config = list(yaml.safe_load_all(config_contents))
            elif cfg_path.lower().endswith(".json"):
                config = json.loads(config_contents)
                config = config if isinstance(config, list) else [config]

        for net in config:
            if any(i not in net for i in ("name", "topology", "state")):
                continue
            result["changed"] = result["changed"] or configure_network(
                api, net, module.check_mode, silent=True
            )
    except (ApiException, ConfigureNetworkError) as err:
        result["error"] = repr(err)
        module.fail_json(
            msg="Syntropy API call resulted in an error",
            exception=traceback.format_exc(),
        )
    except OSError as err:
        result["error"] = repr(err)
        module.fail_json(
            msg="Could not read Syntropy Configuration template",
            exception=traceback.format_exc(),
        )
    except jinja2.TemplateError as err:
        result["error"] = repr(err)
        module.fail_json(
            msg="There was an error understanding Syntropy Configuration template",
            exception=traceback.format_exc(),
        )
    except (json.JSONDecodeError, yaml.YAMLError) as err:
        result["error"] = repr(err)
        module.fail_json(
            msg="Syntropy Configuration template contains syntax errors",
            exception=traceback.format_exc(),
        )
    finally:
        del api.api_client

    module.exit_json(**result)


if __name__ == "__main__":
    main()
