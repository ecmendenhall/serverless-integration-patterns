from unittest2 import TestCase
import mock

import message_translator.github as github

@mock.patch('message_translator.github.requests')
class TestGithubAPI(TestCase):

    def test_posts_query_to_github(self, mock_requests):
        github.graphQL(
          query="query { viewer { login } }",
          token='abc123'
        )
        args, kwargs = mock_requests.post.call_args
        self.assertEqual(args[0], 'https://api.github.com/graphql')

    def test_posts_auth_header(self, mock_requests):
        github.graphQL(
          query="query { viewer { login } }",
          token='abc123'
        )
        args, kwargs = mock_requests.post.call_args

        expected_headers = {'Authorization': 'bearer abc123'}
        self.assertEqual(kwargs['headers'], expected_headers)

    def test_posts_query_json(self, mock_requests):
        github.graphQL(
          query="query { viewer { login } }",
          token='abc123'
        )
        args, kwargs = mock_requests.post.call_args

        self.assertEqual(kwargs['json'], {"query": "query { viewer { login } }"})
