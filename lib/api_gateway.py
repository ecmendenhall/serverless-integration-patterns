import json

def parse_event(event):
    body_json = event.get('body', '{}') or '{}'
    body = json.loads(body_json)
    message = body.get('message', '')
    return message or ''