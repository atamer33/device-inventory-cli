pipeline {
    agent {
        docker {
            image 'python:3.13-slim'
        }
    }
    stages {
        stage('Test') {
            steps {
                sh '''
                    pip install --no-cache-dir \
                        --trusted-host pypi.org \
                        --trusted-host files.pythonhosted.org \
                        -r requirements.txt
                    export PYTHONPATH=src
                    python -m pytest -q
                '''
            }
        }
    }
}