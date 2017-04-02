from unittest2 import TestCase
from xml.etree import ElementTree

import message_translator.translators as translators


class TestXMLTranslator(TestCase):

    def setUp(self):
        self.raw_soap = '''<?xml version="1.0" encoding="UTF-8"?>
         <env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
             <env:Header>
                 <apiToken>
                 abcd1234
                 </apiToken>
             </env:Header>
             <env:Body>
                <runGraphQLQuery>
                    <query>
                     query { viewer { login } }
                    </query>
                </runGraphQLQuery>
             </env:Body>
         </env:Envelope>
        '''
        self.converted_json = "<data><viewer><login>ecmendenhall</login></viewer></data>"

    def test_returns_api_token(self):
        token = translators.xml_to_dict(self.raw_soap).get('token')
        self.assertEqual(token, 'abcd1234')

    def test_returns_query(self):
        query = translators.xml_to_dict(self.raw_soap).get('query')
        self.assertEqual(query, "query { viewer { login } }")

    def test_converts_dict_to_xml(self):
        data_dict = {"viewer": {"login": "ecmendenhall"}}
        xml = translators.dict_to_xml(data_dict, 'data')
        self.assertEqual(ElementTree.tostring(xml), self.converted_json)
