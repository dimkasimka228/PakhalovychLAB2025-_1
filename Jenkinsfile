pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-repo',
                    url: 'https://github.com/dimkasimka228/PakhalovychLAB2025-_1.git'
            }
        }

        stage('Run Unit Tests') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    args '-u root'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m unittest app_tests.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
    }
}
