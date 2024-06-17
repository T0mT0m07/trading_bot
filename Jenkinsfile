pipeline {
    agent any

    environment {
        ALPACA_API_KEY = credentials('ALPACA_API_KEY') // Reference the API Key
        ALPACA_SECRET_KEY = credentials('ALPACA_SECRET_KEY') // Reference the Secret Key
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/T0mT0m07/trading_bot.git'
            }
        }

        stage('Setup') {
            steps {
                sh 'python3 -m venv venv' // Create a virtual environment
                sh '. venv/bin/activate && pip install -r requirements.txt' // Install dependencies
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && python -m unittest discover tests' // Run tests
            }
        }

        stage('Deploy') {
            steps {
                sh '. venv/bin/activate && python main.py' // Run the main script
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/logs/*.log', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
