# PROJECT DETAILS
PROJECT = S3-Triggers-Demo
DESCRIPTION = "REPS & Co - AWS Serverless Demo - S3 Triggers Case"
ENV = demo


# AWS SETTINGS
REGION = us-east-2
PACKAGE_BUCKET = reps-demo-deployment-pkg
STACKNAME = reps-demo-s3-triggers


.PHONY: help info list
.DEFAULT_GOAL := help


help: ## display usage and available targets
	@echo Project Makefile Usage:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

info: ## show project settings
	@echo app: $(PROJECT)
	@echo description: $(DESCRIPTION)
	@echo package_bucket: $(PACKAGE_BUCKET)
	@echo stackname: $(STACKNAME)

list: ## list contents of directory
	@pwd
	@tree || list

make-pkg-bucket: ## make the deployment bucket for packaged apps
	aws s3 mb s3://$(PACKAGE_BUCKET) --region $(REGION)  # Example regions: us-east-1, ap-east-1, eu-central-1, sa-east-1

# Step 1 - Download a sample application
init: ## Initial bare sample app
	sam init --runtime python3.7

build: ## Build your application
	sam build --use-container

package: ## Package app to s3 deployment dir
	sam package --output-template packaged.yaml --s3-bucket $(PACKAGE_BUCKET)

deploy: ## Deploy app/stack
	sam deploy --template-file packaged.yaml --region $(REGION) --capabilities CAPABILITY_IAM --stack-name $(STACKNAME)

delete-stack: ## Delete stack when done
	aws cloudformation delete-stack --stack-name $(STACKNAME)

open-s3: ## Open S3 for easy uploads
	open https://us-east-2.console.aws.amazon.com/s3/object/reps-demo-triggers-bucket-dest-bucket
	open https://us-east-2.console.aws.amazon.com/s3/object/reps-demo-triggers-bucket-source-bucket
