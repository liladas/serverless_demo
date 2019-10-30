# REPS & Co -- AWS Serverless Demo

# Quick note -- Work-in-Progress

This is a work-in-progress/concept I put together for a meetup to present SAM CLI.

You'll have to follow some of the getting started tutorials for getting all the dependencies.

Also check out https://stedolan.github.io/jq/ (used in the makefiles)

Please feel free to submit issues/pull_requests w/ questions/concerns/improvements/needs. 

My intention is to turn this repo into a "Serverless Scaffold" that will include logical placement of settings.py, logging conventions, and other boilerplate to enable faster development while maintaining thoughtful best-practices (like the Makefile scheme).

# Introduction to AWS Serverless

[Google Slides - REPS Prezo -- AWS Series -- Serverless Applications with Python](https://docs.google.com/presentation/d/1Dx-7KUNVpKzywl1skV7UHH41SRSPiaYyEkVShvsgTOs/edit?usp=sharing)

## Hello Upper, a very basic serverless application (single file lambda function)

[Hello Upper](./hello_upper)

Given a word, return a lowercase or uppercase version.

This is just to show how to bundle and zip a very simple application


## S3 Trigger Events Application using AWS SAM

[S3 Triggers](./s3-triggers-sam)

Follow the guide for installation:
* https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html

# Changes...

See the [Changelog](./CHANGELOG.md) for the latest happenings to this repo.
