pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/shrav-anikay/shrav-anikay-cicd-user-dashboard.git'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment Successful'
            }
        }

    }
}