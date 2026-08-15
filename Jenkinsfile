pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh '''
                    pip3 install --no-cache-dir \
                        --trusted-host pypi.org \
                        --trusted-host files.pythonhosted.org \
                        -r requirements.txt
                    export PYTHONPATH=src
                    python3 -m pytest -q
                '''
            }
        }
    }
}