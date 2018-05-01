# PhotoShop

### Commands

```bash

# MySQL Login
$ mysql -u <USERNAME> -p

# AFS Login
$ ssh -l <USERNAME> afs8.njit.edu
```

### Dependencies 

MySQLConnector for Python

```bash
# Install python mysql connector
$ pip3 mysql-connector-python
```

### MySQL Database Setup

create an "config.ini" file which includes:

[mysql]

host = HOSTNAME

database = DATABASENAME

user = USERNAME

password = PASSWORD

**Tables**

Photo

Landscape

Location

Abstract

Models

Model

Photographer

Influences

Transaction

Customer
