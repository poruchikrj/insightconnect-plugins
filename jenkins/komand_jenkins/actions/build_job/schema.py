# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Start a build job"


class Input:
    NAME = "name"
    PARAMETERS = "parameters"
    

class Output:
    BUILD_NUMBER = "build_number"
    JOB_NUMBER = "job_number"
    

class BuildJobInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Job name",
      "order": 1
    },
    "parameters": {
      "type": "object",
      "title": "Parameters",
      "description": "Dictionary of job parameters",
      "order": 2
    }
  },
  "required": [
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class BuildJobOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "build_number": {
      "type": "integer",
      "title": "Build Number",
      "description": "Build number",
      "order": 2
    },
    "job_number": {
      "type": "integer",
      "title": "Job Number",
      "description": "Item queue ID",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
