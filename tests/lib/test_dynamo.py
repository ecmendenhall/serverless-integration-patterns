import json
import mock
from unittest2 import TestCase

import lib.dynamo as dynamo

@mock.patch('lib.dynamo.boto3')
class TestSendMessageToSNSTopic(TestCase):

    def test_creates_dynamo_client(self, mock_boto3):
        dynamo.put('some-table', {"lol": "wut"})
        mock_boto3.client.assert_called_with('dynamodb')

    def test_calls_put(self, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client

        dynamo.put('some-table', {"lol": "wut"})

        self.assertTrue(mock_client.put_item.called)

    def test_calls_put_with_table(self, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client

        dynamo.put('some-table', {"lol": "wut"})

        args, kwargs = mock_client.put_item.call_args
        self.assertEqual(kwargs['TableName'], 'some-table')

    def test_calls_put_with_item(self, mock_boto3):
        mock_client = mock.MagicMock()
        mock_boto3.client.return_value = mock_client

        dynamo.put('some-table', {"lol": "wut"})

        args, kwargs = mock_client.put_item.call_args
        self.assertEqual(kwargs['Item'], {"lol": "wut"})

