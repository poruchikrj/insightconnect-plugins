# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Keep fields from CSV string"


class Input:
    CSV = "csv"
    FIELDS = "fields"
    

class Output:
    STRING = "string"
    

class FilterStringInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "csv": {
      "type": "string",
      "title": "Csv",
      "description": "CSV string",
      "order": 1
    },
    "fields": {
      "type": "string",
      "title": "Fields",
      "description": "Fields to filter",
      "order": 2
    }
  },
  "required": [
    "csv",
    "fields"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class FilterStringOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "string": {
      "type": "string",
      "title": "String",
      "description": "Filtered CSV string",
      "order": 1
    }
  },
  "required": [
    "string"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
