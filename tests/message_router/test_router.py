from unittest2 import TestCase
import mock

from tests.test_helper import captured_output
from message_router import router

@mock.patch('message_router.router.sns')
class TestRouter(TestCase):

    def test_parses_data_from_sns(self, mock_sns):
        router.route({}, {})
        self.assertTrue(mock_sns.parse_data.called)

    def test_notifies_whozits_orders(self, mock_sns):
        order_data = {
          "product": "whozits",
          "quantity": 3
        }
        mock_sns.parse_data.return_value = order_data

        router.route({}, {})

        mock_sns.send_data.assert_called_with(
          order_data,
          'whozits-order'
        )

    def test_notifies_whatzits_orders(self, mock_sns):
        order_data = {
          "product": "whatzits",
          "quantity": 3
        }
        mock_sns.parse_data.return_value = order_data

        router.route({}, {})

        mock_sns.send_data.assert_called_with(
          order_data,
          'whatzits-order'
        )

    def test_notifies_thingamabobs_orders(self, mock_sns):
        order_data = {
          "product": "thingamabobs",
          "quantity": 3
        }
        mock_sns.parse_data.return_value = order_data

        router.route({}, {})

        mock_sns.send_data.assert_called_with(
          order_data,
          'thingamabobs-order'
        )

    def test_prints_error_on_unknown_product(self, mock_sns):
        order_data = {
          "product": "widgets",
          "quantity": 3
        }
        mock_sns.parse_data.return_value = order_data

        with captured_output() as (out, err):
          router.route({}, {})
        self.assertEqual(out.getvalue().strip(), "Error: Invalid product widgets")
