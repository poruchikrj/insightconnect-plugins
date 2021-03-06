# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Lookup URL"


class Input:
    URL = "url"
    

class Output:
    CREATED = "created"
    DOMAIN = "domain"
    FOUND = "found"
    IPS = "ips"
    LOCATION = "location"
    SOURCES = "sources"
    UPDATED = "updated"
    

class UrlLookupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "url": {
      "type": "string",
      "title": "Url",
      "description": "Full URL E.g. http://faker.su/data/entry/steam/Steam.exe",
      "order": 1
    }
  },
  "required": [
    "url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UrlLookupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "created": {
      "type": "string",
      "title": "Created Date",
      "description": "Created date",
      "order": 2
    },
    "domain": {
      "type": "string",
      "title": "Cymon Domain URL",
      "description": "Cymon Domain URL",
      "order": 6
    },
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Found in database",
      "order": 7
    },
    "ips": {
      "type": "array",
      "title": "Cymon IP URLs",
      "description": "Cymon IPs URL",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "location": {
      "type": "string",
      "title": "Location",
      "description": "Location",
      "order": 1
    },
    "sources": {
      "type": "array",
      "title": "Sources",
      "description": "Sources",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "updated": {
      "type": "string",
      "title": "Updated Date",
      "description": "Updated date",
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
