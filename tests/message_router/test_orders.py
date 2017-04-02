from unittest2 import TestCase
import mock

from message_router import orders


@mock.patch('message_router.orders.sns')
class TestCreateOrder(TestCase):

    def test_notifies_new_order_topic(self, mock_sns):
        order_data = {
          "product": "whozits",
          "quantity": 3
        }

        orders.create(order_data)

        mock_sns.send_data.assert_called_with(order_data, 'new-order')


@mock.patch('message_router.orders.dynamo')
class TestCreateOrder(TestCase):

    def test_notifies_new_order_topic(self, mock_dynamo):
        mock_dynamo.scan.return_value = [
          {"quantity": {"N": "1"}},
          {"quantity": {"N": "2"}},
          {"quantity": {"N": "3"}}
        ]
        expected_stats = {
          "whozits": {
              "number_of_orders": 3,
              "total_quantity_ordered": 6
          },
          "whatzits": {
              "number_of_orders": 3,
              "total_quantity_ordered": 6
          },
          "thingamabobs": {
              "number_of_orders": 3,
              "total_quantity_ordered": 6
          }
        }

        stats = orders.stats()
        self.assertEqual(stats, expected_stats)

