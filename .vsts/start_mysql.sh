#!/usr/bin/env bash

export MYSQL_ROOT_PASSWORD=super-secret
sudo -u mysql --preserve-env -b /usr/local/bin/docker-entrypoint.sh mysqld
sleep 20
mysql --host=127.0.0.1 --port=3306 -u root --password=super-secret --execute="SELECT User, Host FROM mysql.user"
