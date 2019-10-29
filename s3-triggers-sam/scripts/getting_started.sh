# install sam-cli via homebrew
brew tap aws/tap
brew install aws-sam-cli

# got warnings about fs perms
sudo chown -R $(whoami) /usr/local/bin /usr/local/include /usr/local/lib /usr/local/share /usr/local/share/doc /usr/local/share/man /usr/local/share/man/man1
chmod u+w /usr/local/bin /usr/local/include /usr/local/lib /usr/local/share /usr/local/share/doc /usr/local/share/man /usr/local/share/man/man1

# install
brew install aws-sam-cli
sam --version


#Make sure that the Region for this bucket aligns with where you deploy
aws s3 mb s3://reps-demo-deployment-pkg --region us-east-2  # Example regions: us-east-1, ap-east-1, eu-central-1, sa-east-1

# Step 1 - Download a sample application
sam init --runtime python3.7

cd sam-app # make edits to suit my needs...

# Step 2 - Build your application

# docker neeeds to be running for this to succeed
sam build --use-container

# Starting Build inside a container
# Building resource 'S3TriggersFunction'
#
# Fetching lambci/lambda:build-python3.7 Docker container image................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
# Mounting /Users/adam/proj/serverless_demo/s3-triggers-sam/s3_triggers as /tmp/samcli/source:ro,delegated inside runtime container
#
# Build Succeeded
#
# Built Artifacts  : .aws-sam/build
# Built Template   : .aws-sam/build/template.yaml
#
# Commands you can use next
# =========================
# [*] Invoke Function: sam local invoke
# [*] Package: sam package --s3-bucket <yourbucket>

# Step 3 - Package your application
sam package --output-template packaged.yaml --s3-bucket reps-demo-deployment-pkg

# Step 4 - Deploy your application
sam deploy --template-file packaged.yaml --region us-east-2 --capabilities CAPABILITY_IAM --stack-name reps-demo-s3-triggers
