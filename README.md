![Tests](https://github.com/SyntropyNet/syntropy-ansible-collection/workflows/Tests/badge.svg)

# Syntropy Network Ansible collection
The Ansible Syntropy Network collection includes a variety of Ansible content to help automate the management of Syntropy networks. This collection is maintained by the Syntropy team.

More information can be found at https://docs.syntropystack.com/docs/ansible

## Tested with Ansible

This collection has been tested against Ansible versions >=2.9.

## Supported Python versions

This collection supports Python 3.6+ only.

## Included content

Name | Description
--- | ---
[syntropynet.syntropy.syntropy_facts](docs/syntropy_facts_module.rst)|Gathers facts from Syntropy Stack.
[syntropynet.syntropy.syntropy_api_key](docs/syntropy_api_key_module.rst)|Manages Syntropy Stack API Keys for endpoint agent.
[syntropynet.syntropy.syntropy_network](docs/syntropy_network_module.rst)|Manages Syntropy Stack networks and connections.
[syntropynet.syntropy.syntropy_template](docs/syntropy_template_module.rst)|Manages Syntropy Stack networks and connections using configuration template.
[syntropynet.syntropy.syntropy_oracle_agent](roles/syntropy_oracle/README.md)| Ansible role to deploy a Syntropy Agent on Oracle Linux 8.

## Installing this collection

You can install this collection using Ansible Galaxy 2.10 CLI:

```sh
ansible-galaxy collection install git@github.com:SyntropyNet/syntropy-ansible-collection.git
```

Older versions of Ansible Galaxy CLI (>=2.9,<2.10) do not support installation from GitHub repositories, so you should first download the
latest release either from GitHub or use the Galaxy repo like this:

```sh
ansible-galaxy collection install syntropynet.syntropy
```

The python module dependencies are not installed by `ansible-galaxy`. They can be manually installed using pip:

```sh
pip install -r requirements.txt
```

or:

```sh
pip install syntropynac jinja2
```

## Using this collection

This collection uses environment variables for the general configuration, such as:

```sh
export SYNTROPY_API_SERVER='{URL of the Syntropy API Stack}'
export SYNTROPY_API_TOKEN='{API Authorization token}'
```

Also, it is possible to override these environment variables by specifying `api_url` and/or `api_token` module options.
The most convenient way to do that is to specify `SYNTROPY_API_SERVER` in the environment variable and provide `api_token`.

You can either call modules by their Fully Qualified Collection Namespace (FQCN), such as `syntropynet.syntropy.syntropy_facts`, or you can call modules by their short name if you list the `syntropynet.syntropy` collection in the playbook's collections keyword:

```yaml
-   name: Gather facts
    syntropynet.syntropy.syntropy_facts:
        api_token: '{{ api_token }}'
    register: facts

- name: Dump facts output
    debug:
        facts: '{{ facts.facts }}'
```

See [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection


## Release notes


## Roadmap


## More information

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Collections Checklist](https://github.com/ansible-collections/overview/blob/master/collection_requirements.rst)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)
- [The Bullhorn (the Ansible Contributor newsletter)](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420)
- [Changes impacting Contributors](https://github.com/ansible-collections/overview/issues/45)

## Licensing

MIT