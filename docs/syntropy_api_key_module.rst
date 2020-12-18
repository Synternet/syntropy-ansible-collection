.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.syntropynet.syntropy.syntropy_api_key_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

syntropynet.syntropy.syntropy_api_key -- Manages API keys on Syntropy Platform.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `syntropynet.syntropy collection <https://galaxy.ansible.com/syntropynet/syntropy>`_ (version 0.1.0).

    To install it use: :code:`ansible-galaxy collection install syntropynet.syntropy`.

    To use it in a playbook, specify: :code:`syntropynet.syntropy.syntropy_api_key`.

.. version_added

.. versionadded:: 0.1.0 of syntropynet.syntropy

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- API Keys are being used by the Syntropy Agent that is run on each endpoint.
- These keys are being used to communicate with the Syntropy platform.


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
                    <div class="ansibleOptionAnchor" id="parameter-api_token"></div>
                    <b>api_token</b>
                    <a class="ansibleOptionLink" href="#parameter-api_token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>API Authorization token string.</div>
                                            <div>This parameter is required if SYNTROPY_API_TOKEN environment variable is not set.</div>
                                                        </td>
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
                    <div class="ansibleOptionAnchor" id="parameter-expires"></div>
                    <b>expires</b>
                    <a class="ansibleOptionLink" href="#parameter-expires" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>ISO formatted API key expiration datetime.</div>
                                            <div>If expires is null, then current day-time + 30 days will be used as expiration date.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>API Key name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>A desired state of the API key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-suspend"></div>
                    <b>suspend</b>
                    <a class="ansibleOptionLink" href="#parameter-suspend" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Indicate whether the API Key is suspended.</div>
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
                    <div class="ansibleOptionAnchor" id="return-api_key"></div>
                    <b>api_key</b>
                    <a class="ansibleOptionLink" href="#return-api_key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Retrieved API key upon successful login.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;additionalProp1&#x27;: {}, &#x27;api_key_is_suspended&#x27;: True, &#x27;api_key_name&#x27;: &#x27;string&#x27;, &#x27;api_key_secret&#x27;: &#x27;string&#x27;, &#x27;api_key_valid_until&#x27;: &#x27;string&#x27;, &#x27;organization_id&#x27;: 0, &#x27;user_id&#x27;: 0}</div>
                                    </td>
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
                                            <div>Error message upon unsuccessful API key creation.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Syntropy API call resulted in an error</div>
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

