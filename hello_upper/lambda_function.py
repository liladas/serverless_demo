#!/usr/bin/env python

'''
https://gist.github.com/liladas/94a9d6510ec55188baa20481c3b7a225

# open the aws console for this function
open https://us-east-2.console.aws.amazon.com/lambda/home?region=us-east-2#/functions/hello_upper?tab=configuration

# do an uppercase (default) operation
aws lambda invoke  --function-name hello_upper  --payload '{ "word": "example" }' response.json;
cat response.json;

# do a lowercase operation
aws lambda invoke  --function-name hello_upper  --payload '{ "word": "ALL_CAPS", "operation": "lower"  }' response.json;
cat response.json;

# do an invalid request
aws lambda invoke  --function-name hello_upper  --payload '{ "wordx": "ALL_CAPS", "operation": "lower"  }' response.json;

# print some logs using CLI (this isn't a very useful thing...)
aws logs filter-log-events --log-group-name /aws/lambda/hello_upper --filter-pattern "lower" | jq .events[].message | sed 's/"//g'

# print some logs, no filter
aws logs filter-log-events --log-group-name /aws/lambda/hello_upper | jq .events[].message | sed 's/"//g'

# show cloudwatch
open https://us-east-2.console.aws.amazon.com/cloudwatch/home?region=us-east-2#logStream:group=/aws/lambda/hello_upper;streamFilter=typeLogStreamPrefix

'''

import json
import time


def uppercase(string):
    ''' upper the letters in the string '''
    return string.upper()


def lowercase(string):
    ''' lowercase the letters in the string '''
    return string.lower()


# function mapping
string_function_mapping = {
    'lower': lowercase,
    'upper': uppercase
}


def lambda_handler(event, context):
    # print the event object
    print(json.dumps(event, indent=2, sort_keys=True))

    # print some of the context object items
    print("Log stream name:", context.log_stream_name)
    print("Log group name:",  context.log_group_name)
    print("Request ID:",context.aws_request_id)
    print("Mem. limits(MB):", context.memory_limit_in_mb)

    # Code will execute quickly, so we add a 1 second intentional delay so you can see that in time remaining value.
    time.sleep(1)
    print("Time remaining (MS):", context.get_remaining_time_in_millis())

    string_operation =  event.get('operation', 'upper')
    word =  event.get('word', None)

    if not word:
        print("No word specified...")
        return dict(word=None, error="no word specified")

    new_word = string_function_mapping[string_operation](word)

    print("%s ==> %s ==> %s" % (word, string_operation, new_word ))

    return dict(word=word, new_word=new_word, operation=string_operation)
