import base64
import json
import mock
from unittest2 import TestCase

import lib.channel as channel

@mock.patch('lib.channel.boto3')
class TestSendToChannel(TestCase):

    def test_creates_kinesis_client(self, mock_boto3):
        channel.send_message("message")
        mock_boto3.client.assert_called_with('kinesis')

    def test_calls_put_record(self, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client

        channel.send_message("message")

        mock_client.put_record.assert_called()

    def test_calls_put_record_with_message(self, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client
        message_json = json.dumps({'message': 'message'})

        channel.send_message("message")

        args, kwargs = mock_client.put_record.call_args
        self.assertEqual(kwargs['Data'], message_json)

    def test_calls_put_record_with_partition_key(self, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client

        channel.send_message("message")

        args, kwargs = mock_client.put_record.call_args
        self.assertEqual(kwargs['PartitionKey'], 'default-partition-key')

    @mock.patch('lib.channel.os')
    def test_calls_put_record_with_channel_name(self, mock_os, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client
        mock_os.environ = {'MESSAGE_CHANNEL_NAME': 'channel'}

        channel.send_message("message")

        args, kwargs = mock_client.put_record.call_args
        self.assertEqual(kwargs['StreamName'], 'channel')


class TestReadFromChannel(TestCase):

    def test_decodes_message_body(self):
        b64_body_data = base64.b64encode(json.dumps({"message": "message"}))
        event = {
          'Records': [
            {'kinesis': {'data': b64_body_data}}
          ]
        }

        message = channel.parse_event(event)

        self.assertEqual(message, "message")

    def test_returns_first_message(self):
        message1_b64_body_data = base64.b64encode(json.dumps({"message": "message 1"}))
        message2_b64_body_data = base64.b64encode(json.dumps({"message": "message 2"}))
        event = {
          'Records': [
            {'kinesis': {'data': message1_b64_body_data}},
            {'kinesis': {'data': message2_b64_body_data}}
          ]
        }

        message = channel.parse_event(event)

        self.assertEqual(message, "message 1")

    def test_returns_empty_message_when_missing(self):
        b64_body_data = base64.b64encode(json.dumps({}))
        event = {
          'Records': [
            {'kinesis': {'data': b64_body_data}}
          ]
        }

        message = channel.parse_event(event)

        self.assertEqual(message, "")
