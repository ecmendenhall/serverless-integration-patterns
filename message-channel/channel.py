import boto3
import json
import os


def send_message(event):
    event_data = json.dumps(event)
    client = boto3.client('kinesis')
    client.put_record(
        StreamName='MessageChannel',
        Data=event_data,
        PartitionKey='partition-key'
    )
