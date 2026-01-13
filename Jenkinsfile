pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Клонування репозиторію з гілки main
                git branch: 'main',
                    credentialsId: 'github-repo',
                    url: 'https://github.com/dimkasimka228/PakhalovychLAB2025-_1.git'
            }
        }

        stage('Run Unit Tests') {
            agent {
                docker {
                    image 'python:3.11-slim'
                }
            }
            steps {
                // Встановлення залежностей і запуск тестів у контейнері з Python
                sh '''
                    pip install -r requirements.txt
                    python -m unittest app_tests.py
                '''
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
    }
}
