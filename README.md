# Aurora - An Enterprise Data Platform

**Description**:  This repository is a collection of Ansible scripts and other
supporting code required to build a scalable, secure, and powerful data
processing platform.

  - **Technology stack**: Ansible is used for deployment.
  - **Status**:  Under active development.  Once we've reached "Alpha", further
  changes will be tracked in the [CHANGELOG](CHANGELOG.md).

## Dependencies

The Aurora data platform was designed to work on a network of RHEL 6.5 servers, and
has only been tested in that environment.  Additionally, you must have Ansible
installed to deploy, and Vagrant to run locally.

## Installation

To install locally, simply run "vagrant up" from the /deploy directory.  To deploy
to a remote environment, a custom inventory file is required along with a custom
group_vars file to go with it.  Once that has been added, simply run
"ansible-playbook site.yml -i inventories/{{ your_environment }}"

## Configuration

As mentioned above, you can configure the deployment using Ansible's inventory
and group_vars functionality.

## Usage

TBD - Likely will create more substantial documentation defining what each
server is for and how it is meant to be used.

## How to test the software

TBD

## Known issues

None at this time.

## Getting help

Open an issue on Github if you need help, have a feature request, or have
code to contribute.

## Getting involved

Refer to [CONTRIBUTING](CONTRIBUTING.md) if you'd like to help!

----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)

----

## Credits and references