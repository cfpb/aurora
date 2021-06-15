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

python_pip_bin: [/opt/rh/python27/root/usr/bin/pip2.7]

points to pip binary installed by this role useful for setting the executable parameter
in "pip" module tasks. Used by python-libs and clouseau roles.

python_pip_ld_path: [/opt/rh/python27/root/usr/lib64]

For setting LD_LIBRARY_PATH when using SCL python. Needed by python27 where libpython path
is not compiled in to the binary.

set_python27_default_python: [False]

If True will set /etc/profile.d to make python27 the default python for users

"python" tag will run all tasks in this role


Dependencies
------------

Under RHEL this role expects the SCL to be availiable.

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
