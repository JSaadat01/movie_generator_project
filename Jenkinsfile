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
                sh "bash jenkins/build_images.sh"
                sh "echo build and push"
            }
        }
        stage("Configure Swarm"){
            steps{
                sh "/home/jenkins/.local/bin/ansible-playbook -i inventory playbook.yaml"
                sh "echo config"
            }
        }
        stage("Deploy application"){
            steps{
                sh "bash jenkins/deploy_stack.sh"
                sh "echo push"
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