import boto3

def put(table, item):
  db = boto3.client('dynamodb')
  db.put_item(
    TableName=table,
    Item=item
   )

def scan(table, attribute):
  db = boto3.client('dynamodb')
  items = db.scan(
    TableName=table,
    ProjectionExpression=attribute
   )
  return items['Items']
