import traceback
import logging
import requests
from requests import adapters as request_adapters
import json
from pprint import pprint
from typing import Union
import mimetypes
import binascii
import os
# Requests Framework --> http://docs.python-requests.org/en/master/api/#api-changes
# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
try:
    from httplib import HTTPConnection
except ImportError:
    from http.client import HTTPConnection  # for Python 3

_logger = logging.getLogger(__name__)
# _logger = logging.getLogger("requests.packages.urllib3")
logging.basicConfig()  # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.INFO)
_logger.setLevel(logging.INFO)
_logger.propagate = True

url = "https://{{HOST}}/api/restaurant/list/{{apikey}}"

class API:
    ENDPOINTS = {
        'restaurant': {
            'restaurant_list': '/api/restaurant/list/'
        }
    }
    HEADER = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'python-requests/2.21.0',
        'Connection': 'keep-alive',
    }
    TEST_URL = "https://httpbin.org/headers"
    ADAPTERS = ['http://', 'https://']

    def __init__(self, host_domain, api_key, logger, debug=False):
        # Debug - if set to true will add more verbose loggin output, for a full trace of the HTTP trafic set debug to 'HTTP'
        self.host_domain = host_domain
        self.api_key = api_key
        self.debug = debug
        self.testing = True
        self.logger = logger
        self.default_adapter = None
        self.adapter = None
        self.api = self._init_api()
        self.threading_enabled = False

    def _init_api(self) -> requests.sessions.Session:
        # TODO: Make a proper requests Session
        session = requests.Session()
        session.auth = (self.api_key, 'password')
        self.default_adapter = self.ADAPTERS[1]
        self.adapter = session.get_adapter(self.default_adapter)
        if self.debug == 'HTTP':
            HTTPConnection.debuglevel = 1
            logging.basicConfig()  # you need to initialize logging, otherwise you will not see anything from requests
            logging.getLogger().setLevel(logging.DEBUG)
            self.logger.setLevel(logging.DEBUG)
            self.logger.propagate = True
        if self.debug:
            session.hooks['response'].append(self._hook_log_response_data)
        if self.testing:
            session.hooks['response'].append(self._hook_print_response_headers_links)

        return session

    def _test_connection(self) -> Union[list, None]:
        if not self.api:
            return False
        test_connection = self.api.request("GET", url=self.TEST_URL)
        prettified_response = pprint(test_connection.json())
        _logger.info(prettified_response)

    def enable_threading(self, connections: int) -> bool:
        self.threading_enabled = True
        self._switch_requests_pool_size(pool_conn=connections, poll_max=connections)
        return True

    def _switch_requests_pool_size(self, pool_conn: int = 10, poll_max: int = 10) -> None:
        adapter = request_adapters.HTTPAdapter(pool_connections=pool_conn, pool_maxsize=poll_max)
        self.api.mount(self.default_adapter, adapter)

    def _reset_adapter_to_default(self) -> None:
        adapter = request_adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10)
        self.api.mount(self.default_adapter, adapter)

    def get_api_pool_connections(self):
        return self.api.adapters[self.default_adapter]._pool_connections

    def send(self, endpoint, method='GET', data=None, headers=None):

        response = self._send(endpoint, method, data, headers)
        if isinstance(response, tuple): # Error
            return False
        return response

    def _send(self, endpoint, method='GET', data=None, headers=None):

        response_result = None
        headers = headers if headers else self.HEADER
        try:
            response = self.api.request(method, endpoint, data=data, headers=headers,  timeout=3)
            response.raise_for_status()

        except (ConnectionError, requests.exceptions.Timeout) as http__connection_error:
            if isinstance(http__connection_error, requests.exceptions.ConnectTimeout):
                msg = """The request timed out."""
            elif isinstance(http__connection_error, requests.exceptions.ConnectionError):
                msg =  """A Connection error occurred."""
            elif isinstance(http__connection_error, requests.exceptions.ReadTimeout):
                msg = """The server did not send any data in the allotted amount of time."""
            else:
                msg = "Connection Error"
            _logger.error(msg)
            _logger.error(f'Error -> {http__connection_error}')
            traceback.print_exc()
            response_result = 'error', http__connection_error

        except requests.exceptions.HTTPError as http_error:
            _logger.error(f"HTTP Error --> \n{http_error}")
            traceback.print_exc()
            response_result = 'error', http_error

        except requests.exceptions.RequestException as request_exception:
            _logger.error(f"Error encountered while requesting to cover manager --> \n{request_exception}")
            traceback.print_exc()
            response_result = 'error', request_exception

        else:
            response_result = self._get_json_handle(response)
        finally:
            return response_result

    # ====================================== < HOOKS > ====================================== #
    def _hook_log_response_data(self, response, *__, **___) -> None:
        data = self._get_json_handle(response)
        if not isinstance(data, tuple):
            self.logger.info(json.dumps(data, indent=4))

    def _hook_print_response_headers_links(self, response, *__, **___) -> None:
        """DEV"""
        print(f'Reponse Link -> {response.links}')

    # ====================================== < HANDLES > ====================================== #
    def _get_json_handle(self, response):
        try:
            data = response.json()
        except json.decoder.JSONDecodeError as json_error:
            _logger.error(f'Could not Read Object response from Cover Manager')
            _logger.error(f'Error -> {json_error}')
            traceback.print_exc()
            return 'error', json_error
        else:
            return data

    # ====================================== < ENDPOINTS > ====================================== #

    # ====================================== < UTILS > ====================================== #

    def get_content_type(self, filename: str) -> mimetypes:
        """Retrieve filename mimetype.

        :param filename: file name.
        :return: mimetype.
        """
        return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

    def encode_multipart_formdata(self, payload):
        boundary = binascii.hexlify(os.urandom(16)).decode('ascii')

        body = (
                "".join("--%s\r\n"
                        "Content-Disposition: form-data; name=\"%s\"\r\n"
                        "\r\n"
                        "%s\r\n" % (boundary, field, value)
                        for field, value in payload.items()) +
                "--%s--\r\n" % boundary
        )

        content_type = "multipart/form-data; boundary=%s" % boundary

        return body, content_type


if __name__ == '__main__':
    thread_test = False
    HOST_DOMAIN = "https://www.covermanager.com"
    API_KEY = "9Pxa1F9uqep38EbU2wcs"
    payload = {}
    headers = {}
    cover_manager = API(HOST_DOMAIN, API_KEY, _logger, debug=True)
    if thread_test:
        cover_manager_threaded = CoverManager(HOST_DOMAIN, API_KEY, _logger, debug=True)
        cover_manager_threaded.enable_threading(100)
        print(cover_manager.get_api_pool_connections())
        print(cover_manager_threaded.get_api_pool_connections())

    restaurants = cover_manager.restaurant_get_restaurant_list()

