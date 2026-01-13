pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/dimkasimka228/PakhalovychLAB2025-_1.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest --junitxml=test-reports/results.xml'
            }
        }

        stage('Publish results') {
            steps {
                junit 'test-reports/results.xml'
            }
        }
    }
}
