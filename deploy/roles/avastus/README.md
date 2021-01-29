Role Name
=========

Installs and configures Avastus. An internal tool that provides name resolution for the applications deployed on the Mesos/Marathon cluster by means of updating Apache configuration to match 

Requirements
------------

This module is meant to be installed on a proxy server running apache. It expects python3 via RHEL SCL and for a
mesos/marathon cluster to be in the inventory under the mesos_master group.

Role Variables
--------------

    - avastus_base_path: [/opt/avastus]
      The base directory to checkout the avastus app

    - avastus_conf_file_path: [/opt/avastus-conf]
      Where to place example avastus configuration. Later copied to systemd folder.

    - avastus_venv_path: [/opt/avastus.env3]
      Path to install the python virtualenv for avastus

    - avastus_repo: 
      Where to find the Avastus app

    - avastus_apache_conf: [/srv/www/enclave_proxy/apps]
      Where to write out apache configuration files. The directory will contain files named after the marathon
      id of all apps with a passing health check and contain the ip/port at which the app is listening. The
      intention if for a host directive for each app will proxy to a balancer over the contents of the file.

    - avastus_marathon_hosts: ["{{ groups['mesos_master'] | map('extract',hostvars,'aurora_hostname') | list}}"]
      Coma separated list of Marathon host/ports culled by default
      May be hardcoded as eg:
      "http://10.0.1.31:8080,http://10.0.1.32:8080,http://10.0.1.33:8080"

    - avastus_logstash_host:
      Logging will be sent to this host if set

    - avastus_logstash_port:
      Logging will be sent to this port if set

Dependencies
------------



Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

CC0

Author Information
------------------

CFPB
