import boto3
import json
import os


def send_message(message, topic):
    client = boto3.client('sns')
    prefix = os.environ.get('SNS_TOPIC_ARN_PREFIX')
    topic_arn = '{}:{}'.format(prefix, topic)
    client.publish(
      TopicArn=topic_arn,
      Message=json.dumps({"message": message})
    )

def parse_event(event):
    records = event['Records']
    data = records[0]['Sns']['Message']
    body = json.loads(data)
    message = body.get('message')
    return message or ''
