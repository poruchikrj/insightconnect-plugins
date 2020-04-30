# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Return tracked email objects"


class Input:
    ADVANCED_OPTIONS = "advanced_options"
    END_DATE = "end_date"
    MESSAGE_ID = "message_id"
    SEARCH_REASON = "search_reason"
    START_DATE = "start_date"
    

class Output:
    TRACKED_EMAILS = "tracked_emails"
    

class MessageFinderSearchInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "advanced_options": {
      "$ref": "#/definitions/advanced_options",
      "title": "Advanced Track And Trace Options",
      "description": "An object describing the advanced filters to use in the tracking query",
      "order": 5
    },
    "end_date": {
      "type": "string",
      "title": "End Date",
      "description": "The date and time of the latest message to track, in the following format, 2011-12-03T10:15:30+0000",
      "order": 2
    },
    "message_id": {
      "type": "string",
      "title": "Message ID",
      "description": "The internet message ID of the message to track",
      "order": 4
    },
    "search_reason": {
      "type": "string",
      "title": "Search Reason",
      "description": "Reason for Tracking a email, used for activity tracking puposes",
      "order": 3
    },
    "start_date": {
      "type": "string",
      "title": "Start Date",
      "description": "The date and time of the earliest message to track, in the following format, 2011-12-03T10:15:30+0000",
      "order": 1
    }
  },
  "definitions": {
    "advanced_options": {
      "type": "object",
      "title": "advanced_options",
      "properties": {
        "from": {
          "type": "string",
          "title": "From",
          "description": "The sending email address or domain of the messages to track",
          "order": 1
        },
        "senderIP": {
          "type": "string",
          "title": "Sender IP",
          "description": "The source IP address of messages to track",
          "order": 4
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "description": "The subject of the messages to track",
          "order": 3
        },
        "to": {
          "type": "string",
          "title": "To",
          "description": "The recipient email address or domain of the messages to track",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MessageFinderSearchOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tracked_emails": {
      "type": "array",
      "title": "Tracked Emails",
      "description": "An array of tracked email objects",
      "items": {
        "$ref": "#/definitions/tracked_emails"
      },
      "order": 1
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
    },
    "tracked_emails": {
      "type": "object",
      "title": "tracked_emails",
      "properties": {
        "attachments": {
          "type": "boolean",
          "title": "Attachments",
          "description": "If the message has attachments",
          "order": 1
        },
        "fromEnv": {
          "$ref": "#/definitions/email_address",
          "title": "From Envelope",
          "description": "An object describing the envelope from address of the message",
          "order": 2
        },
        "fromHdr": {
          "$ref": "#/definitions/email_address",
          "title": "From HDR",
          "description": "An object describing the header from address of the message",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The Mimecast ID of the message. Used to load more information about the message",
          "order": 4
        },
        "received": {
          "type": "string",
          "title": "Received",
          "description": "The date and time the message was received by Mimecast",
          "order": 5
        },
        "route": {
          "type": "string",
          "title": "Route",
          "description": "The route of the message",
          "order": 6
        },
        "senderIP": {
          "type": "string",
          "title": "Sender IP",
          "description": "The source IP address of the message",
          "order": 7
        },
        "sent": {
          "type": "string",
          "title": "Sent",
          "description": "The date and time that the message was sent / processed by Mimecast",
          "order": 8
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of the message",
          "order": 9
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "description": "The subject of the message",
          "order": 10
        },
        "to": {
          "type": "array",
          "title": "To",
          "description": "An array of recipient objects",
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
