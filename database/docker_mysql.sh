#!/bin/bash

docker container run --rm --name mariadb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mariadb:10.4