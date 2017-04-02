from xml.etree import ElementTree
from StringIO import StringIO
import xml.dom.minidom as minidom

import translators

def build_response(response):
    if response['errors']:
        data_element = translators.dict_to_xml(response['errors'], 'errors')
    else:
        data_element = translators.dict_to_xml(response['data'], 'data')
    return build_envelope(data_element)


def build_envelope(data_element):
    ns = {
      'env': 'http://www.w3.org/2003/05/soap-envelope',
    }

    envelope = ElementTree.Element('env:Envelope', ns)
    namespace = envelope.attrib['env']
    envelope.attrib['xmlns:env'] = namespace
    del(envelope.attrib['env'])
    body = ElementTree.SubElement(envelope, 'env:Body')
    query_response = ElementTree.SubElement(body, 'runGraphQLQueryResponse')
    query_response.append(data_element)
    string = StringIO()
    document = ElementTree.ElementTree(envelope)
    document.write(string, encoding="UTF-8", xml_declaration=True)
    ugly_markup = string.getvalue()
    return minidom.parseString(ugly_markup).toprettyxml(encoding="UTF-8", indent=" ")

