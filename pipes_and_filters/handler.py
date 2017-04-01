import json

import lib.api_gateway as api_gateway
import lib.sns as sns

import filters


def start_pipeline(event, context):
    message = api_gateway.parse_event(event)
    reponse_message = ''

    if message:
      sns.send_message(message, 'new-message')
      response_message = "Got a new message: {}. Notifying lambdas subscribed to the 'new-message' topic.".format(message)

    body = {
        "message": response_message
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def make_transformer(transformer_function, notify_topic=None):
    def transformer(event, context):
        message = sns.parse_event(event)
        transformed_message = transformer_function(message)
        print "Received message: {}.  Transformed to {}.".format(message, transformed_message)
        if notify_topic:
          sns.send_message(transformed_message, notify_topic)
          print "Notifying lambdas subscribed to the {} topic.".format(notify_topic)
    return transformer

def make_filter(filter_function, notify_topic=None):
    def filter(event, context):
        message = sns.parse_event(event)
        print "Received message: {}.".format(message)
        if filter_function(message):
          if notify_topic:
            sns.send_message(message, notify_topic)
            print "Notifying lambdas subscribed to the {} topic.".format(notify_topic)
        else:
            print "Message filtered."
    return filter

lowercase_filter = make_transformer(filters.lowercase, 'lowercased-message')
no_fun_filter = make_filter(filters.no_fun, 'no-fun-message')
exclamation_points_filter = make_transformer(filters.exclamation_points, 'exclamation-points-message')
not_too_excited_filter = make_filter(filters.not_too_excited, 'not-too-excited-message')
sparkles_emoji_filter = make_transformer(filters.sparkles_emoji)
