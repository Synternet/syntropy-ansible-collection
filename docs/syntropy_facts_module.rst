.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.syntropynet.syntropy.syntropy_facts_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

syntropynet.syntropy.syntropy_facts -- Gathers Syntropy Stack Facts
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `syntropynet.syntropy collection <https://galaxy.ansible.com/syntropynet/syntropy>`_ (version 0.1.0).

    To install it use: :code:`ansible-galaxy collection install syntropynet.syntropy`.

    To use it in a playbook, specify: :code:`syntropynet.syntropy.syntropy_facts`.

.. version_added

.. versionadded:: 0.1.0 of syntropynet.syntropy

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module gathers facts about providers, api-keys, networks, connections, endpoints, topology.


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
                    <div class="ansibleOptionAnchor" id="parameter-endpoint_name"></div>
                    <b>endpoint_name</b>
                    <a class="ansibleOptionLink" href="#parameter-endpoint_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>specifies endpoint name to filter facts by.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-endpoint_tags"></div>
                    <b>endpoint_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-endpoint_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>specifies endpoint tag to filter facts by.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-gather_subset"></div>
                    <b>gather_subset</b>
                    <a class="ansibleOptionLink" href="#parameter-gather_subset" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>providers</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>api_keys</li>
                                                                                                                                                                                                <li>endpoints</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>networks</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li><div style="color: blue"><b>connections</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>topology</li>
                                                                                    </ul>
                                                                                    <b>Default:</b><br/><div style="color: blue">["providers", "networks", "connections"]</div>
                                    </td>
                                                                <td>
                                            <div>A subset of facts to gather.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-network_name"></div>
                    <b>network_name</b>
                    <a class="ansibleOptionLink" href="#parameter-network_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>specifies network name to filter facts by.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-skip"></div>
                    <b>skip</b>
                    <a class="ansibleOptionLink" href="#parameter-skip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">0</div>
                                    </td>
                                                                <td>
                                            <div>Skip N items in the fact list.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-take"></div>
                    <b>take</b>
                    <a class="ansibleOptionLink" href="#parameter-take" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">42</div>
                                    </td>
                                                                <td>
                                            <div>Take N items in from the fact list.</div>
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

    
    -   name: Retrieve all networks and all connections
        syntropy_facts:
        register: facts_output
    -   name: Retrieve api-keys
        syntropy_facts:
            gather_subset: ['api_keys']
    -   name: Retrieve topology
        syntropy_facts:
            endpoint_tags: ['dns', 'iot']
            gather_subset: ['endpoints', 'networks', 'topology']
        register: facts_subset_output




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="2">
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-facts"></div>
                    <b>facts</b>
                    <a class="ansibleOptionLink" href="#return-facts" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Retrieved facts for various objects specified in gather_subset.</div>
                                            <div>Please refer to the API documentation for more information on the returned facts.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-facts/api_keys"></div>
                    <b>api_keys</b>
                    <a class="ansibleOptionLink" href="#return-facts/api_keys" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>                    </div>
                                    </td>
                <td>When api_keys is present in gather_subset.</td>
                <td>
                                            <div>A list of API Keys.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-facts/connections"></div>
                    <b>connections</b>
                    <a class="ansibleOptionLink" href="#return-facts/connections" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>                    </div>
                                    </td>
                <td>When connections is present in gather_subset.</td>
                <td>
                                            <div>A list of configured connections.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-facts/endpoints"></div>
                    <b>endpoints</b>
                    <a class="ansibleOptionLink" href="#return-facts/endpoints" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>                    </div>
                                    </td>
                <td>When endpoints is present in gather_subset.</td>
                <td>
                                            <div>A list of available endpoints.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-facts/networks"></div>
                    <b>networks</b>
                    <a class="ansibleOptionLink" href="#return-facts/networks" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>                    </div>
                                    </td>
                <td>When networks is present in gather_subset.</td>
                <td>
                                            <div>A list of configured networks.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-facts/providers"></div>
                    <b>providers</b>
                    <a class="ansibleOptionLink" href="#return-facts/providers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>                    </div>
                                    </td>
                <td>When providers is present in gather_subset.</td>
                <td>
                                            <div>A list of endpoint providers.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-facts/topology"></div>
                    <b>topology</b>
                    <a class="ansibleOptionLink" href="#return-facts/topology" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=dictionary</span>                    </div>
                                    </td>
                <td>When topology is present in gather_subset.</td>
                <td>
                                            <div>A list of network topology objects.</div>
                                        <br/>
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

