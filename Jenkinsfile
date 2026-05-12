pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/shrav-anikay/shrav-anikay-cicd-user-dashboard.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                pkill -f app.py || true
                nohup venv/bin/python3 app.py > output.log 2>&1 &
                '''
            }
        }

    }
}