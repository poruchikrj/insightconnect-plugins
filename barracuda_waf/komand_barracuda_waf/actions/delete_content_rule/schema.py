# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Deletes the given content rule"


class Input:
    ID = "id"
    VIRTUAL_SERVICE_ID = "virtual_service_id"
    

class Output:
    MSG = "msg"
    

class DeleteContentRuleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Content rule ID",
      "order": 2
    },
    "virtual_service_id": {
      "type": "string",
      "title": "Virtual Service ID",
      "description": "Virtual Service ID",
      "order": 1
    }
  },
  "required": [
    "id",
    "virtual_service_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteContentRuleOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "msg": {
      "type": "string",
      "title": "Message",
      "description": "Message of deleted",
      "order": 1
    }
  },
  "required": [
    "msg"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
