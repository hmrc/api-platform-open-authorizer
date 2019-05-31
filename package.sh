#!/bin/bash

set -xeou
yum install -y zip python36

PIPPACKAGESDIR=./packages
ZIP_FILE=api-platform-open-authorizer.zip

rm -rf ${ZIP_FILE}
rm -rf ${PIPPACKAGESDIR}

zip ${ZIP_FILE} lambda_function.py api_request_details.py

# @TODO Insert this code if this project gets requirements
#mkdir -p ${PIPPACKAGESDIR}
#pip-3.6 install -t ${PIPPACKAGESDIR} -r requirements.txt
#cd ${PIPPACKAGESDIR}
#zip -r ../${ZIP_FILE} .
