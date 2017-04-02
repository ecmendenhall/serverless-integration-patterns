import sys
import os
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendor"))

import json

import lib.api_gateway as api_gateway
import controller

def soap_service(event, context):
    xml = api_gateway.parse_raw_body(event)
    status, body = controller.run_query(xml)
    return {
      "statusCode": status,
      "body": body
    }
