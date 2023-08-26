pipeline{

    stages{
        stage("Build"){
            agent {
                docker {
                    image 'python:3.11.4-alpine3.18'
                }
            }
            steps{
                sh "python --version"
            }
        }
    }
}