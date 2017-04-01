import json
from unittest2 import TestCase

import handler

class TestApiGatewayParser(TestCase):

    def test_returns_200(self):
        response = handler.send_message({}, {})
        self.assertEqual(response['statusCode'], 200)

    def test_returns_body(self):
        response = handler.send_message({}, {})
        self.assertIsNotNone(response['body'])

    def test_returns_message_in_body(self):
        response = handler.send_message({}, {})
        body = json.loads(response['body'])
        message = body['message']
        self.assertEqual(message, "Sent a message to the channel!")
