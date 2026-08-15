pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh '''
                    export PYTHONPATH=src
                    python -m pytest -q
                '''
            }
        }
    }
}
