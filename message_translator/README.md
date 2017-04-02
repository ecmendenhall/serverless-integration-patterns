# Message Translator

[Read about this pattern](http://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html)

## Service information
```
Service Information
service: message-translator
stage: dev
region: us-east-1
api keys:
  None
  endpoints:
    POST - https://997rabjyp5.execute-api.us-east-1.amazonaws.com/dev/soapQL
    functions:
      soap-service: message-translator-dev-soap-service
```
(Your stage, region, and endpoints may vary)

## Setup

This example includes Python dependencies. Before deploying, make sure you run:

```
pip install -t vendor -r requirements.txt
```

You'll also need to get a token for the GitHub GraphQL API. See [the documentation here](https://developer.github.com/early-access/graphql/guides/accessing-graphql/) for details.

## About

GitHub has a cool new [GraphQL API](https://developer.github.com/early-access/graphql/), but it's not very enterprisey. Let's make it talk SOAP instead.

This example creates a `/soapQL` endpoint that accepts a GraphQL query as a SOAP message:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
  <env:Header>
    <apiToken>
    YOUR_API_TOKEN_HERE
    </apiToken>
  </env:Header>
  <env:Body>
    <runGraphQLQuery>
      <query>
        query { viewer { name repositories(last:5) { nodes { name description } } } }
      </query>
    </runGraphQLQuery>
  </env:Body>
</env:Envelope>
```

On the way in, we convert this to JSON and send the query to the Github API. On the way back, we convert it back to XML:

```sh
$ curl -X POST https://997rabjyp5.execute-api.us-east-1.amazonaws.com/dev/soapQL --data @sample_request.xml
<?xml version="1.0" encoding="UTF-8"?>
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
  <env:Body>
    <runGraphQLQueryResponse>
      <data>
        <viewer>
          <login>ecmendenhall</login>
          <repositories>
            <nodes>
              <item>
                <name>beetrace</name>
                <description>🐝 play a bee movie sound effect on every system call</description>
              </item>
              <item>
                <name>refactoring-infrastructure</name>
                <description/>
              </item>
              <item>
                <name>serverless-integration-patterns</name>
                <description>⚡️ Enterprise Integration Patterns using AWS Lambda and serverless</description>
              </item>
            </nodes>
          </repositories>
        </viewer>
      </data>
    </runGraphQLQueryResponse>
  </env:Body>
</env:Envelope>
```

Technologies of the future, yesterday!
