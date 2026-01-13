pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Клонування репозиторію з гілки main
                git branch: 'main', url: 'https://github.com/dimkasimka228/PakhalovychLAB2025-_1'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Запуск одного файлу tests.py
                sh '''
                python3 -m unittest app_tests.py
                '''
            }
        }
    }
}