from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
from unittest import mock

import pytest
import syntropy_sdk as sdk
from ansible_collections.syntropynet.syntropy.plugins.module_utils import syntropy


def test_imports():
    assert syntropy.HAS_SDK


def test_get_api_client(env_mock, login_mock):
    api = syntropy.get_api_client()
    assert isinstance(api, sdk.ApiClient)
    assert api.configuration.host == "server"
    assert api.configuration.api_key["Authorization"] == "JWT access token"
    del api
    login_mock.assert_called_once_with("server", "token")


def test_get_api_client__params(env_mock, login_mock):
    api = syntropy.get_api_client("a server", "a token")
    assert isinstance(api, sdk.ApiClient)
    assert api.configuration.host == "a server"
    assert api.configuration.api_key["Authorization"] == "JWT access token"
    del api
    login_mock.assert_called_once_with("a server", "a token")


def test_auth_api(api_mock):
    api = syntropy.get_auth_api("a server", "a token")
    assert isinstance(api, sdk.AuthApi)
    api_mock.assert_called_once_with(api_url="a server", api_key="a token")


def test_auth_api__with_client(api_mock):
    api = syntropy.get_auth_api("a server", "a token", client="a client")
    assert isinstance(api, sdk.AuthApi)
    assert api_mock.call_count == 0
    assert api.api_client == "a client"


def test_api_keys_api(api_mock):
    api = syntropy.get_api_keys_api("a server", "a token")
    assert isinstance(api, sdk.ApiKeysApi)
    api_mock.assert_called_once_with(api_url="a server", api_key="a token")


def test_platform_api(api_mock):
    api = syntropy.get_platform_api("a server", "a token")
    assert isinstance(api, sdk.PlatformApi)
    api_mock.assert_called_once_with(api_url="a server", api_key="a token")
