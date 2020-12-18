.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.syntropynet.syntropy.syntropy_login_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

syntropynet.syntropy.syntropy_login -- Logins to Syntropy Platform
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `syntropynet.syntropy collection <https://galaxy.ansible.com/syntropynet/syntropy>`_ (version 0.1.0).

    To install it use: :code:`ansible-galaxy collection install syntropynet.syntropy`.

    To use it in a playbook, specify: :code:`syntropynet.syntropy.syntropy_login`.

.. version_added

.. versionadded:: 0.1.0 of syntropynet.syntropy

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Logins to Syntropy Platform and returns API authorization token that can be used with other modules.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- syntropy-sdk


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-api_url"></div>
                    <b>api_url</b>
                    <a class="ansibleOptionLink" href="#parameter-api_url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>URL Of the Platform API.</div>
                                            <div>This parameter is required if SYNTROPY_API_SERVER environment variable is not set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Password for the user.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Username registered on Syntropy Platform.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    -   name: Login
        syntropylogin:
            username: AUserName
            password: APassword
        register: api_token

    -   name: Gather facts
        syntropyfacts:
            api_token: '{{ api_token.token }}'
        register: facts




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-error"></div>
                    <b>error</b>
                    <a class="ansibleOptionLink" href="#return-error" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Error message upon unsuccessful login.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Authorization failure</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-token"></div>
                    <b>token</b>
                    <a class="ansibleOptionLink" href="#return-token" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Retrieved API token upon successful login.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{API token string}</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Andrius Mikonis (@foxis)



.. Parsing errors

