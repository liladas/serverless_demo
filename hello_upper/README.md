# Upper/Lower Hello World Lambda Function

Single python file lambda with no dependencies.

Converts a supplied word to all lower or upper [default] case.

# Quick Note:

Make sure to update your AWS_ACCOUNT setting (I should put it in an ENV so it's not committed to source).
* https://github.com/liladas/serverless_demo/blob/1a5a6c5901e531a5933c264c483e942c883613a1/hello_upper/Makefile#L14
* The account is used to template out the ROLE_ARN used for the lambda deploy.

Just one of the few deficiencies left over from a hasty session of coding up the demo and making the repo public :)


## Usage


```console
$ make help
Project Makefile Usage:
help                           display usage and available targets
info                           show project/lambda settings
list                           list contents of directory
clean                          clean workspace and deploy bucket
inspect-zip                    inspect deployment package
function-arn                   get function arn
open-lambda                    show lambda console
create-function                create the lambda function
update-function-code           update the function code
update-function-configuration  update function configuration
delete-function                delete the lambda function
invoke-function-upper          invoke the lambda function (upper)
invoke-function-lower          invoke the lambda function (lower)
invoke-function-faulty         invoke w/ error
dump-lower-logs                show some filter log output
dump-logs                      show some log output
show-cw                        open cloudwatch
```

```console
$ make info
building: hello_upper demo
runtime: python3.7 lambda_function.lambda_handler
role: arn:aws:iam::0011222333445:role/reps-demo-lambda-upper
package: s3://reps-demo-deployment-pkg/hello_upper/hello_upper.zip
```

```console
$ make inspect-zip
zip -r ./hello_upper.zip ./lambda_function.py
  adding: lambda_function.py (deflated 61%)
zipinfo -1 ./hello_upper.zip
lambda_function.py
```


```console
make create-function
...
```

```console
make delete-function
```
