#!groovy

def kubectlTest() {
    // Test that kubectl can correctly communication with the Kubernetes API
    echo "running kubectl test"
    sh "kubectl get nodes"

}

def helmTest() {
    // lint helm chart
    sh "/usr/local/bin/helm version"
}

def helmLint() {
  sh "/usr/local/bin/helm lint tutorial"
}

def helmInstall() {
  sh "/usr/local/bin/helm upgrade --install tutorial tutorial"
}

def getServices() {
  sh "kubectl get services"
}


node {

        stage ('helm test') {
          kubectlTest();
          helmTest();
          echo "Done testing"
        }

        stage ('git pull') {
          echo "Pull project"
          git url: 'https://github.com/ogross74/helm-tutorial.git'
        }

        stage ('helm lint') {
          echo "Lint..."

          helmLint();
        }


        stage ('helm install') {
          echo "Install..."

          helmInstall();

          echo "Installed"

          getServices();
        }
}
