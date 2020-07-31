# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CLIENT_ID = "client_id"
    CLIENT_SECRET = "client_secret"
    REGION = "region"
    TENANT_ID = "tenant_id"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "client_id": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Client ID",
      "description": "Client ID for Sophos Central instance",
      "order": 3
    },
    "client_secret": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Client Secret",
      "description": "Client secret key that allows access to Sophos Central",
      "order": 2
    },
    "region": {
      "type": "string",
      "title": "API region",
      "description": "API region",
      "default": "US East",
      "enum": [
        "US West",
        "US East",
        "EU Ireland",
        "DE Germany"
      ],
      "order": 1
    },
    "tenant_id": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Tenant ID",
      "description": "Tenant ID for Sophos Central instance",
      "order": 4
    }
  },
  "required": [
    "client_id",
    "client_secret"
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