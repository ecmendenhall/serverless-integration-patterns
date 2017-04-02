import json

import lib.api_gateway as api_gateway
import orders

def create(event, context):
    data = api_gateway.parse_body(event)
    orders.create(data)
    return {"statusCode": 201}


def list(event, context):
    order_stats = orders.stats()
    return {
      "statusCode": 200,
      "body": json.dumps(order_stats)
    }

