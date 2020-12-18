.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.syntropynet.syntropy.syntropy_template_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

syntropynet.syntropy.syntropy_template -- Manages networks and connections on Syntropy Platform.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `syntropynet.syntropy collection <https://galaxy.ansible.com/syntropynet/syntropy>`_ (version 0.1.0).

    To install it use: :code:`ansible-galaxy collection install syntropynet.syntropy`.

    To use it in a playbook, specify: :code:`syntropynet.syntropy.syntropy_template`.

.. version_added

.. versionadded:: 0.1.0 of syntropynet.syntropy

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Allows to create/delete networks between endpoints using Jinja configuration template.
- Configuration file format can be either YAML or JSON and templating is done using Jinja language.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- syntropynac
- jinja2


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
                    <div class="ansibleOptionAnchor" id="parameter-template_params"></div>
                    <b>template_params</b>
                    <a class="ansibleOptionLink" href="#parameter-template_params" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                                <td>
                                            <div>ID of the network. Has precedence before network name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-template_path"></div>
                    <b>template_path</b>
                    <a class="ansibleOptionLink" href="#parameter-template_path" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The local path of the Syntropy configuration template.</div>
                                            <div>This must be the full path to the file, relative to the working directory. If using roles this may look</div>
                                            <div>like <code>roles/syntropy/files/config-example.yaml</code>.</div>
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
        syntropy_template:
            template_path: "files/configuration.yaml"
            template_params:
                network_name: "custom name"
                network_state: present

    -   name: Delete the network
        syntropy_template:
            template_path: "files/configuration.yaml"
            template_params:
                network_name: "custom name"
                network_state: absent




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

