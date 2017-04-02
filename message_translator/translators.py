from xml.etree import ElementTree
import dicttoxml


def xml_to_dict(raw_xml):
    ns = {
     'soap': 'http://www.w3.org/2003/05/soap-envelope',
    }
    root = ElementTree.fromstring(raw_xml)
    api_token = root.find('.soap:Header/apiToken', ns).text.strip()
    query = root.find('.soap:Body/runGraphQLQuery/query', ns).text.strip()
    return {"token": api_token, "query": query}


def dict_to_xml(data, root_element_tag):
    data_snippet = dicttoxml.dicttoxml(data, attr_type=False, root=False)
    root_element = ElementTree.Element(root_element_tag)
    data_element = ElementTree.fromstring(data_snippet)
    root_element.append(data_element)
    return root_element
