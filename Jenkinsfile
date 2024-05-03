pipeline {
    agent { label "agentfarm"}
    environment {
        PORT = '8082'
    }
    stages {
        stage('Build') {
            steps {
                sh './build.sh'  // Execute the build script to install dependencies
            }
        }
        stage('Test') {
            steps {
                sh './start.sh'  // Activate virtual environment, install dependencies, and run tests
            }
        }
        stage('Test stage') {
            steps {
                sh 'pytest hello_world_test.py'
  }
}
        stage('env'){
           steps{
            sh label: 'Run fancy bash script',
             script: '''
               #!/venv/bin/activate  bash

               nohup python3 main.py > ~/flasklogs.log 2>&1 &
             '''.stripIndent().stripLeading()
   }
}
        stage(Deploy){
            steps {
               sh 'nohup python3 main.py > ~/flasklogs.log 2>&1 &'
   }
}
        }
    }
