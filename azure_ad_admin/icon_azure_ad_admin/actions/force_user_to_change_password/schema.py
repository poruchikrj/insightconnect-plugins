# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Forces a user to change their password on their next successful login"


class Input:
    USER_ID = "user_id"
    

class Output:
    SUCCESS = "success"
    

class ForceUserToChangePasswordInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID",
      "order": 1
    }
  },
  "required": [
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ForceUserToChangePasswordOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
