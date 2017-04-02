from unittest2 import TestCase
import mock

from tests.test_helper import captured_output
from pipes_and_filters import handler

@mock.patch('pipes_and_filters.handler.sns')
class TestTransformers(TestCase):

    def setUp(self):
      self.transformer = handler.make_transformer(
        lambda msg: '!{}!'.format(msg), 'transformed-message'
      )

    def test_parses_sns_event(self, mock_sns):
        with captured_output() as (out, err):
          self.transformer({}, {})
        self.assertTrue(mock_sns.parse_event.called)

    def test_transforms_message(self, mock_sns):
        mock_sns.parse_event.return_value = 'message'

        with captured_output() as (out, err):
          self.transformer({}, {})
        self.assertIn('!message!', out.getvalue().strip())

    def test_notifies_topic_when_provided(self, mock_sns):
        mock_sns.parse_event.return_value = 'message'

        with captured_output() as (out, err):
          self.transformer({}, {})
        mock_sns.send_message.assert_called_with('!message!', 'transformed-message')

    def test_does_not_notify_topic_when_missing(self, mock_sns):
        mock_sns.parse_event.return_value = 'message'
        transformer = handler.make_transformer(lambda m: m)

        with captured_output() as (out, err):
          transformer({}, {})
        self.assertFalse(mock_sns.send_message.called)


@mock.patch('pipes_and_filters.handler.sns')
class TestFilters(TestCase):

    def setUp(self):
      self.filter = handler.make_filter(
        lambda msg: '!' not in msg, 'filtered-message'
      )

    def test_parses_sns_event(self, mock_sns):
        with captured_output() as (out, err):
          self.filter({}, {})
        self.assertTrue(mock_sns.parse_event.called)

    def test_prints_message(self, mock_sns):
        mock_sns.parse_event.return_value = '!'

        with captured_output() as (out, err):
          self.filter({}, {})
        self.assertIn('Received message: !', out.getvalue().strip())

    def test_filters_message(self, mock_sns):
        mock_sns.parse_event.return_value = '!'

        with captured_output() as (out, err):
          self.filter({}, {})
        self.assertIn('Message filtered.', out.getvalue().strip())
        self.assertFalse(mock_sns.send_message.called)


    def test_notifies_topic_when_provided(self, mock_sns):
        mock_sns.parse_event.return_value = 'message'

        with captured_output() as (out, err):
          self.filter({}, {})
        mock_sns.send_message.assert_called_with('message', 'filtered-message')

    def test_does_not_notify_topic_when_missing(self, mock_sns):
        mock_sns.parse_event.return_value = 'message'
        no_notify_filter = handler.make_filter(lambda m: m)

        with captured_output() as (out, err):
          no_notify_filter({}, {})
        self.assertFalse(mock_sns.send_message.called)
