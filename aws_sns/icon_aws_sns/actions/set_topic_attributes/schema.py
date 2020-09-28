# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class SetTopicAttributesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attribute_name": {
      "type": "string",
      "title": "Attribute Name",
      "description": "The name of the attribute you want to set",
      "order": 2
    },
    "attribute_value": {
      "type": "string",
      "title": "Attribute Value",
      "description": "The new value for the attribute",
      "order": 3
    },
    "topic_arn": {
      "type": "string",
      "title": "Topic Arn",
      "description": "The ARN of the topic to modify",
      "order": 1
    }
  },
  "required": [
    "topic_arn",
    "attribute_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SetTopicAttributesOutput(insightconnect_plugin_runtime.Output):
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
