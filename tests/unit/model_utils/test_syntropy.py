from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
from unittest import mock

import syntropy_sdk as sdk
from ansible_collections.syntropynet.syntropy.plugins.module_utils import syntropy


def test_imports():
    assert syntropy.HAS_SDK


def test_get_api_client():
    with mock.patch(
        "ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy.login_with_access_token",
        autospec=True,
        returns="jwt token",
    ) as login_mock:
        with mock.patch.dict(
            os.environ,
            {
                syntropy.EnvVars.API_URL: "server",
                syntropy.EnvVars.TOKEN: "token",
            },
        ):
            api = syntropy.get_api_client()
            assert isinstance(api, sdk.ApiClient)
            assert api.configuration.host == "server"
            assert api.configuration.api_key["Authorization"] == "jwt token"
            del api
            login_mock.assert_called_once_with("server", "token")


def test_get_api_client__params():
    with mock.patch(
        "ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy.login_with_access_token",
        autospec=True,
        returns="jwt token",
    ) as login_mock:
        with mock.patch.dict(
            os.environ,
            {
                syntropy.EnvVars.API_URL: "server",
                syntropy.EnvVars.TOKEN: "token",
            },
        ):
            api = syntropy.get_api_client("a server", "a token")
            assert isinstance(api, sdk.ApiClient)
            assert api.configuration.host == "a server"
            assert api.configuration.api_key["Authorization"] == "jwt token"
            del api
            login_mock.assert_called_once_with("server", "a token")


def test_auth_api():
    with mock.patch(
        "ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy.get_api_client",
        autospec=True,
    ) as the_mock:
        api = syntropy.get_auth_api("a server", "a token")
        assert isinstance(api, sdk.AuthApi)
        the_mock.assert_called_once_with(api_url="a server", api_key="a token")


def test_auth_api__with_client():
    with mock.patch(
        "ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy.get_api_client",
        autospec=True,
    ) as the_mock:
        api = syntropy.get_auth_api("a server", "a token", client="a client")
        assert isinstance(api, sdk.AuthApi)
        assert the_mock.call_count == 0
        assert api.api_client == "a client"


def test_api_keys_api():
    with mock.patch(
        "ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy.get_api_client",
        autospec=True,
    ) as the_mock:
        api = syntropy.get_api_keys_api("a server", "a token")
        assert isinstance(api, sdk.ApiKeysApi)
        the_mock.assert_called_once_with(api_url="a server", api_key="a token")


def test_platform_api():
    with mock.patch(
        "ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy.get_api_client",
        autospec=True,
    ) as the_mock:
        api = syntropy.get_platform_api("a server", "a token")
        assert isinstance(api, sdk.PlatformApi)
        the_mock.assert_called_once_with(api_url="a server", api_key="a token")
