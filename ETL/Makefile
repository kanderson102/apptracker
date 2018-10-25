PROJECT: s3_lambda_py
VIRTUAL_ENV: /git/apptracker
FUNCTION_NAME: s3_lambda_py
AWS_REGION: us-east-1
FUNCTION_HANDLER: lambda_handler
LAMBDA_ROLE: arn:aws:iam::606818331634:role/S3_API_Cloud_RDS

buid_package_tmp:
	mkdir -p ../package/tmp
	cp -a ./$(PROJECT)/ ../package/tmp/

copy_python:
	if test -d $(VIRTUAL_ENV)/lib; then \
		cp $(VIRTUAL_ENV)/lib/python3.6/site-packages/
