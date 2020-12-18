# Syntropy Network collection
The Ansible Syntropy Network collection includes a variety of Ansible content to help automate the management of Syntropy networks. This collection is maintained by the Syntropy team.

## Tested with Ansible

This collection has been tested against Ansible version 2.10

## Supported Python versions

This collection supports Python 3.6+ only.

## Included content

Name | Description
--- | ---
[syntropynet.syntropy.syntropy_login](docs/noia_login_module.rst)|Logs in to NOIA Platform API and returns `api_token`.
[syntropynet.noia.noia_facts](docs/noia_facts_module.rst)|Gathers facts from NOIA Platform.
[syntropynet.noia.noia_api_key](docs/noia_api_key_module.rst)|Manages NOIA Platform API Keys.
[syntropynet.noia.noia_network](docs/noia_network_module.rst)|Manages NOIA Platform networks and connections.
[syntropynet.noia.noia_template](docs/noia_template_module.rst)|Manages NOIA Platform networks and connections using configuration template.

## Installing this collection

You can install this collection using Ansible Galaxy 2.10 CLI:

```sh
ansible-galaxy collection install git@github.com:SyntropyNet/syntropy-ansible-collection.git
```

The python module dependencies are not installed by `ansible-galaxy`. They can be manually installed using pip:

```sh
pip install -r requirements.txt
```

or:

```sh
pip install syntropy-sdk syntropynac pyyaml jinja2
```

## Using this collection

This collection uses environment variables for the general configuration, such as:

```sh
export SYNTROPY_API_SERVER='{URL of the Syntropy API Stack}'
export SYNTROPY_API_TOKEN='{API Authorization token}'
```

Also, it is possible to override these environment variables by specifying `api_url` and/or `api_token` module options.
The most convenient way to do that is to specify `SYNTROPY_API_SERVER` in the environment variable and provide `api_token` by using `noia_login` module.

You can either call modules by their Fully Qualified Collection Namespace (FQCN), such as `syntropynet.syntropy.syntropy_login`, or you can call modules by their short name if you list the `syntropynet.syntropy` collection in the playbook's collections keyword:

```yaml
-   name: Login
    syntropynet.syntropy.syntropy_login:
        username: AUserName
        password: APassword
    register: api_token

-   name: Gather facts
    syntropynet.syntropy.syntropy_facts:
        api_token: '{{ api_token.token }}'
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

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
