# postgresql-server

## Kerberos and `pg_ident.conf`

### Generating `pg_ident.conf`

The `postgresql-server` role can (optionally) generate a `pg_ident.conf` file,
which enables you to assign Kerberos principals (user identities) to
Postgres roles.

Somehwere in your `group_vars` where all the relevant postgres servers
will be able to see it, define a `pp_ident_mappings` variable like this:

```
pp_ident_mappings:
  -
    type: mymap
    match: fumentary
    pg_role: yada
  -
    type: mymap
    match: barnacle
    pg_role: blah
```

These will be used to generate a `pg_ident.conf` file, with one line per
identity:

`{{ ident.type }}    {{ ident.match }}   {{ ident.pg_role }}`

[__ Why the heck did we call the field "type" instead of "map_name"?
Ditto "match" instead of "system_username"
and "pg_role" instead of "database_username".]

### Matching system usernames against a pattern

If match starts with a slash (/), it will be interpreted as a
(Postgres-style) regular expression to match, rather than as a literal
string.  Together with a capture, this lets you do
somewhat-more-sophisticated transformations of multiple system
usernames to database usernames at once.

For example,
```
pp_ident_mappings:
  -
    type: mymap
    match: /^(.*)@mydomain\.org$
    pg_role: \1
```
will traslate `alice@mydomain.org` to `alice`, `bob@mydomain.org`
to `bob`, `carol.yuletide@mydomain.org` to `carol.yuletide`, etc.

The part in parentheses, `(.*)`, is the capture; the `\1` in the
`pg_role` line substitutes in whatever was before the `@` in the
system username (e.g. `alice`, `bob`).  Using patterns can relieve you
of having to update your `pg_ident.conf` file every time someone new
joins your organization.

A couple gotchas:
* Start the regular expression with a slash (/), but don't end it with one.
* Put a `^` after the `/`, and a `$` at the end of the expression, to
make sure you're matching the **entire** system username.
* You can only have one capture, and you refer to it with `\1`
(although you may be able to add text before it, like `db-\1` to
generate `db-alice`, `db-bob`, etc. if that's how your organization
names database users).

See https://www.postgresql.org/docs/10/auth-username-maps.html
and
https://www.postgresql.org/docs/10/auth-methods.html#GSSAPI-AUTH
in the Postgres documentation for more details.


### Generating `pg_hba.conf`

An entry in your pg_hba.conf file must have one of the following for its method:

* `gss` (for GSSAPI)
* `cert` (for Certificate Authentication) or
* `ident`
* `peer`
[__ do the non-GSSAPI ones work with Kerberos? If not, delete mentions of them.]

and specify `map=mymap` in the `auth_options` field (to follow the example above).

(SSPI is Windows-only, and thus unavailable.)

In the context of Aurora, that means at least one entry in your
pg_hba_settings must look like this:

```
pg_hba_settings:
  -
    comment: 'For hosts on our private IPs, use mymap to map to PG users'
    context: host
    db: all
    user: all
    address: '192.168.0.0/16'
    ip_mask: ''
    auth_method: gss  # or ident, cert, or peer
    auth_options: 'map=mymap'
```

Having multiple different maps is allowed; all the entries for all of
the maps will exist in the generated `pg_ident.conf` file.

See https://www.postgresql.org/docs/10/auth-pg-hba-conf.html
in the Postgres documentation for more details.

[__ do we have to do anything in pg_bha.conf to point to pg_ident.conf ?
The postgres docs seem to indicate no.]

Be careful with the items in `pg_hba_settings`, since they end up in
`pg_bha.conf`; if that's misconfigured, you could be opening your
database server up to far more hosts and users than you want to.
