#!/bin/bash
scp -i ~/.ssh
ssh -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@manager
docker stack deploy --compose-file docker-compose.yaml movie_generator_project
