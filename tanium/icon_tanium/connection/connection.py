import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from komand.exceptions import ConnectionTestException
from icon_tanium.util.resource_requests import ResourceRequests
import requests


class Connection(insightconnect_plugin_runtime.Connection):

    _LOGIN_URI = "api/v2/session/login"
    _VALIDATE = "api/v2/session/validate"

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.host = params.get(Input.HOST)
        verify_ssl = params.get(Input.VERIFY_SSL)
        domain = params.get(Input.DOMAIN)
        username = params.get(Input.USERNAME_AND_PASSWORD).get('username')
        password = params.get(Input.USERNAME_AND_PASSWORD).get('password')

        # set login url
        self.host = self.clean_host(self.host)
        self.logger.info(f"trying to connect to {self.host}")
        login_url = f"{self.host}{self._LOGIN_URI}"

        # request session key
        authentication = {"username": username, "domain": domain, "password": password}
        self.key = self.login(login_url, authentication, verify_ssl)

        # create resource_requester for use in all actions
        self.resource_requester = ResourceRequests(self.host, self.key, verify_ssl, self.logger)

    def test(self):
        validate_url = f"{self.host}{self._VALIDATE}"
        response = requests.post(validate_url, json=self.key)
        if response.status_code in range(400 - 499):
            raise ConnectionTestException(cause="validation failed",
                                          assistance="check that the host and user password were both correct",
                                          data=f"returned body was:\n {response.text}")

        try:
            validate_key = response.json()
        except ValueError:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.INVALID_JSON)

        try:
            key = validate_key["data"]
        except KeyError:
            raise ConnectionTestException(cause="The login request returned a malformed session key",
                                          assistance="Contact support for assistance",
                                          data=f"returned body was:\n {response.text}")
        self.logger.info("connection test successful")
        return

    @staticmethod
    def login(host: str, authentication: dict, verify_ssl: bool) -> dict:
        """
        Gets a session key which will be used for authentication of all API calls other than login
        :param host: The host FQDN or IP + the login URI
        :param authentication: A authentication dictionary
        :param verify_ssl: Strictly enforce signed certificates
        """
        response = requests.post(host, json=authentication, verify_ssl=verify_ssl)
        if response.status_code in range(400-499):
            raise ConnectionTestException(cause="Login attempt failed",
                                          assistance="check that the host and user password were both correct",
                                          data=f"returned body was:\n {response.text}")
        try:
            session_key = response.json()
        except ValueError:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.INVALID_JSON)
        try:
            key = session_key["data"]
        except KeyError:
            raise ConnectionTestException(cause="The login request returned a malformed session key",
                                          assistance="Contact support for assistance",
                                          data=f"returned body was:\n {response.text}")
        return key

    @staticmethod
    def clean_host(host: str) -> str:
        """
        Checks the host name for proper formatting and correctly formats it if needed
        :param host: The host FQDN or IP
        :return: correctly formatted host
        """
        if host.startswith("http://"):
            host = host[7:]
        if not host.startswith("https://"):
            host = f"https://{host}"
        if not host.endswith("/"):
            host = f"{host}/"
        return host
