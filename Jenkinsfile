pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'YOUR_DOCKERHUB_USERNAME/my-web-app:latest'
        CREDENTIALS_ID = 'docker-hub-credentials'
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Tejas092828/CCD_CCA2.git'
            }
        }
        stage('Build and Test') {
            steps {
                sh 'echo "Running build and syntax checks..."'
                // Add your test commands here, e.g., pytest or python -m py_compile app.py
                sh 'python3 -m py_compile app.py'
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    app = docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }
        stage('Push Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', "${env.CREDENTIALS_ID}") {
                        app.push("latest")
                    }
                }
            }
        }
        stage('Minikube Deployment') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
                sh 'kubectl rollout restart deployment/web-app-deployment'
            }
        }
    }
}