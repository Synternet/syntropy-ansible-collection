.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.syntropynet.syntropy.syntropy_network_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

syntropynet.syntropy.syntropy_network -- Manages networks and connections on Syntropy Platform.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `syntropynet.syntropy collection <https://galaxy.ansible.com/syntropynet/syntropy>`_ (version 0.1.0).

    To install it use: :code:`ansible-galaxy collection install syntropynet.syntropy`.

    To use it in a playbook, specify: :code:`syntropynet.syntropy.syntropy_network`.

.. version_added

.. versionadded:: 0.1.0 of syntropynet.syntropy

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Allows to create/delete networks between endpoints using configuration embedded in the playbook.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- syntropynac


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
                    <div class="ansibleOptionAnchor" id="parameter-connections"></div>
                    <b>connections</b>
                    <a class="ansibleOptionLink" href="#parameter-connections" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A dictionary specifying network connections. A key represents the name of the endpoint or tag name of a set of endpoints.</div>
                                            <div>Each endpoint has a mandatory option &#x27;type&#x27; which is one of &#x27;endpoint&#x27; or &#x27;tag&#x27; and a &#x27;state&#x27; option that is one of &#x27;present&#x27; or &#x27;absent&#x27;.</div>
                                            <div>For p2p or p2m networks a connections supports &#x27;connect_to&#x27; option which is a dictionary containing endpoint names/tags as keys.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>ID of the network. Has precedence before network name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ignore_configured_topology"></div>
                    <b>ignore_configured_topology</b>
                    <a class="ansibleOptionLink" href="#parameter-ignore_configured_topology" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Instructs the platform to ignore currently configured network topology and</div>
                                            <div>create/update connections between endpoints specified in connections according to the</div>
                                            <div>topology specified in this config.</div>
                                            <div>This parameter is mainly used to configure complex topologies consisting of multiple topologies.</div>
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
                                            <div>Name of the network.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-topology"></div>
                    <b>topology</b>
                    <a class="ansibleOptionLink" href="#parameter-topology" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>p2p</li>
                                                                                                                                                                                                <li>p2m</li>
                                                                                                                                                                                                <li>mesh</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Network topology.</div>
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

    
    -   name: Create a Point to point network
        syntropynetwork:
            name: p2p-network
            topology: p2p
            use_sdn: no
            state: present
            connections:
                endpoint-1:
                    state: present
                    connect_to:
                        endpoint-2
                endpoint-3:
                    state: present
                    connect_to:
                        endpoint-4

    -   name: Create a Point to multi-point network using tags
        syntropynetwork:
            name: p2m-network
            topology: p2m
            use_sdn: no
            state: present
            connections:
                endpoint-1:
                    state: present
                    type: endpoint
                    connect_to:
                        iot-devices:
                            type: tag
                            state: present

    -   name: Create a mesh network using tags
        syntropynetwork:
            name: mesh-network
            topology: mesh
            use_sdn: yes
            state: present
            connections:
                dns-servers:
                    state: present
                    type: tag




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
                                            <div>Error message upon unsuccessful configuration.</div>
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

