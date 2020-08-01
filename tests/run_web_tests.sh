#! /bin/bash

docker-compose up --detach && sleep 4 && python test_webapp.py
docker-compose down
