pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
		bat 'if exist venv rmdir /s /q venv'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\python -m pytest -v --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        stage('Evidently Report') {
            steps {
                bat 'venv\\Scripts\\python monitor.py'
                archiveArtifacts artifacts: 'evidently_report.html', fingerprint: true
            }
        }
    }
}