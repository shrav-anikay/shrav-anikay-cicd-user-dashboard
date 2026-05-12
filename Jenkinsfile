pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/shrav-anikay/shrav-anikay-cicd-user-dashboard.git'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                pkill -f app.py || true
                nohup python3 app.py > output.log 2>&1 &
                '''
            }
        }

    }
}