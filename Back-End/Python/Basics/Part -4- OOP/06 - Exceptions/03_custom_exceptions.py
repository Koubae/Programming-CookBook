class TimeoutError(Exception):
    """Timeout exception"""


try:
    raise TimeoutError('timeout occurred')
except TimeoutError as ex:
    print(ex)
# timeout occurred


class ReadOnlyError(AttributeError):
    """Indicates an attribute is read-only"""


try:
    raise ReadOnlyError('Account number is read-only', 'BA10001')
except ReadOnlyError as ex:
    print(repr(ex))
# ReadOnlyError('Account number is read-only', 'BA10001')


class WebScraperException(Exception):
    """Base exception for WebScraper"""


class HTTPException(WebScraperException):
    """General HTTP exception for WebScraper"""
    
class InvalidUrlException(HTTPException):
    """Indicates the url is invalid (dns lookup fails)"""
    
class TimeoutException(HTTPException):
    """Indicates a general timeout exception in http connectivity"""
    
class PingTimeoutException(TimeoutException):
    """Ping time out"""
    
class LoadTimeoutException(TimeoutException):
    """Page load time out"""
    
class ParserException(WebScraperException):
    """General page parsing exception"""

# WebScraperException
#    - HTTPException
#        - InvalidUrlException
#        - TimeoutException
#            - PingTimeoutException
#            - LoadTimeoutException
#     - ParserException

try:
    raise PingTimeoutException('Ping to www.... timed out')
except HTTPException as ex:
    print(repr(ex))
# PingTimeoutException('Ping to www.... timed out',)

try:
    raise PingTimeoutException('Ping time out')
except WebScraperException as ex:
    print(repr(ex))
# PingTimeoutException('Ping time out',)


class APIException(Exception):
    """Base API exception"""


class ApplicationException(APIException):
    """Indicates an application error (not user caused) - 5xx HTTP type errors"""
    
class DBException(ApplicationException):
    """General database exception"""
    
class DBConnectionError(DBException):
    """Indicates an error connecting to database"""
    
class ClientException(APIException):
    """Indicates exception that was caused by user, not an internal error"""
    
class NotFoundError(ClientException):
    """Indicates resource was not found"""

class NotAuthorizedError(ClientException):
    """User is not authorized to perform requested action on resource"""
    
    
class Account:
    def __init__(self, account_id, account_type):
        self.account_id = account_id
        self.account_type = account_type

# APIException
#    - ApplicationException (5xx errors)
#        - DBException
#            - DBConnectionError
#    - ClientException
#        - NotFoundError
#        - NotAuthorizedError

def lookup_account_by_id(account_id):
    # mock of various exceptions that could be raised getting an account from database
    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientException(f'Account number {account_id} is invalid.')
        
    if account_id < 100:
        raise DBConnectionError('Permanent failure connecting to database.')
    elif account_id < 200:
        raise NotAuthorizedError('User does not have permissions to read this account')
    elif account_id < 300:
        raise NotFoundError(f'Account not found.')
    else:
        return Account(account_id, 'Savings')

from http import HTTPStatus

def get_account(account_id):
    try:
        account = lookup_account_by_id(account_id)
    except ApplicationException as ex:
        return HTTPStatus.INTERNAL_SERVER_ERROR, str(ex)
    except NotFoundError as ex:
        return HTTPStatus.NOT_FOUND, 'The account {} does not exist.'.format(account_id)
    except NotAuthorizedError as ex:
        return HTTPStatus.UNAUTHORIZED, 'You do not have the proper authorization.'
    except ClientException as ex:
        return HTTPStatus.BAD_REQUEST, str(ex)
    else:
        return HTTPStatus.OK, {"id": account.account_id, "type": account.account_type}

get_account('abc')
# (<HTTPStatus.BAD_REQUEST: 400>, 'Account number abc is invalid.')

get_account(50)
# (<HTTPStatus.INTERNAL_SERVER_ERROR: 500>,
#  'Permanent failure connecting to database.')

get_account(150)
# (<HTTPStatus.UNAUTHORIZED: 401>, 'You do not have the proper authorization.')

get_account(250)
# (<HTTPStatus.NOT_FOUND: 404>, 'The account 250 does not exist.')
get_account(350)
# (<HTTPStatus.OK: 200>, {'id': 350, 'type': 'Savings'})

class APIException(Exception):
    """Base API exception"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred.'
    user_err_msg = "We are sorry. An unexpected error occurred on our end."


class APIException(Exception):
    """Base API exception"""
    
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred.'
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
    def __init__(self, *args, user_err_msg = None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)
            
        if user_err_msg is not None:
            self.user_err_msg = user_err_msg

try:
    raise APIException()
except APIException as ex:
    print(repr(ex))
    print(ex.user_err_msg)
# APIException('API exception occurred.',)

try:
    raise APIException('custom message...', 10, 20)
except APIException as ex:
    print(repr(ex))
# APIException('custom message...', 10, 20)

try:
    raise APIException('custom message...', 10, 20, user_err_msg='custom user message')
except APIException as ex:
    print(repr(ex))
    print(ex.user_err_msg)
# APIException('custom message...', 10, 20)

import json

class APIException(Exception):
    """Base API exception"""
    
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred.'
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
    def __init__(self, *args, user_err_msg = None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)
            
        if user_err_msg is not None:
            self.user_err_msg = user_err_msg
            
    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object)

try:
    raise APIException()
except APIException as ex:
    print(repr(ex), ex.to_json())
# APIException('API exception occurred.',) {"status": 500, "message": "We are sorry. An unexpected error occurred on our end."}

from datetime import datetime

class APIException(Exception):
    """Base API exception"""
    
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred.'
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
    def __init__(self, *args, user_err_msg = None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)
            
        if user_err_msg is not None:
            self.user_err_msg = user_err_msg
    
    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object)
    
    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "http_status": self.http_status,
            "message": self.args[0] if self.args else self.internal_err_msg,
            "args": self.args[1:]
        }
        print(f'EXCEPTION: {datetime.utcnow().isoformat()}: {exception}')

try:
    raise APIException()
except APIException as ex:
    ex.log_exception()
    print(ex.to_json())
# EXCEPTION: 2019-08-09T23:53:42.088051: {'type': 'APIException', 'http_status': <HTTPStatus.INTERNAL_SERVER_ERROR: 500>, 'message': 'API exception occurred.', 'args': ()}
# {"status": 500, "message": "We are sorry. An unexpected error occurred on our end."}

class ApplicationException(APIException):
    """Indicates an application error (not user caused) - 5xx HTTP type errors"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = "Generic server side exception."
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
class DBException(ApplicationException):
    """General database exception"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = "Database exception."
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
class DBConnectionError(DBException):
    """Indicates an error connecting to database"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = "DB connection error."
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
class ClientException(APIException):
    """Indicates exception that was caused by user, not an internal error"""
    http_status = HTTPStatus.BAD_REQUEST
    internal_err_msg = "Client submitted bad request."
    user_err_msg = "A bad request was received."
    
class NotFoundError(ClientException):
    """Indicates resource was not found"""
    http_status = HTTPStatus.NOT_FOUND
    internal_err_msg = "Resource was not found."
    user_err_msg = "Requested resource was not found."

class NotAuthorizedError(ClientException):
    """User is not authorized to perform requested action on resource"""
    http_status = HTTPStatus.UNAUTHORIZED
    internal_err_msg = "Client not authorized to perform operation."
    user_err_msg = "You are not authorized to perform this request."

def lookup_account_by_id(account_id):
    # mock of various exceptions that could be raised getting an account from database
    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientException(f'Account number {account_id} is invalid.', 
                              f'account_id = {account_id}',
                              'type error - account number not an integer')
        
    if account_id < 100:
        raise DBConnectionError('Permanent failure connecting to database.', 'db=db01')
    elif account_id < 200:
        raise NotAuthorizedError('User does not have permissions to read this account', f'account_id={account_id}')
    elif account_id < 300:
        raise NotFoundError(f'Account not found.', f'account_id={account_id}')
    else:
        return Account(account_id, 'Savings')

def get_account(account_id):
    try:
        account = lookup_account_by_id(account_id)
    except APIException as ex:
        ex.log_exception()
        return ex.to_json()
    else:
        return HTTPStatus.OK, {"id": account.account_id, "type": account.account_type}
# get_account('ABC')
# EXCEPTION: 2019-08-09T23:53:43.380819: {'type': 'ClientException', 'http_status': <HTTPStatus.BAD_REQUEST: 400>, 'message': 'Account number ABC is invalid.', 'args': ('account_id = ABC', 'type error - account number not an integer')}
# '{"status": 400, "message": "A bad request was received."}'

get_account(50)
# EXCEPTION: 2019-08-09T23:53:43.569481: {'type': 'DBConnectionError', 'http_status': <HTTPStatus.INTERNAL_SERVER_ERROR: 500>, 'message': 'Permanent failure connecting to database.', 'args': ('db=db01',)}
# '{"status": 500, "message": "We are sorry. An unexpected error occurred on our end."}'

get_account(150)
# EXCEPTION: 2019-08-09T23:53:43.738034: {'type': 'NotAuthorizedError', 'http_status': <HTTPStatus.UNAUTHORIZED: 401>, 'message': 'User does not have permissions to read this account', 'args': ('account_id=150',)}
# '{"status": 401, "message": "You are not authorized to perform this request."}'

get_account(250)
# EXCEPTION: 2019-08-09T23:53:43.934897: {'type': 'NotFoundError', 'http_status': <HTTPStatus.NOT_FOUND: 404>, 'message': 'Account not found.', 'args': ('account_id=250',)}
# '{"status": 404, "message": "Requested resource was not found."}'
get_account(350)
# (<HTTPStatus.OK: 200>, {'id': 350, 'type': 'Savings'})