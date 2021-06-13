 pipeline{
    agent any
    environment {
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
    }
    stages {
        stage('Install Requirements') {
            steps {
                sh 'bash jenkins/install-requirements.sh'
            }
        }
        stage("Testing stage"){
            steps{
                // pytest
                // run for each service
                // produce cov reports
                sh "bash jenkins/test.sh"
            }
        }
        stage("Build and Push Images"){
            steps{
                // install docker-compose
                // docker-compose build
                // docker-compose push
                sh "bash jenkins/build_images.sh"
            }

        }
        
        stage("Configure Management (Ansible)"){
            steps{
                // install ansible on jenkins machine for the Jenkins user
                // ansible-playbook -i inventory.yaml playbook.yaml
                sh "cd ansible && ansible-playbook -i inventory playbook.yaml"
                sh "echo config"
            }
        }
        stage("Deploy application"){
            steps{
                // create swarm infrastructure
                // copy over docker-compose.yaml
                // ssh: docker stack deploy --compose-file docker-compose.yaml movie_generator_project
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