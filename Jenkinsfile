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
    stage('Ansible') {
      steps {
         sh 'ansible-playbook deploy-and-scale-playbook.yml'
        }
      }
    }
  }
}
