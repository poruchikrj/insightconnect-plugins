# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    API_KEY = "api_key"
    REGION = "region"
    SSL_VERIFY = "ssl_verify"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "Enter API key e.g. 8lzx2lnr7uwyu27abc7jjo0ezo3",
      "order": 2
    },
    "region": {
      "type": "string",
      "title": "Region",
      "description": "Select a region e.g. US",
      "default": "US",
      "enum": [
        "US",
        "Europe"
      ],
      "order": 1
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "SSL verify",
      "default": false,
      "order": 3
    }
  },
  "required": [
    "api_key",
    "region",
    "ssl_verify"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
