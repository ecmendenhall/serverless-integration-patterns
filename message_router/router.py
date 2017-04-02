from lib import sns

SUPPORTED_PRODUCTS = {'whozits', 'whatzits', 'thingamabobs'}

def route(event, context):
    order_data = sns.parse_data(event)
    product = order_data.get('product')
    if product in SUPPORTED_PRODUCTS:
      product_topic = '{}-order'.format(product)
      sns.send_data(order_data, product_topic)
    else:
      print "Error: Invalid product {}".format(product)
