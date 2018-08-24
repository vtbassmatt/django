#!/usr/bin/env bash

MYSQL_ROOT_PASSWORD=super-secret
sudo -u mysql /usr/local/bin/docker-entrypoint.sh mysqld
sleep 10
mysql --host=127.0.0.1 --port=3306 -u root --password=secret --execute="SELECT User, Host FROM mysql.user"
