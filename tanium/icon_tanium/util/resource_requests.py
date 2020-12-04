from komand.exceptions import PluginException
import requests


class ResourceRequests(object):
    """
    Class for helper methods for making requests against the APIv3. A new instance should
    be instantiated within the action/trigger being developed. New methods should be
    created as instance methods to allow reference of the logger and session passed to
    the __init__ function during instantiation.
    """

    def __init__(self, base_url, key: dict, verify: bool, logger):
        """
        Creates a new instance of ResourceHelper
        :param key: Authentication key to the Tanium server
        :param verify: Strictly enforce signed certificates
        :param logger: Logger object available to Insightconnect actions/triggers, usually self.logger
        :return: ResourceHelper object
        """
        self.session = requests.Session()
        self.base_url = base_url
        self.logger = logger
        self.verify = verify
        self.session.headers.update(key)

    def resource_request(self, uri: str, method: str = 'get', params: dict = None, payload: dict = None):
        """
        Sends a request to the tanium server with the provided uri and optional method params and payload
        :param uri: URI for the API call
        :param method: HTTP method for the API request
        :param params: URL parameters to append to the request
        :param payload: JSON body for the API request if required
        :return: Dict containing the JSON response body
        """
        url = f"{self.base_url}{uri}"
        self.logger.info(f"sending request to endpoint:\n {url}")
        extras = {"json": payload, "params": params}
        response = self.session.request(method, url, verify=self.verify, **extras)
        self.status_code_check(response.text, response.status_code)
        try:
            data = response.json()
        except ValueError:
            self.logger.error(f"invalid JSON response body was:\n {response.text}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        return data

    def status_code_check(self, response_text, status_code):
        """
        Checks for non 2xx status codes and raises an exception if found
        :param response_text: The text of the response
        :param status_code: response status code
        :return: None
        """