import json
import mock
from unittest2 import TestCase

import message_router.handler as handler

@mock.patch('message_router.handler.api_gateway')
class TestCreateOrder(TestCase):

    def test_parses_api_gateway_event(self, mock_gateway):
        handler.create({}, {})
        self.assertTrue(mock_gateway.parse_body.called)

    def test_returns_201(self, mock_gateway):
        mock_gateway.parse_body.return_value = {}
        response = handler.create({}, {})
        self.assertEqual(response['statusCode'], 201)

    @mock.patch('message_router.handler.orders')
    def test_parses_api_gateway_event(self, mock_orders, mock_gateway):
        order_data = {
          "product": "whozits",
          "quantity": 3
        }
        mock_gateway.parse_body.return_value = order_data

        handler.create({}, {})

        mock_orders.create.assert_called_with(order_data)


@mock.patch('message_router.handler.orders')
class TestListOrders(TestCase):

    def test_returns_200(self, mock_orders):
        mock_orders.stats.return_value = {}
        response = handler.list({}, {})
        self.assertEqual(response['statusCode'], 200)

    def test_returns_order_stats(self, mock_orders):
        order_stats = {
          "whozits": 10,
          "whatzits": 5,
          "thingamabobs": 3
        }
        mock_orders.stats.return_value = order_stats
        response = handler.list({}, {})
        self.assertEqual(response['body'], json.dumps(order_stats))
