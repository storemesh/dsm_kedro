#!/bin/bash

docker-compose run app1 python manage.py makemigrations
docker-compose run app1 python manage.py migrate
docker-compose run app1 python manage.py loaddata db1.json

docker-compose run app2 python manage.py makemigrations
docker-compose run app2 python manage.py migrate
docker-compose run app2 python manage.py loaddata db2.json

#docker-compose up
