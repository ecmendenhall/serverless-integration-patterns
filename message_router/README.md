# Message Router

[Read about this pattern](http://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageRouter.html)

## Service information
```
Service Information
service: message-router
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  POST - https://ldevpx1po1.execute-api.us-east-1.amazonaws.com/dev/orders/create
  GET - https://ldevpx1po1.execute-api.us-east-1.amazonaws.com/dev/orders
functions:
  create-order: message-router-dev-create-order
  list-orders: message-router-dev-list-orders
  router: message-router-dev-router
  whozits: message-router-dev-whozits
  whatzits: message-router-dev-whatzits
  thingamabobs: message-router-dev-thingamabobs
```
(Your stage, region, and endpoints may vary)

## About

Now we're getting enterprisey. This example models an order system with three products: `whozits`, `whatzits`, and `thingamabobs`. To place a new order, `POST` to the `create-order` service at `/orders/create` with a `product` and `quantity` in the JSON body:

```
$ curl -X POST https://ldevpx1po1.execute-api.us-east-1.amazonaws.com/dev/orders/create 
  --data '{"product": "whozits", "quantity": 1}'
```

The `create-order` service sends all new orders to the `new-order` topic. New orders trigger the `router` service, which decides what to do with them: 

1) It sends `whozits`, `whatzits`, and `thingamabobs` orders to `whozits-order`, `whatzits-order`, and `thingamabobs-order` topics, respectively.
2) It filters out products that don't exist.

Each product's order service listens on the associated `<product>-order` topic, and saves the order to a DynamoDB table.

A `GET` to the The `list-orders` service at `/orders` prints out order count and totals for each product:

```
$ curl -s https://ldevpx1po1.execute-api.us-east-1.amazonaws.com/dev/orders | python -m json.tool
{
    "thingamabobs": {
        "number_of_orders": 0,
        "total_quantity_ordered": 0
    },
    "whatzits": {
        "number_of_orders": 0,
        "total_quantity_ordered": 0
    },
    "whozits": {
        "number_of_orders": 1,
        "total_quantity_ordered": 1
    }
}
```
