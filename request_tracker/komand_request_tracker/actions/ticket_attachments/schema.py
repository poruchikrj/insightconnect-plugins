# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Gets a list of all attachments related to the ticket"


class Input:
    TICKET_ID = "ticket_id"
    

class Output:
    ATTACHMENTS = "Attachments"
    

class TicketAttachmentsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ticket_id": {
      "type": "integer",
      "title": "Ticket ID",
      "description": "Ticket ID e.g. 3",
      "order": 1
    }
  },
  "required": [
    "ticket_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TicketAttachmentsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "Attachments": {
      "type": "array",
      "title": "Attatchments",
      "description": "Attatchments",
      "items": {
        "$ref": "#/definitions/Attachment"
      },
      "order": 1
    }
  },
  "definitions": {
    "Attachment": {
      "type": "object",
      "title": "Attachment",
      "properties": {
        "ContentType": {
          "type": "string",
          "title": "ContentType",
          "order": 4
        },
        "Name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "Size": {
          "type": "string",
          "title": "Size",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
