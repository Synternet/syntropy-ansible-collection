# Copyright: (c) 2020, Syntropy Network
# MIT License
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
import traceback

SDK_IMP_ERR = None
try:
    from syntropy_sdk import ApiClient, ApiKeysApi, AuthApi, Configuration, PlatformApi
    from syntropy_sdk.exceptions import ApiException, SyntropyError
    from syntropy_sdk.models import AccessTokenData
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


def login_with_access_token(url, token):
    config = Configuration()
    config.host = url
    api = ApiClient(config)
    auth = AuthApi(api)

    body = AccessTokenData(access_token=token)
    try:
        response = auth.auth_access_token_login(body)
        return response.access_token
    finally:
        del auth
        del api


def get_api_client(api_url=None, api_key=None):
    config = Configuration()
    config.host = api_url if api_url else os.environ.get(EnvVars.API_URL)
    access_token = api_key if api_key else os.environ.get(EnvVars.TOKEN)
    config.api_key["Authorization"] = login_with_access_token(config.host, access_token)
    return ApiClient(config)


def api_getter_builder(T):
    def get(api_url=None, api_key=None, client=None):
        return T(get_api_client(api_url, api_key)) if client is None else T(client)

    return get


if HAS_SDK:
    get_auth_api = api_getter_builder(AuthApi)
    get_api_keys_api = api_getter_builder(ApiKeysApi)
    get_platform_api = api_getter_builder(PlatformApi)
