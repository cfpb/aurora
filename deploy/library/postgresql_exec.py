#!/usr/bin/python

# This module is for executing arbitrary SQL scripts, either
# as text or in a file

DOCUMENTATION = '''
---
module: postgresql_exec
short_description: Executes arbitrary SQL scripts
description: Executes arbitrary SQL scripts.  It is recommended to
use the "when" argument to control execution, as arbitrary scripts
cannot be idempotent.

options:
  db:
    description:
      - name of database where script should be executed
    required: false
    default: none
  port:
    description:
      - Database port to connect to
    required: false
    default: 5432
  login_user:
    description:
      - User (role) used to authenticate with PostgreSQL
    required: false
    default: postgres
  login_password:
    description:
      - Password used to authenticate with PostgreSQL
    required: false
    default: null
  login_host:
    description:
      - Host running PostgreSQL.
    required: false
    default: localhost
  login_unix_socket:
    description:
      - Path to a Unix domain socket for local connections
    required: false
    default: null
  script_file:
    description:
      - A remote SQL script file to execute
    required: false
    default: null
  script:
    description:
      - A SQL script to execute
    required: false
    default: null
  autocommit:
    description:
      - Turns on autocommit, required for some operations
    required: false
    default: false
notes:
   - The default authentication assumes that you are either logging in as or
     sudo'ing to the postgres account on the host.
   - This module uses psycopg2, a Python PostgreSQL database adapter. You must
     ensure that psycopg2 is installed on the host before using this module. If
     the remote host is the PostgreSQL server (which is the default case), then
     PostgreSQL must also be installed on the remote host. For Ubuntu-based
     systems, install the postgresql, libpq-dev, and python-psycopg2 packages
     on the remote host before using this module.
requirements: [ psycopg2 ]
author: "Tim Anderegg (@tanderegg)"
'''

EXAMPLES = '''
# Execute a SQL script from file
- postgresql_exec: db=acme,script_file=myscript.sql
'''

try:
    import psycopg2
    import psycopg2.extras
except ImportError:
    postgresqldb_found = False
else:
    postgresqldb_found = True

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# ================================
# Module execution.
#

def main():
    module = AnsibleModule(
        argument_spec = dict(
            login_user         = dict(default="postgres"),
            login_password    = dict(default=""),
            login_host         = dict(default=""),
            login_unix_socket = dict(default=""),
            db                  = dict(required=True),
            port                = dict(default='5432'),
            script_file         = dict(default=None),
            script              = dict(default=None),
            autocommit          = dict(default=False)
        ),
        supports_check_mode = True
    )

    db = module.params['db']
    port = module.params['port']
    script = None

    # Ensure that either script or script_file is present,
    # but not both.  Prepare script var to hold the script
    # in either case.
    if module.params['script']:
        script = module.params['script']
        if module.params['script_file']:
            module.fail_json(msg="You cannot specify both script and script_file")
    elif not module.params['script_file']:
        module.fail_json(msg="You must specify either script or script_file")
    else:
        script = os.path.expanduser(module.params['script_file'])
        if not os.path.exists(script):
            module.fail_json(msg="Script file {0} not found".format(script))
        if not os.access(script, os.R_OK):
            module.fail_json(msg="Script file {0} not readable".format(script))

    # To use defaults values, keyword arguments must be absent, so
    # check which values are empty and don't include in the **kw
    # dictionary
    params_map = {
        "login_host":"host",
        "login_user":"user",
        "login_password":"password",
        "port":"port",
        "db":"database"
    }
    kw = dict( (params_map[k], v) for (k, v) in module.params.iteritems()
              if k in params_map and v != "" )

    # If a login_unix_socket is specified, incorporate it here.
    is_localhost = "host" not in kw or kw["host"] == "" or kw["host"] == "localhost"
    if is_localhost and module.params["login_unix_socket"] != "":
        kw["host"] = module.params["login_unix_socket"]

    try:
        db_connection = psycopg2.connect(**kw)
        if module.params["autocommit"]:
            db_connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = db_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    except Exception, e:
        module.fail_json(msg="unable to connect to database: %s" % e)

    kw = dict(script=script)

    if not (module.check_mode and module.params["autocommit"]):
        if module.params["script"]:
            cursor.execute(script)
        elif module.params["script_file"]:
            cursor.execute(open(script, "r").read())

    if not module.params["autocommit"]:
        if module.check_mode:
            db_connection.rollback()
        else:
            db_connection.commit()

    kw['changed'] = True
    kw['status'] = cursor.statusmessage

    try:
        # cursor.fetchall returns a list of DictRow classes which breaks with ansible 2.4
        kw['query_result'] = [list(row) for row in cursor.fetchall()]
    except psycopg2.ProgrammingError:
        kw['query_result'] = []

    module.exit_json(**kw)

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.database import *
main()
