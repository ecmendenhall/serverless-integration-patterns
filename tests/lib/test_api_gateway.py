import json
from unittest2 import TestCase

import lib.api_gateway as api_gateway


class TestApiGatewayParser(TestCase):

    def test_returns_message_from_event_body_json(self):
        message = "Hello!"
        message_json = json.dumps({"message": message})
        parsed_message = api_gateway.parse_event({'body': message_json})
        self.assertEqual(message, parsed_message)

    def test_handles_missing_message(self):
        message_json = json.dumps({"message": None})
        parsed_message = api_gateway.parse_event({'body': message_json})
        self.assertEqual("", parsed_message)

    def test_handles_missing_body(self):
        parsed_message = api_gateway.parse_event({"body": None})
        self.assertEqual("", parsed_message)
