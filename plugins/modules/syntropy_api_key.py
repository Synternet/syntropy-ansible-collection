#!/usr/bin/python

# Copyright: (c) 2020, Syntropy Network
# MIT License
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: syntropy_api_key
version_added: "0.1.0"
short_description: Manages API keys on Syntropy Platform.
description:
    - API Keys are being used by the Syntropy Agent that is run on each endpoint.
    - These keys are being used to communicate with the Syntropy platform.
author:
    - Andrius Mikonis (@foxis)
requirements: ["syntropy-sdk"]
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
    description: API Key name.
    required: true
    type: str
  suspend:
    description: Indicate whether the API Key is suspended.
    required: false
    default: false
    type: bool
  expires:
    description:
        - ISO formatted API key expiration datetime.
        - If expires is null, then current day-time + 30 days will be used as expiration date.
    required: false
    default: null
    type: str
  state:
    description: A desired state of the API key.
    required: false
    choices: ['present', 'absent']
    default: 'present'
    type: str
"""

EXAMPLES = """
-   name: Create a new API key
    syntropy_api_key:
        name: my-api-key
        suspend: no
        state: present
    register: api_key

-   name: Delete an API key
    syntropy_api_key:
        name: my-api-key
        state: absent
"""

RETURN = """
error:
    description: Error message upon unsuccessful API key creation.
    type: str
    returned: always
    sample: 'Syntropy API call resulted in an error'
api_key:
    description: Retrieved API key upon successful login.
    type: dict
    returned: always
    sample:  {
            "organization_id": 0,
            "user_id": 0,
            "api_key_secret": "string",
            "api_key_name": "string",
            "api_key_id": 0,
            "api_key_is_suspended": true,
            "api_key_valid_until": "string"
        }
"""

import traceback
from datetime import datetime, timedelta

from ansible.module_utils.basic import AnsibleModule, missing_required_lib

try:
    from ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy import (
        HAS_SDK,
        SDK_IMP_ERR,
        ApiException,
        get_api_keys_api,
    )
except ImportError:
    pass


def main():
    argument_spec = {
        "api_url": dict(type="str", default=None),
        "api_token": dict(type="str", default=None, no_log=True),
        "name": dict(type="str", required=True),
        "state": dict(
            default="present",
            required=False,
            choices=["present", "absent"],
        ),
        "suspend": dict(type="bool", required=False, default=False),
        "expires": dict(
            type="str",
            required=False,
            default=None,
        ),
    }

    result = dict(
        changed=False,
        error="",
        key={},
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    if not HAS_SDK:
        result["error"] = SDK_IMP_ERR
        module.fail_json(
            msg=missing_required_lib("syntropy-sdk"), exception=SDK_IMP_ERR
        )

    try:
        if module.params["expires"] is not None:
            expires = datetime.fromisoformat(module.params["expires"])
        else:
            expires = (datetime.now() + timedelta(days=30)).isoformat()
    except ValueError:
        module.fail_json(msg="Expires must be an ISO formatted date time")

    api = get_api_keys_api(
        api_url=module.params["api_url"], api_key=module.params["api_token"]
    )

    try:
        keys = api.get_api_key(filter=f"api_key_name:'{module.params['name']}'").data

        if module.params["state"] == "present":
            if keys:
                result["key"] = keys[0].to_dict()
                module.exit_json(**result)
            if not module.check_mode:
                body = {
                    "api_key_name": module.params["name"],
                    "api_key_is_suspended": module.params["suspend"],
                    "api_key_valid_until": expires,
                }
                result["key"] = api.create_api_key(body=body).data.to_dict()
                result["changed"] = True
        elif module.params["state"] == "absent":
            if not keys:
                module.exit_json(**result)
            if not module.check_mode and keys:
                api.delete_api_key(keys[0].api_key_id)
                result["changed"] = True
    except ApiException:
        result["error"] = "Failure"
        module.fail_json(
            msg="Syntropy API call resulted in an error",
            exception=traceback.format_exc(),
        )
    finally:
        del api.api_client

    module.exit_json(**result)


if __name__ == "__main__":
    main()
