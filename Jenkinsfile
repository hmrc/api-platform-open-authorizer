#!/usr/bin/env groovy
pipeline {
  agent any

  stages {
    stage('Prepare') {
      steps {
        step([$class: 'WsCleanup'])
        checkout(scm)
        sh("""virtualenv -p python3 venv
        . venv/bin/activate
        pip install -r requirements-dev.txt
        nosetests -v --with-cover --cover-erase --cover-package=lambda_function --cover-package=api_request_details
        flake8 --ignore=E501 *.py
        deactivate""")
      }
    }
    stage('Build artefact') {
      steps {
        sh('docker run -t -v $(pwd):/data amazonlinux:2018.03.0.20180424 /bin/bash -c "cd /data; ./package.sh"')
      }
    }
    stage('Generate sha256') {
      steps {
        sh('openssl dgst -sha256 -binary api-platform-open-authorizer.zip | openssl enc -base64 > api-platform-open-authorizer.zip.base64sha256')
      }
    }
    stage('Upload to s3') {
      steps {
        script {
          git_id = sh(returnStdout: true, script: 'git describe --always').trim()
          target_file = 'api-platform-open-authorizer.zip'
        }
        sh(
                """
                    aws s3 cp ${target_file} \
                        s3://mdtp-lambda-functions-integration/${env.JOB_BASE_NAME}/${env.JOB_BASE_NAME}_${git_id}.zip \
                        --acl=bucket-owner-full-control --only-show-errors
                    aws s3 cp ${env.JOB_BASE_NAME}.zip.base64sha256 \
                        s3://mdtp-lambda-functions-integration/${env.JOB_BASE_NAME}/${env.JOB_BASE_NAME}_${git_id}.zip.base64sha256 \
                        --content-type text/plain --acl=bucket-owner-full-control --only-show-errors
                    """
        )
      }
    }
    stage('Deploy to Integration') {
      steps {
        build(
                job: 'api-platform-admin-api/deploy_lambda',
                parameters: [
                        [$class: 'StringParameterValue', name: 'ARTEFACT', value: env.JOB_BASE_NAME],
                        [$class: 'StringParameterValue', name: 'VERSION', value: git_id],
                        [$class: 'BooleanParameterValue', name: 'DEPLOY_INTEGRATION', value: true]
                ]
        )
      }
    }
  }
}
