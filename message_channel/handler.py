import json

import lib.api_gateway as api_gateway
import lib.sns as sns


def send_message(event, context):
    message = api_gateway.parse_event(event) or "Hello, world!"
    channel = 'message-channel'
    sns.send_message(message, channel)

    response_message = "Sent a message to channel {}: {}".format(channel, message)
    body = {
        "message": response_message
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def receive_message(event, context):
    message = sns.parse_event(event)
    print "Received a message: {}".format(message)
