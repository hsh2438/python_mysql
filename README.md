# python_pymysql
pymysql library example

## setting mariadb server with docker

    docker run -it -p 3306:3306 --name mariadb -e MYSQL_ROOT_PASSWORD=admin123 -d mariadb:latest

## get inside container
   
   docker exec -it mariadb bash

## db client tool
> HeidiSQL
