import uuid

from lib import sns, dynamo


def whozits(event, context):
    order_data = sns.parse_data(event)
    quantity = order_data.get('quantity')
    dynamo.put('whozits-orders', {
        "order_id": { 'S': str(uuid.uuid4()) },
        "quantity": { 'N': str(quantity) }
    })


def whatzits(event, context):
    order_data = sns.parse_data(event)
    quantity = order_data.get('quantity')
    dynamo.put('whatzits-orders', {
        "order_id": { 'S': str(uuid.uuid4()) },
        "quantity": { 'N': str(quantity) }
    })


def thingamabobs(event, context):
    order_data = sns.parse_data(event)
    quantity = order_data.get('quantity')
    dynamo.put('thingamabobs-orders', {
        "order_id": { 'S': str(uuid.uuid4()) },
        "quantity": { 'N': str(quantity) }
    })
