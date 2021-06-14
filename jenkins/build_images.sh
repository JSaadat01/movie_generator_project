#!/bin/bash

# Build and push images
docker-compose down --rmi all
docker-compose build
docker-compose up -d
sudo docker-compose push
export DATABASE_URI=mysql+pymysql://root:root@35.197.207.20:3306/project
docker exec movie-gen_frontend_service python /app/create.py
