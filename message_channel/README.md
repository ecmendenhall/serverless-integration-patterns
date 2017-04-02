# Message Channel 
[Read about this pattern](http://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html)

## Service Information 
```
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
(Your region, stage, and enpoints may vary)

## About 

This example uses an SNS topic as a message channel between two Lambdas. `POST` to the `/message-channel/send` endpoint to trigger the `send-message` function:

```sh
$ curl -X POST https://gb6e8kd2r0.execute-api.us-east-1.amazonaws.com/dev/message-channel/send \ 
  --data '{"message": "Every time I do this Jeff Bezos gets a nickel."}'
{"message": "Sent a message to channel message-channel: Every time I do this Jeff Bezos gets a nickel."}%
```

The `send-message` function will take your message and publish it to an SNS topic called `message-channel`. `receive-message` is subscribed to the topic. When it's triggered by a new message, it prints it out to the console. You can tail a function's logs with `serverless logs -f <function name>`:

```sh
$ serverless logs -f send-message -t
START RequestId: e1646cec-175a-11e7-bcf2-afa4f132cdd4 Version: $LATEST
Received a message: Every time I do this Jeff Bezos gets a nickel.
END RequestId: e1646cec-175a-11e7-bcf2-afa4f132cdd4
REPORT RequestId: e1646cec-175a-11e7-bcf2-afa4f132cdd4	Duration: 0.36 ms	Billed Duration: 100 ms 	Memory Size: 1024 MB	Max Memory Used: 21 MB
```
