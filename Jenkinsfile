pipeline {
  agent any
  stages {
    stage('Docker Build') {
      steps {
         sh 'docker build -t conroy3644/capstone1-webapp:latest .'
      }
    }
    stage('Docker Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'docker push conroy3644/capstone1-webapp:latest'
        }
      }
    }
    stage('Testing Flask') {
      steps {
        sh 'pytest /home/osboxes/Per-Scholas-Capstone-Project-1/tests/testhttp.py | grep FAILED > testoutput.txt'
      }
    }
    stage('Deploy Kubernetes') {
      steps {
        sh 'kubectl apply -f kubernetes.yml'
      }
    }
  }
}
