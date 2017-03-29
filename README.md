ansible-role-users
=========

This role manages groups, its users and sudo privileges of the group.
This way, focus is on service clusters and users grouping.

The role depends heavily on data structures that make sense for managing users,
and sudo privilages based on service groups.
The possibility of multiple groups existing in a system (system
admins, service admins, regular users) is taken into account
formulising this structure. The simplest road was taken with
no extra manipulation on ansible configuration and complex hash maps.

Group variable example:

      ---
      users_group:
          name: beautiful_people
          members:
            - junior
            - tony
          sudo: ['/bin/bash', '/sbin/service nginx *', '/usr/bin/systemctl * nginx.service']

Take note of the sudo command list. Make sure that what you put
in that array of commands are valid or you'll have a bad time.

SSH `authorized_key` file management management also part of this role,
with the prerequisite that the key file is present in the role's
`files` directory.

Requirements
------------

This is a stand-alone role.

Role Variables
--------------

The only needed role variable would be `group_name`.
This is the name of the group definition as described above.


Dependencies
------------

Supply SSH public keys in the playbook `files/pubkeys` directory and
group variables in `vars/groups`.

Example Playbook
----------------

```
- hosts: servers
  roles:
     - { role: xyzrbt/users }
     - { role: xyzrbt/users, group_name: sopranos}
     - { role: xyzrbt/users, group_name: sanchez_and_smith }
```

License
-------

GPLv2

Author Information
------------------

github.com/xyzrbt
