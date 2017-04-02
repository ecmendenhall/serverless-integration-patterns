# Serverless Integration Patterns

[![Build Status](https://travis-ci.org/ecmendenhall/serverless-integration-patterns.svg?branch=master)](https://travis-ci.org/ecmendenhall/serverless-integration-patterns)

This project implements some of the examples from [Enterprise Integration Patterns](http://www.enterpriseintegrationpatterns.com/) using AWS Lambda and [serverless framework](https://serverless.com/).

## About
[Enterprise Integration Patterns](http://www.enterpriseintegrationpatterns.com/) is an awesome book about how to make software systems talk to each other. [AWS Lambda](https://aws.amazon.com/lambda/) is an interesting new way to run code without managing conventional servers. [Serverless](https://serverless.com/) is a way to use Lambda without tearing your hair out.

Chapter 2 of EIP defines four common integration styles: [Flat Files](http://www.enterpriseintegrationpatterns.com/patterns/messaging/FileTransferIntegration.html), [Shared Database](http://www.enterpriseintegrationpatterns.com/patterns/messaging/SharedDataBaseIntegration.html), [Remote Procedure Invocation](http://www.enterpriseintegrationpatterns.com/patterns/messaging/EncapsulatedSynchronousIntegration.html), and [Messaging](http://www.enterpriseintegrationpatterns.com/patterns/messaging/Messaging.html). Lambda's features map to each of these styles, and many of the messaging patterns in the rest of the book. Triggers for Lambda functions include:

- S3 writes (flat files)
- HTTP requests through API Gateway (RPC/messaging)
- DynamoDB triggers (shared database/messaging)
- SNS notifications (messaging)
- Kinesis streams (messaging)

It's a great toolkit for experimenting with the patterns in EIP without setting up all the enterprise stuff that needs to integrate.

## Getting Started

To deploy the examples in this repo you'll need:
  - Python 2.7.x
  - `pip`, the Python package manager
  - Node v4.x.x or higher
  - [Serverless framework](https://serverless.com/framework/docs/providers/aws/guide/installation/)
  - An AWS account
  
Once you have Node and Python, install serverless with:

```sh
$ npm install -g serverless
```
Serverless has great docs on [getting started](https://serverless.com/framework/docs/providers/aws/guide/). Give them a read and follow the instructions.

You'll also need to make sure AWS credentials are configured. Follow the [serverless docs here](https://serverless.com/framework/docs/providers/aws/guide/credentials/).
  
To install Python dependencies, run:

```sh
$ pip install -r requirements.txt
```

## Deploying the examples
Every directory in this repo containing a `serverless.yml` file is a deployable serverless application. To spin up an example, `cd` into one and run: 

```sh
$ serverless deploy
```

This will spin up all the Lambdas and necessary AWS infrastructure associated with the example:


```sh
$ serverless deploy
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
.....
Serverless: Stack create finished...
Serverless: Packaging service...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading service .zip file to S3 (9.63 KB)...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.................................................
Serverless: Stack update finished...
```

At the end of a successful deploy, it will usually print out a few API Gateway endpoints, which are usually entrypoints to the example code:

```sh
Service Information
service: message-channel
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  POST - https://gb6e8kd2r0.execute-api.us-east-1.amazonaws.com/dev/message-channel/send
functions:
  send-message: message-channel-dev-send-message
  receive-message: message-channel-dev-receive-message
```
For details on what these do, see the `README.md` files inside each example directory.

Make sure you remove all the provisioned resources when you're done. To do so, run:

```sh
$ serverless remove
```


## Tests

From the repo root, run:

```
$ nosetests
```
