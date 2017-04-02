# Pipes and Filters

[Read about this pattern](http://www.enterpriseintegrationpatterns.com/patterns/messaging/PipesAndFilters.html)

## Service information

```
Service Information
service: pipes-and-filters
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  POST - https://t0ykcfmdm4.execute-api.us-east-1.amazonaws.com/dev/start
functions:
  start-pipeline: pipes-and-filters-dev-start-pipeline
  lowercase: pipes-and-filters-dev-lowercase
  no-fun: pipes-and-filters-dev-no-fun
  exclamation-points: pipes-and-filters-dev-exclamation-points
  not-too-excited: pipes-and-filters-dev-not-too-excited
  sparkles-emoji: pipes-and-filters-dev-sparkles-emoji
```
(Your stage, region, and endpoints may vary)

## About

This example defines 6 Lambdas, which form a pipeline. Each one transforms the incoming message in some way or filters it out completely. After each one processes a message, it notifies an SNS topic. To kick it off, `POST` to the `/start` endpoint:

```
$ curl -X POST https://t0ykcfmdm4.execute-api.us-east-1.amazonaws.com/dev/start \
  --data '{"message": "HERE WE GO"}'
{"message": "Got a new message: HERE WE GO. Notifying lambdas subscribed to the 'new-message' topic."}
```

Tail the logs from each function in sequence to see the transformations:

```
$ sls logs -f lowercase
START RequestId: 31403194-175c-11e7-991d-3397a79e8947 Version: $LATEST

Received message: HERE WE GO.  Transformed to here we go.
Notifying lambdas subscribed to the lowercased-message topic.

END RequestId: 31403194-175c-11e7-991d-3397a79e8947
REPORT RequestId: 31403194-175c-11e7-991d-3397a79e8947	Duration: 232.65 ms	Billed Duration: 300 ms 	Memory Size: 1024 MB	Max Memory Used: 34 MB
```

```
$ sls logs -f no-fun
START RequestId: 31b4294c-175c-11e7-951e-4f464beb9f5a Version: $LATEST

Received message: here we go.
Notifying lambdas subscribed to the no-fun-message topic.

END RequestId: 31b4294c-175c-11e7-951e-4f464beb9f5a
REPORT RequestId: 31b4294c-175c-11e7-951e-4f464beb9f5a	Duration: 130.05 ms	Billed Duration: 200 ms 	Memory Size: 1024 MB	Max Memory Used: 26 MB
```

```
$ sls logs -f exclamation-points
START RequestId: 32030cbd-175c-11e7-b1c9-65c4c192e929 Version: $LATEST

Received message: here we go.  Transformed to here we go!!!.
Notifying lambdas subscribed to the exclamation-points-message topic.

END RequestId: 32030cbd-175c-11e7-b1c9-65c4c192e929
REPORT RequestId: 32030cbd-175c-11e7-b1c9-65c4c192e929	Duration: 133.30 ms	Billed Duration: 200 ms 	Memory Size: 1024 MB	Max Memory Used: 26 MB
```

```
$ sls logs -f not-too-excited
START RequestId: 32ba4e21-175c-11e7-9e6c-2559fcd2abde Version: $LATEST

Received message: here we go!!!.
Notifying lambdas subscribed to the not-too-excited-message topic.

END RequestId: 32ba4e21-175c-11e7-9e6c-2559fcd2abde
REPORT RequestId: 32ba4e21-175c-11e7-9e6c-2559fcd2abde	Duration: 329.00 ms	Billed Duration: 400 ms 	Memory Size: 1024 MB	Max Memory Used: 34 MB
```

```
$ sls logs -f sparkles-emoji
START RequestId: 338d076b-175c-11e7-bcad-75159176d351 Version: $LATEST

Received message: here we go!!!.  Transformed to ✨  here we go!!! ✨ .

END RequestId: 338d076b-175c-11e7-bcad-75159176d351
REPORT RequestId: 338d076b-175c-11e7-bcad-75159176d351	Duration: 0.34 ms	Billed Duration: 100 ms 	Memory Size: 1024 MB	Max Memory Used: 21 MB
```
