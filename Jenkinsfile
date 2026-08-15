pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
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