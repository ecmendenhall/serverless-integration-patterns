from unittest2 import TestCase
import mock

from message_translator import controller

@mock.patch('message_translator.controller.github')
@mock.patch('message_translator.controller.translators')
@mock.patch('message_translator.controller.soap')
class TestController(TestCase):

    def test_builds_response_on_successful_query(self, soap, translators, github):
        translators.xml_to_dict.return_value = {}
        query_response = {'status_code': 200, 'data': {}}
        github.graphQL.return_value = query_response

        controller.run_query('<xml />')

        self.assertTrue(soap.build_response.called)

    def test_returns_status_code_on_successful_query(self, soap, translators, github):
        translators.xml_to_dict.return_value = {}
        query_response = {'status_code': 200, 'data': {}}
        github.graphQL.return_value = query_response

        status, body = controller.run_query('<xml />')

        self.assertEqual(status, 200)

    def test_returns_empty_body_on_unsuccessful_query(self, soap, translators, github):
        translators.xml_to_dict.return_value = {}
        query_response = {'status_code': 500, 'data': {}}
        github.graphQL.return_value = query_response

        status, body = controller.run_query('<xml />')

        self.assertFalse(soap.build_response.called)
        self.assertIsNone(body)

    def test_returns_status_code_on_unsuccessful_query(self, soap, translators, github):
        translators.xml_to_dict.return_value = {}
        query_response = {'status_code': 500, 'data': {}}
        github.graphQL.return_value = query_response

        status, body = controller.run_query('<xml />')

        self.assertEqual(status, 500)
