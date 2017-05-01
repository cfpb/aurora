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

### Running Docker on a Macbook

1. brew cask install docker-toolbox
1. docker-machine start default
1. docker-machine create --driver "virtualbox" default
1. eval "$(docker-machine env default)"
1. docker ps (to validate it works)

If docker starts running out of disk space, connect to the boot2docker VM (or Mac terminal) and run this:

docker ps -a -q | xargs -n 1 -I {} docker rm {}

Command to make sure the exited containers are deleted:

docker rm -v $(docker ps -a -q -f status=exited)

### Setting up Test Environment

When developing the Travis CI file, it can be helpful to test in travis's environment as described
here: https://docs.travis-ci.com/user/common-build-problems/#Build-times-out-because-no-output-was-received
* Note: you'll need to install the travis image with --privileged
  * docker run --privileged -it quay.io/travisci/travis-ruby /bin/bash

To do this, follow the steps above up to actually running your commands.  Before doing so, Docker must
be installed in the Travis CI image, like so:

1. sudo apt-get install apt-transport-https ca-certificates
1. sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
1. echo "deb https://apt.dockerproject.org/repo ubuntu-precise main" | sudo tee /etc/apt/sources.list.d/docker.list
1. sudo apt-get update
1. apt-cache policy docker-engine
1. sudo apt-get install docker-engine (May neeed --force-yes)
1. sudo ln -s /bin/true /sbin/initctl
1. sudo service docker start ->>
1. docker daemon -H unix:///var/run/docker.sock&>/var/log/docker.log &
1. git clone https://github.com/[githubfork]/aurora /aurora
1. cd /aurora
1. git checkout travis
1. Run commands in travis.yml file


TBD

## Known issues

- Travis-CI hangs when jobs complete - [resolution](https://www.jeffgeerling.com/blog/2017/fix-ansible-hanging-when-used-docker-and-tty)

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