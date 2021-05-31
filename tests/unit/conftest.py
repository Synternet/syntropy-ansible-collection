from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
from unittest import mock

import pytest
from ansible_collections.syntropynet.syntropy.plugins.module_utils import syntropy


@pytest.fixture
def login_mock():
    with mock.patch(
        "ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy.login_with_access_token",
        autospec=True,
        return_value="JWT access token",
    ) as the_mock:
        yield the_mock


@pytest.fixture
def env_mock():
    with mock.patch.dict(
        os.environ,
        {
            syntropy.EnvVars.API_URL: "server",
            syntropy.EnvVars.TOKEN: "token",
        },
    ):
        yield


@pytest.fixture
def api_mock():
    with mock.patch(
        "ansible_collections.syntropynet.syntropy.plugins.module_utils.syntropy.get_api_client",
        autospec=True,
    ) as the_mock:
        yield the_mock
