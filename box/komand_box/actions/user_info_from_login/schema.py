# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve user information using their login ID"


class Input:
    LOGIN = "login"
    

class Output:
    ADDRESS = "address"
    AVATAR_URL = "avatar_url"
    ID = "id"
    JOB_TITLE = "job_title"
    LOGIN = "login"
    NAME = "name"
    PHONE = "phone"
    SPACE_AMOUNT = "space_amount"
    SPACE_USED = "space_used"
    TIMEZONE = "timezone"
    

class UserInfoFromLoginInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "login": {
      "type": "string",
      "title": "User Login",
      "description": "User's login e.g. bob@hotmail.com",
      "order": 1
    }
  },
  "required": [
    "login"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UserInfoFromLoginOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "User Address",
      "description": "User address",
      "order": 9
    },
    "avatar_url": {
      "type": "string",
      "title": "User Avatar",
      "description": "User avatar",
      "order": 10
    },
    "id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID",
      "order": 2
    },
    "job_title": {
      "type": "string",
      "title": "Job Title",
      "description": "Job title",
      "order": 7
    },
    "login": {
      "type": "string",
      "title": "User Email",
      "description": "User email",
      "order": 1
    },
    "name": {
      "type": "string",
      "title": "Username",
      "description": "Username",
      "order": 3
    },
    "phone": {
      "type": "string",
      "title": "User Phone Number",
      "description": "User phone number",
      "order": 8
    },
    "space_amount": {
      "type": "number",
      "title": "Max Space Amount",
      "description": "Max space amount",
      "order": 5
    },
    "space_used": {
      "type": "number",
      "title": "Space Used",
      "description": "Space used",
      "order": 6
    },
    "timezone": {
      "type": "string",
      "title": "Timezone",
      "description": "Timezone",
      "order": 4
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
