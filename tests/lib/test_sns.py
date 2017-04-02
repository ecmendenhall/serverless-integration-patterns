import json
import mock
from unittest2 import TestCase

import lib.sns as sns

@mock.patch('lib.sns.boto3')
class TestSendMessageToSNSTopic(TestCase):

    def test_creates_sns_client(self, mock_boto3):
        sns.send_message('message', 'topic')
        mock_boto3.client.assert_called_with('sns')

    def test_calls_publish(self, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client

        sns.send_message('message', 'topic')

        self.assertTrue(mock_client.publish.called)

    def test_calls_publish_with_message(self, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client
        message_json = json.dumps({'message': 'message'})

        sns.send_message('message', 'topic')

        args, kwargs = mock_client.publish.call_args
        self.assertEqual(kwargs['Message'], message_json)

    @mock.patch('lib.sns.os')
    def test_calls_publish_with_topic_arn(self, mock_os, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client
        mock_os.environ = {'SNS_TOPIC_ARN_PREFIX': 'arn:aws:sns:us-east-1:12345'}

        sns.send_message('message', 'topic')

        args, kwargs = mock_client.publish.call_args
        self.assertEqual(kwargs['TopicArn'], 'arn:aws:sns:us-east-1:12345:topic')


@mock.patch('lib.sns.boto3')
class TestSendDataToSNSTopic(TestCase):

    def test_creates_sns_client(self, mock_boto3):
        sns.send_data({"lol": "wut"}, 'topic')
        mock_boto3.client.assert_called_with('sns')

    def test_calls_publish(self, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client

        sns.send_data({"lol": "wut"}, 'topic')

        self.assertTrue(mock_client.publish.called)

    def test_calls_publish_with_serialized_data(self, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client
        data = {"lol": "wut"}
        message_json = json.dumps(data)

        sns.send_data(data, 'topic')

        args, kwargs = mock_client.publish.call_args
        self.assertEqual(kwargs['Message'], message_json)

    @mock.patch('lib.sns.os')
    def test_calls_publish_with_topic_arn(self, mock_os, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client
        mock_os.environ = {'SNS_TOPIC_ARN_PREFIX': 'arn:aws:sns:us-east-1:12345'}

        sns.send_data({"lol": "wut"}, 'topic')

        args, kwargs = mock_client.publish.call_args
        self.assertEqual(kwargs['TopicArn'], 'arn:aws:sns:us-east-1:12345:topic')
