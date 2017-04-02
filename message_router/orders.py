from lib import sns, dynamo

def create(order_data):
    if order_data:
      sns.send_data(order_data, 'new-order')


def _product_stats(product):
    table = '{}-orders'.format(product)
    orders = dynamo.scan(table, 'quantity')
    total_ordered = sum(int(item['quantity']['N']) for item in orders)
    return {
      "number_of_orders": len(orders),
      "total_quantity_ordered": total_ordered
    }


def stats():
    return {
      "whozits": _product_stats('whozits'),
      "whatzits": _product_stats('whatzits'),
      "thingamabobs": _product_stats('thingamabobs'),
    }
