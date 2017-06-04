# Billy bones

A small web application to account for and manage your bills. No
authentication or admin, just managing bills.

## Requirements

* Python 3
* PostgreSQL
* Ansible
* Vagrant (?)

## Deployment

In order to properly deploy the app, you need to make another variable
file: **deploy/vars/prod_settings.yml**. This file should have these
keys:

```yaml
django_secret_key:
django_host: 172.20.0.1
django_db:
  name:
  host:
  user:
  password:
django_staticroot:
```

The provided `django_host` variable is used in the Vagrantfile. If you
want to use some other host, make sure to alter both **Vagrantfile**
and **deploy/vars/prod_settings.yml**
