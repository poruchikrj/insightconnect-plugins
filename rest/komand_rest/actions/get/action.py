import komand
from .schema import GetInput, GetOutput
# Custom imports below
from komand_rest.util.util import Common
import requests
import urllib.parse as parse


class Get(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get',
            description='Make a GET request',
            input=GetInput(),
            output=GetOutput())

    def run(self, params={}):
        route = params.get("route")
        headers = params.get("headers", {})

        req_headers = Common.merge_dicts(self.connection.default_headers,
                                         headers)
        url = parse.urljoin(self.connection.base_url, route)
        response = requests.get(url, headers=req_headers,
                                verify=self.connection.ssl_verify, auth=self.connection.auth)
        body_object = {}
        try:
            body_object = response.json()
        except ValueError:
            """ Nothing? We don't care if it fails, that could be normal """
        # It's possible to have a successful call with no body
        # https://stackoverflow.com/questions/32319845/python-requests-gives-none-response-where-json-data-is-expected
        if body_object == None:
            body_object = {}

        resp_headers = Common.copy_dict(response.headers)
        return {
            'body_object': body_object if isinstance(body_object, dict) else {"object": body_object},
            'body_string': response.text,
            'status': response.status_code,
            'headers': resp_headers,
        }

    def test(self):
        # TODO: Implement test function
        return {}
