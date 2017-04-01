import json

import lib.api_gateway as api_gateway
import lib.channel as channel


def send_message(event, context):
    message = api_gateway.parse_event(event) or "Hello, world!"
    channel.send_message(message)

    response_message = "Sent a message to the channel: {}".format(message)
    body = {
        "message": response_message
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def receive_message(event, context):
    message = channel.parse_event(event)
    print "Received a message: {}".format(message)
