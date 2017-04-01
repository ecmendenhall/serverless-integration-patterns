import base64
import boto3
import json
import os


def send_message(message):
    event_data = json.dumps({"message": message})
    channel_name = os.environ.get('MESSAGE_CHANNEL_NAME')
    client = boto3.client('kinesis')
    client.put_record(
        StreamName=channel_name,
        Data=event_data,
        PartitionKey='default-partition-key'
    )

def parse_event(event):
    records = event['Records']
    b64_data = records[0]['kinesis']['data']
    body = json.loads(base64.b64decode(b64_data))
    message = body.get('message')
    return message or ''
