from unittest2 import TestCase
import mock

from message_router import products

@mock.patch('message_router.products.uuid')
@mock.patch('message_router.products.dynamo')
@mock.patch('message_router.products.sns')
class TestWhozits(TestCase):

    def test_parses_sns_data(self, mock_sns, mock_dynamo, mock_uuid):
        products.whozits({}, {})
        self.assertTrue(mock_sns.parse_data.called)

    def test_persists_order_data(self, mock_sns, mock_dynamo, mock_uuid):
        mock_uuid.uuid4.return_value = 'some-uuid'
        mock_sns.parse_data.return_value = {
          "quantity": 3
        }

        products.whozits({}, {})

        mock_dynamo.put.assert_called_with(
          'whozits-orders',
          {"order_id": {'S': 'some-uuid'}, "quantity": {'N': '3'}}
        )

@mock.patch('message_router.products.uuid')
@mock.patch('message_router.products.dynamo')
@mock.patch('message_router.products.sns')
class TestWhatzits(TestCase):

    def test_parses_sns_data(self, mock_sns, mock_dynamo, mock_uuid):
        products.whatzits({}, {})
        self.assertTrue(mock_sns.parse_data.called)

    def test_persists_order_data(self, mock_sns, mock_dynamo, mock_uuid):
        mock_uuid.uuid4.return_value = 'some-uuid'
        mock_sns.parse_data.return_value = {
          "quantity": 3
        }

        products.whatzits({}, {})

        mock_dynamo.put.assert_called_with(
          'whatzits-orders',
          {"order_id": {'S': 'some-uuid'}, "quantity": {'N': '3'}}
        )


@mock.patch('message_router.products.uuid')
@mock.patch('message_router.products.dynamo')
@mock.patch('message_router.products.sns')
class TestThingamabobs(TestCase):

    def test_parses_sns_data(self, mock_sns, mock_dynamo, mock_uuid):
        products.thingamabobs({}, {})
        self.assertTrue(mock_sns.parse_data.called)

    def test_persists_order_data(self, mock_sns, mock_dynamo, mock_uuid):
        mock_uuid.uuid4.return_value = 'some-uuid'
        mock_sns.parse_data.return_value = {
          "quantity": 3
        }

        products.thingamabobs({}, {})

        mock_dynamo.put.assert_called_with(
          'thingamabobs-orders',
          {"order_id": {'S': 'some-uuid'}, "quantity": {'N': '3'}}
        )
