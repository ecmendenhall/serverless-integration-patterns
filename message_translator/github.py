import requests


def graphQL(query, token):
    auth_header = 'bearer {}'.format(token)
    response = requests.post(
      'https://api.github.com/graphql',
      headers={'Authorization': auth_header},
      json={"query": query}
    )
    errors = response.json().get('errors')
    data = response.json().get('data')
    return {
      "status_code": response.status_code,
      "errors": errors,
      "data": data
    }

