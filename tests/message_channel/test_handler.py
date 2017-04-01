import json
import mock
from unittest2 import TestCase

from tests.test_helper import captured_output
import message_channel.handler as handler


@mock.patch('message_channel.handler.channel')
class TestSendMessageHandler(TestCase):

    def test_returns_200(self, mock_channel):
        response = handler.send_message({}, {})
        self.assertEqual(response['statusCode'], 200)

    def test_returns_body(self, mock_channel):
        response = handler.send_message({}, {})
        self.assertIsNotNone(response['body'])

    def test_returns_message_in_body(self, mock_channel):
        response = handler.send_message({}, {})
        body = json.loads(response['body'])
        message = body['message']
        self.assertEqual(message, "Sent a message to the channel: Hello, world!")

    @mock.patch('message_channel.handler.api_gateway')
    def test_returns_message_from_event(self, mock_gateway, mock_channel):
        mock_gateway.parse_event.return_value = "Some message"
        response = handler.send_message({}, {})
        body = json.loads(response['body'])
        message = body['message']
        self.assertEqual(message, "Sent a message to the channel: Some message")

@mock.patch('message_channel.handler.channel')
class TestReceiveMessageHandler(TestCase):

    def test_returns_message_from_event(self, mock_channel):
        mock_channel.parse_event.return_value = "Some message"
        with captured_output() as (out, err):
          response = handler.receive_message({}, {})
        self.assertEqual(out.getvalue().strip(), "Received a message: Some message")
