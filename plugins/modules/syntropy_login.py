#!/usr/bin/python

# Copyright: (c) 2020, Syntropy Network
# MIT License
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: syntropy_login
short_description: Logins to Syntropy Platform
version_added: "0.1.0"
description:
    - Logins to Syntropy Platform and returns API authorization token that can be used with other modules.
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
    username:
        description: Username registered on Syntropy Platform.
        required: true
        type: str
    password:
        description: Password for the user.
        required: true
        type: str
"""  # NOQA

EXAMPLES = """
-   name: Login
    syntropylogin:
        username: AUserName
        password: APassword
    register: api_token

-   name: Gather facts
    syntropyfacts:
        api_token: '{{ api_token.token }}'
    register: facts
"""  # NOQA

RETURN = """
error:
    description: Error message upon unsuccessful login.
    type: str
    returned: always
    sample: 'Authorization failure'
token:
    description: Retrieved API token upon successful login.
    type: str
    returned: always
    sample: '{API token string}'
"""

import traceback

from ansible.module_utils.basic import AnsibleModule, missing_required_lib

try:
    from ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy import (
        HAS_SDK,
        SDK_IMP_ERR,
        ApiException,
        get_auth_api,
    )
except ImportError:
    pass


def main():
    module_args = dict(
        api_url=dict(type="str", required=False, default=None),
        username=dict(type="str", required=True),
        password=dict(type="str", required=True, no_log=True),
    )

    result = dict(changed=False, error="", token="")

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    if not HAS_SDK:
        result["error"] = SDK_IMP_ERR
        module.fail_json(
            msg=missing_required_lib("syntropy-sdk"), exception=SDK_IMP_ERR
        )

    if module.check_mode:
        module.exit_json(**result)

    auth = get_auth_api(api_url=module.params["api_url"])

    try:
        payload = {
            "user_email": module.params["username"],
            "user_password": module.params["password"],
        }
        result["token"] = auth.auth_external_login(body=payload)["refresh_token"]
    except ApiException:
        result["error"] = "Failure"
        module.fail_json(
            msg="Login was not successful", exception=traceback.format_exc()
        )
    finally:
        del auth.api_client

    result["changed"] = False

    module.exit_json(**result)


if __name__ == "__main__":
    main()
