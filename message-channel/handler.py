import json

import api_gateway
import channel

def send_message(event, context):
    message = api_gateway.parse_event(event)
    channel.send_message(event)

    body = {
        "message": "Sent a message to the channel!",
        "event": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def receive_message(event, context):
    print "Received a message!"
