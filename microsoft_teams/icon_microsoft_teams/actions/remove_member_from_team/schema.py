# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Remove a member from a team"


class Input:
    MEMBER_LOGIN = "member_login"
    TEAM_NAME = "team_name"
    

class Output:
    SUCCESS = "success"
    

class RemoveMemberFromTeamInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "member_login": {
      "type": "string",
      "title": "Member Login",
      "description": "Member Login e.g. user@example.com",
      "order": 2
    },
    "team_name": {
      "type": "string",
      "title": "Team Name",
      "description": "Team name",
      "order": 1
    }
  },
  "required": [
    "member_login",
    "team_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveMemberFromTeamOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Boolean indicating if this action was successful",
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
