Role Name
=========

Install Python2.7 environment from Centos / Redhat Software Collections

Requirements
------------

libselinux-python may be required.

Role Variables
--------------

ansible_distribution

If "CentOS" will install the CentOS SCL. SCL assumed to already be installed for RHEL

set_python27_default_python: [False]

If True will set /etc/profile.d to make python27 the default python for users

python3 tag will run all tasks in this role


Dependencies
------------

python-libs role python_pip_binary should point to pip binary installed by this role and depends on python being installed

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - python27-scl

    - hosts: servers
      roles:
         - { role: python27-scl, set_python27_default_python: True }


Author Information
------------------

CFPB
