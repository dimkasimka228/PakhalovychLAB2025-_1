pipeline {
    agent any

    environment {
        DOCKERHUB = credentials('dockerhub-creds')
    }

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

        stage('Build Docker image') {
            steps {
                // Збираємо образ під Docker Hub акаунт pkhalovych
                sh 'docker build -t pakhalovych/python-lab4:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // Логін у Docker Hub через креденшали
                sh 'echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin'
                // Пушимо образ у pkhalovych/python-lab4
                sh 'docker push pakhalovych/python-lab4:latest'
            }
        }
    }
}
