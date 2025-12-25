pipeline {                          // START: Define a Pipeline
    agent any                       // RUN: On any available machine
    stages {                        // GROUP: All your stages here
        stage('Checkout') {         // STAGE 1: Download your Git repo
            steps {
                checkout scm         // GIT: Pull code from GitHub
            }
        }
        stage('Stage 1: YAML Parsing (pytest)') {  // STAGE 2: Your pytest
            steps {
                sh '''               // SHELL: Run bash commands
                python3.9 -m venv .venv      # CREATE: Python virtualenv
                source .venv/bin/activate     # ACTIVATE: Virtualenv
                pip install pytest pyyaml     # INSTALL: Your test deps
                pytest tests/ -v --tb=short   # RUN: Your 3 pytest tests!
                '''                          // END shell
            }
        }
    }                                // END: All stages
    post {                           // CLEANUP: After pipeline
        always {
            cleanWs()                // DELETE: Workspace files
        }
    }
}                                    // END: Pipeline
