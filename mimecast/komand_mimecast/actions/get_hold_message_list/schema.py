# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get information about held messages"


class Input:
    ADMIN = "admin"
    END_DATE = "end_date"
    FILTER_BY = "filter_by"
    SEARCH_BY = "search_by"
    START_DATE = "start_date"
    

class Output:
    HELD_EMAILS = "held_emails"
    

class GetHoldMessageListInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "admin": {
      "type": "boolean",
      "title": "Admin",
      "description": "Level of results to return",
      "default": false,
      "order": 1
    },
    "end_date": {
      "type": "string",
      "title": "End Date Time",
      "description": "The date and time of the latest message to return, in the following format, 2011-12-03T10:15:30+0000",
      "order": 4
    },
    "filter_by": {
      "type": "array",
      "title": "Filter By",
      "description": "Filter options to narrow results",
      "items": {
        "$ref": "#/definitions/filter_by"
      },
      "order": 5
    },
    "search_by": {
      "$ref": "#/definitions/search_by",
      "title": "Search By",
      "description": "Object data used to filter results",
      "order": 2
    },
    "start_date": {
      "type": "string",
      "title": "Start Date Time",
      "description": "The date and time of the earliest message to return, in the following format, 2011-12-03T10:15:30+0000",
      "order": 3
    }
  },
  "definitions": {
    "filter_by": {
      "type": "object",
      "title": "filter_by",
      "properties": {
        "attachments": {
          "type": "boolean",
          "title": "Attachments",
          "description": "Specify if results should be held attachments",
          "default": false,
          "enum": [
            "all",
            "subject",
            "sender",
            "recipient",
            "reason_code"
          ],
          "order": 3
        },
        "held_group": {
          "type": "string",
          "title": "Held Group",
          "description": "Specify the level of hold placed on messages to return",
          "default": "administrator",
          "enum": [
            "administrator",
            "moderator",
            "user",
            "cluster"
          ],
          "order": 2
        },
        "route": {
          "type": "string",
          "title": "Route",
          "description": "Specify the route of emails to return",
          "default": "all",
          "enum": [
            "all",
            "internal",
            "outbound",
            "inbound",
            "external"
          ],
          "order": 1
        }
      }
    },
    "search_by": {
      "type": "object",
      "title": "search_by",
      "properties": {
        "field_name": {
          "type": "string",
          "title": "Field Name",
          "description": "Message fields to filter based on",
          "default": "all",
          "enum": [
            "all",
            "subject",
            "sender",
            "recipient",
            "reason_code"
          ],
          "order": 2
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "The text used to filter results",
          "default": "TODO",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetHoldMessageListOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "held_emails": {
      "type": "array",
      "title": "Held Emails",
      "description": "An array of held messages",
      "items": {
        "$ref": "#/definitions/held_emails"
      },
      "order": 1
    }
  },
  "required": [
    "held_emails"
  ],
  "definitions": {
    "email_address": {
      "type": "object",
      "title": "email_address",
      "properties": {
        "displayableName": {
          "type": "string",
          "title": "Displayable Name",
          "description": "A display name, if available",
          "order": 2
        },
        "emailAddress": {
          "type": "string",
          "title": "Email Address",
          "description": "An email address",
          "order": 1
        }
      }
    },
    "held_emails": {
      "type": "object",
      "title": "held_emails",
      "properties": {
        "attachments": {
          "type": "boolean",
          "title": "Attachments",
          "description": "Returns true if the message contains attachments; otherwise returns false",
          "order": 15
        },
        "fromEnv": {
          "$ref": "#/definitions/email_address",
          "title": "From ENV",
          "description": "Object containing the envelope from information",
          "order": 9
        },
        "fromHdr": {
          "$ref": "#/definitions/email_address",
          "title": "From HDR",
          "description": "Object containing the header from information",
          "order": 10
        },
        "heldGroup": {
          "type": "string",
          "title": "Held Group",
          "description": "The level of a message hold",
          "enum": [
            "administrator",
            "moderator",
            "user"
          ],
          "order": 2
        },
        "heldReason": {
          "type": "string",
          "title": "Held Reason",
          "description": "The general reason for holding a message",
          "order": 1
        },
        "heldSince": {
          "type": "string",
          "title": "Held Since",
          "description": "The date that the message was held",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The Mimecast secure ID of a message",
          "order": 7
        },
        "messageInfo": {
          "type": "string",
          "title": "Message Info",
          "description": "The name of the definition that held a message",
          "order": 4
        },
        "policyInfo": {
          "type": "string",
          "title": "Policy Info",
          "description": "The name of the policy that held a message",
          "order": 5
        },
        "received": {
          "type": "string",
          "title": "Received",
          "description": "The date that the message was received by Mimecast",
          "order": 12
        },
        "route": {
          "type": "string",
          "title": "Route",
          "description": "The route of the held message",
          "enum": [
            "inbound",
            "outbound",
            "internal",
            "external"
          ],
          "order": 16
        },
        "senderIP": {
          "type": "string",
          "title": "Sender IP",
          "description": "The IP address that delivered the message to Mimecast",
          "order": 14
        },
        "sent": {
          "type": "string",
          "title": "Sent",
          "description": "The date that the mesage was sent",
          "order": 17
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "The size of the message in bytes",
          "order": 6
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The current held status of a message",
          "order": 8
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "description": "The mesasge subject",
          "order": 13
        },
        "to": {
          "type": "array",
          "title": "Held Reason",
          "description": "An array of recipeint objects",
          "items": {
            "$ref": "#/definitions/email_address"
          },
          "order": 11
        }
      },
      "definitions": {
        "email_address": {
          "type": "object",
          "title": "email_address",
          "properties": {
            "displayableName": {
              "type": "string",
              "title": "Displayable Name",
              "description": "A display name, if available",
              "order": 2
            },
            "emailAddress": {
              "type": "string",
              "title": "Email Address",
              "description": "An email address",
              "order": 1
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
