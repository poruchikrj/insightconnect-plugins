# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class SubscribeInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "endpoint": {
      "type": "string",
      "title": "Endpoint",
      "description": "The endpoint that you want to receive notifications",
      "order": 3
    },
    "protocol": {
      "type": "string",
      "title": "Protocol",
      "description": "The protocol you want to use",
      "order": 2
    },
    "topic_arn": {
      "type": "string",
      "title": "Topic Arn",
      "description": "The ARN of the topic you want to subscribe to",
      "order": 1
    }
  },
  "required": [
    "topic_arn",
    "protocol"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SubscribeOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response_metadata": {
      "$ref": "#/definitions/response_metadata",
      "title": "Response Metadata",
      "description": "Metadata about the response from AWS",
      "order": 1
    },
    "subscription_arn": {
      "type": "string",
      "title": "Subscription Arn",
      "description": "The ARN of the subscription, if the service was able to create a subscription immediately (without requiring endpoint owner confirmation)",
      "order": 2
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
