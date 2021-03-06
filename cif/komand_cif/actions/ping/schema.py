# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Ping the router"


class Input:
    pass

class Output:
    TIMESTAMP = "timestamp"
    

class PingInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PingOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "timestamp": {
      "type": "array",
      "title": "Timestamp",
      "description": "Timestamp",
      "items": {
        "type": "integer"
      },
      "order": 1
    }
  },
  "required": [
    "timestamp"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
