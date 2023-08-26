pipeline{
    agent any

    stages{
        stage("Checkout"){
            steps{
                checkout scmGit(branches: [[name: 'Peter']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/PioWoj1999/PythonExercises.git']])
            }
        }
        stage("Build"){
            steps{
                sh "virtualenv venv && . venv/bin/activate && pip install -r requirements.txt"
            }
        }
    }
}