pipeline {
  agent any
  stages {
    stage('Docker Build') {
      steps {
         sh 'docker build -t conroy3644/sba2022.kube:latest .'
      }
    }
    stage('Docker Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'docker push conroy3644/sba2022.kube:latest'
         }
      }
    }
  }
}
