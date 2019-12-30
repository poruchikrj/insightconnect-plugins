# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Convert HTML to PDF"


class Input:
    DOC = "doc"
    

class Output:
    PDF = "pdf"
    

class PdfInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "doc": {
      "type": "string",
      "title": "Document",
      "description": "Document to transform",
      "order": 1
    }
  },
  "required": [
    "doc"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PdfOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "pdf": {
      "type": "string",
      "title": "PDF",
      "displayType": "bytes",
      "description": "PDF File",
      "format": "bytes",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)