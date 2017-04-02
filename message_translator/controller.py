import github
import translators
import soap


def run_query(xml):
    params = translators.xml_to_dict(xml)
    response = github.graphQL(
      query=params.get('query'),
      token=params.get('token')
    )
    status = response['status_code']

    if status == 200:
      body = soap.build_response(response)
    else:
      body = None

    return status, body
