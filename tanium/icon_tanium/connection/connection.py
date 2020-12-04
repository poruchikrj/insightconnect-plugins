import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from komand.exceptions import ConnectionTestException
from icon_tanium.util.resource_requests import ResourceRequests
import requests


class Connection(insightconnect_plugin_runtime.Connection):

    LOGIN_URI = "api/v2/session/login"

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        host = params.get(Input.HOST)
        verify_ssl = params.get(Input.VERIFY_SSL)
        domain = params.get(Input.DOMAIN)
        username = params.get(Input.USERNAME_AND_PASSWORD).get('username')
        password = params.get(Input.USERNAME_AND_PASSWORD).get('password')

        # set login url
        host = self.clean_host(host)
        self.logger.info(f"trying to connect to {host}")
        login_url = f"{host}{self.LOGIN_URI}"

        # request session key
        authentication = {"username": username, "domain": domain, "password": password}
        key = self.login(login_url, authentication, verify_ssl)

        # create resource_requester for use in all actions
        self.resource_requester = ResourceRequests(host, key, verify_ssl, self.logger)

    def test(self):
        # TODO: Implement connection test
        pass

    def login(self, host: str, authentication: dict, verify_ssl: bool) -> dict:
        """
        Gets a session key which will be used for authentication of all API calls other than login
        :param host: The host FQDN or IP + the login URI
        :param authentication: A authentication dictionary
        :param verify_ssl: Strictly enforce signed certificates
        """
        response = requests.post(host, json=authentication, verify_ssl=verify_ssl)
        if response.status_code in range(400-499):
            self.logger.error(f"Login returned non 2xx status code. return body was:\n {response.text}")
            raise ConnectionTestException()
        try:
            session_key = response.json()
        except ValueError:
            raise ConnectionTestException()
        try:
            key = session_key["data"]
        except KeyError:
            raise ConnectionTestException()
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
