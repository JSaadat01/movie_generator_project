#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@manager:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@manager << EOF
    export DATABASE_URI=$(DATABASE_URI)
    docker stack deploy --compose-file docker-compose.yaml movie_generator_project
EOF