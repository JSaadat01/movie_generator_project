pipeline{
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
        TEST_DATABASE_URI = credentials("TEST_DATABASE_URI") 
    }
    stages {
        stage("Testing stage"){
            steps{
                sh "bash jenkins/test.sh"
            }
        }
        stage("Build and Push Images"){
            steps{
                // install docker and docker compose
                // docker-compose build
                // install docker and docker compose
                // docker-compose push
                sh "bash jenkins/build_images.sh"
                sh "echo build and push"
            }
        }
        stage("Configure Swarm"){
            steps{
                // install ansible on jenkins machine for the Jenkins user
                // ansible-playbook -i inventory.yaml playbook.yaml
                sh "/home/jenkins/.local/bin/ansible-playbook -i inventory playbook.yaml"
                sh "echo config"
            }
        }
        stage("Deploy application"){
            steps{
                // create swarm infrastructure
                // copy over docker-compose.yaml
                // ssh: docker stack deploy --compose-file docker-compose.yaml movie_generator_project
                sh "bash jenkins/deploy_stack.sh"
                sh "echo deploy"
            }
        }
    }
    post{
        always{
            junit "**/junit.xml"
            cobertura coberturaReportFile: '**/coverage.xml', failNoReports: false, failUnstable: false, onlyStable: false
        }
    }
}