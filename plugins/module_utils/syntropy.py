# Copyright: (c) 2020, Syntropy Network
# MIT License
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
import traceback

SDK_IMP_ERR = None
try:
    from syntropy_sdk import ApiClient, AuthApi, Configuration, PlatformApi
    from syntropy_sdk.exceptions import ApiException, SyntropyError
    from syntropy_sdk.utils import MAX_QUERY_FIELD_SIZE, BatchedRequest
    from syntropynac.configure import configure_network
    from syntropynac.exceptions import ConfigureNetworkError
    from syntropynac.fields import ConfigFields

    HAS_SDK = True
except ImportError:
    HAS_SDK = False
    SDK_IMP_ERR = traceback.format_exc()


class EnvVars:
    API_URL = "SYNTROPY_API_SERVER"
    TOKEN = "SYNTROPY_API_TOKEN"


def get_api_client(api_url=None, api_key=None):
    config = Configuration()
    config.host = api_url if api_url else os.environ.get(EnvVars.API_URL)
    config.api_key["Authorization"] = (
        api_key if api_key else os.environ.get(EnvVars.TOKEN)
    )
    return ApiClient(config)


def get_auth_api(api_url=None, api_key=None):
    return AuthApi(get_api_client(api_url, api_key))


def get_platform_api(api_url=None, api_key=None):
    return PlatformApi(get_api_client(api_url, api_key))
