from unittest2 import TestCase
import mock

import message_translator.handler as handler

@mock.patch('message_translator.handler.controller')
@mock.patch('message_translator.handler.api_gateway')
class TestSoapService(TestCase):

    def test_reads_raw_data_from_gateway_event(self, mock_gateway, mock_controller):
        mock_controller.run_query.return_value = (200, {})
        handler.soap_service({}, {})
        self.assertTrue(mock_gateway.parse_raw_body.called)

    def test_returns_status_from_controller(self, mock_gateway, mock_controller):
        mock_controller.run_query.return_value = (200, {})
        response = handler.soap_service({}, {})
        self.assertEqual(response['statusCode'], 200)

    def test_returns_status_from_controller(self, mock_gateway, mock_controller):
        mock_controller.run_query.return_value = (200, 'body')
        response = handler.soap_service({}, {})
        self.assertEqual(response['body'], 'body')
