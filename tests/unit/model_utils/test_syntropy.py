from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
from unittest import mock

import syntropy_sdk as sdk
from ansible_collections.syntropynet.syntropy.plugins.module_utils import syntropy


def test_imports():
    assert syntropy.HAS_SDK


def test_get_api_client():
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
        assert api.configuration.api_key["Authorization"] == "token"
        del api


def test_get_api_client__params():
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
        assert api.configuration.api_key["Authorization"] == "a token"
        del api


def test_auth_api():
    with mock.patch(
        "ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy.get_api_client",
        autospec=True,
    ) as the_mock:
        api = syntropy.get_auth_api("a server", "a token")
        assert isinstance(api, sdk.AuthApi)
        the_mock.assert_called_once_with(api_url="a server", api_key="a token")


def test_platform_api():
    with mock.patch(
        "ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy.get_api_client",
        autospec=True,
    ) as the_mock:
        api = syntropy.get_platform_api("a server", "a token")
        assert isinstance(api, sdk.PlatformApi)
        the_mock.assert_called_once_with(api_url="a server", api_key="a token")
