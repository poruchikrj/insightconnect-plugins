# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class GetSubscriptionAttributesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "subscription_arn": {
      "type": "string",
      "title": "Subscription Arn",
      "description": "The ARN of the subscription whose properties you want to get",
      "order": 1
    }
  },
  "required": [
    "subscription_arn"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSubscriptionAttributesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attributes": {
      "type": "object",
      "title": "Attributes",
      "description": "A map of the subscriptions attributes",
      "order": 2
    },
    "response_metadata": {
      "$ref": "#/definitions/response_metadata",
      "title": "Response Metadata",
      "description": "Metadata about the response from AWS",
      "order": 1
    }
  },
  "required": [
    "response_metadata"
  ],
  "definitions": {
    "response_metadata": {
      "type": "object",
      "title": "response_metadata",
      "properties": {
        "http_status_code": {
          "type": "integer",
          "title": "Http Status Code",
          "description": "HTTP status code for the request",
          "order": 2
        },
        "request_id": {
          "type": "string",
          "title": "Request Id",
          "description": "Unique identifier for the request",
          "order": 1
        }
      },
      "required": [
        "request_id",
        "http_status_code"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
