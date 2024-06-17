pipeline {
    agent any

    environment {
        ALPACA_API_KEY = credentials('alpaca_api_key') // Use Jenkins credentials for API keys
        ALPACA_SECRET_KEY = credentials('alpaca_secret_key')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/alpaca-trading-bot.git'
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
