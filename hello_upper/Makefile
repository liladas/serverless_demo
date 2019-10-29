# PROJECT DETAILS
PROJECT = hello_upper
DESCRIPTION = "REPS & Co - AWS Serverless Demo - Upper Lower Case"
FUNCTION = $(PROJECT)
ENV = demo


# BUILD SETTINGS
# single file
SRC_FILE = lambda_function.py


# AWS SETTINGS
AWS_ACCOUNT = 00112233
REGION = us-east-2
ROLE_ARN = arn:aws:iam::$(AWS_ACCOUNT):role/$(FUNCTION)
ROLE_ARN = arn:aws:iam::$(AWS_ACCOUNT):role/reps-demo-lambda-upper


# RUNTIME INFO
RUNTIME = python3.7
HANDLER = lambda_function.lambda_handler


## Define where to store deployment package
S3_BUCKET = reps-demo-deployment-pkg
S3_KEY=$(PROJECT)/$(FUNCTION).zip
S3_PATH = s3://$(S3_BUCKET)/$(S3_KEY)


.PHONY: help clean info list
.DEFAULT_GOAL := help


help: ## display usage and available targets
	@echo Project Makefile Usage:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

info: ## show project/lambda settings
	@echo building: $(FUNCTION) $(ENV)
	@echo runtime: $(RUNTIME) $(HANDLER)
	@echo role: $(ROLE_ARN)
	@echo package: $(S3_PATH)

list: ## list contents of directory
	@pwd
	@tree || list

clean: ## clean workspace and deploy bucket
	rm -f ./$(FUNCTION).zip response.json
	aws s3 rm $(S3_PATH)

$(FUNCTION).zip:
	zip -r ./$(FUNCTION).zip ./lambda_function.py

zip-files: $(FUNCTION).zip

inspect-zip: $(FUNCTION).zip ## inspect deployment package
	zipinfo -1 ./$(FUNCTION).zip

upload-zip: $(FUNCTION).zip # copy deployment package to s3
	aws s3 cp ./$(FUNCTION).zip $(S3_PATH)


#########################
## awscli lambda commands
#########################
function-arn: ## get function arn
	@aws lambda get-function --function-name $(FUNCTION) | jq -r .Configuration.FunctionArn

open-lambda: ## show lambda console
	open https://us-east-2.console.aws.amazon.com/lambda/home?region=us-east-2#/functions/$(FUNCTION)

create-function: ## create the lambda function
	aws lambda create-function \
		--handler $(HANDLER) \
		--function-name $(FUNCTION) \
		--region $(REGION) \
		--code S3Bucket=$(S3_BUCKET),S3Key=$(S3_KEY) \
		--role $(ROLE_ARN) \
		--runtime $(RUNTIME) \
		--description $(DESCRIPTION)

update-function-code: ## update the function code
	aws lambda update-function-code \
		--function-name $(FUNCTION) \
		--s3-bucket $(S3_BUCKET) --s3-key $(S3_KEY) \
		--publish
		# --zip-file fileb://$(FUNCTION).zip \

update-function-configuration: ## update function configuration
	aws lambda  update-function-configuration \
	--function-name $(FUNCTION) \
	--handler $(HANDLER) \
	--environment Variables='{EXAMPLE=DUMMY}'
	# --environment Variables="{access_key_id=${ACCESS_KEY}, secret_access_key=${ACCESS_SECRET}, default_password=${DEFAULT_PASSWORD}}"

delete-function: ## delete the lambda function
	aws lambda delete-function --function-name $(FUNCTION)

invoke-function-upper: ## invoke the lambda function (upper)
	aws lambda invoke  --function-name $(FUNCTION)  --payload '{ "word": "example" }' response.json;
	cat response.json | jq;

invoke-function-lower: ## invoke the lambda function (lower)
	aws lambda invoke  --function-name hello_upper  --payload '{ "word": "ALL_CAPS", "operation": "lower"  }' response.json;
	cat response.json | jq;

invoke-function-faulty: ## invoke w/ error
	aws lambda invoke  --function-name hello_upper  --payload '{ "wordx": "ALL_CAPS", "operation": "lower"  }' response.json;
	cat response.json | jq;


#####################################
## awscli cloudwatch logs commands
#####################################
dump-lower-logs: ## show some filter log output
	aws logs filter-log-events --log-group-name /aws/lambda/hello_upper --filter-pattern "lower" | jq .events[].message | sed 's/"//g'

dump-logs: ## show some log output
	aws logs filter-log-events --log-group-name /aws/lambda/hello_upper | jq .events[].message | sed 's/"//g'

show-cw: ## open cloudwatch
	open https://us-east-2.console.aws.amazon.com/cloudwatch/home?region=us-east-2#logStream:group=/aws/lambda/$(FUNCTION)
