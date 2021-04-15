try:
    import threading
    import logging
    import enum
    import json
    import time
    import requests
    from .token import Token
    from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
    from ...crm.api.util import APIHTTPConnector
    from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
    from ...crm.api.util.constants import Constants

except Exception as e:
    import threading
    import logging
    import enum
    import json
    import time
    import requests
    from .token import Token
    from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
    from ...crm.api.util import APIHTTPConnector
    from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
    from ...crm.api.util.constants import Constants


class OAuthToken(Token):
    """
    This class maintains the tokens and authenticates every request.
    """

    logger = logging.getLogger('SDKLogger')
    lock = threading.Lock()

    def __init__(self, client_id, client_secret, grant_token=None, refresh_token=None, redirect_url=None, id=None):

        """
        Creates an OAuthToken class instance with the specified parameters.

        Parameters:
            client_id (str) : A string containing the OAuth client id.
            client_secret (str) : A string containing the OAuth client secret.
            grant_token (str) : A string containing the GRANT token.
            refresh_token (str) : A string containing the REFRESH token.
            redirect_url (str) : A string containing the OAuth redirect URL. Default value is None
            id (str) : A string containing the Id. Default value is None
        """

        error = {}

        if not isinstance(client_id, str):
            error[Constants.FIELD] = Constants.CLIENT_ID
            error[Constants.EXPECTED_TYPE] = Constants.STRING
            error[Constants.CLASS] = OAuthToken.__name__
            raise SDKException(code=Constants.TOKEN_ERROR, details=error)

        if not isinstance(client_secret, str):
            error[Constants.FIELD] = Constants.CLIENT_SECRET
            error[Constants.EXPECTED_TYPE] = Constants.STRING
            error[Constants.CLASS] = OAuthToken.__name__
            raise SDKException(code=Constants.TOKEN_ERROR, details=error)

        if grant_token is None and refresh_token is None:
            error[Constants.FIELD] = Constants.TYPE
            error[Constants.EXPECTED_TYPE] = Constants.EXPECTED_TOKEN_TYPES
            error[Constants.CLASS] = OAuthToken.__name__
            raise SDKException(code=Constants.INPUT_ERROR, details=error)

        if grant_token is not None and not isinstance(grant_token, str):
            error[Constants.FIELD] = Constants.GRANT_TOKEN
            error[Constants.EXPECTED_TYPE] = Constants.STRING
            error[Constants.CLASS] = OAuthToken.__name__
            raise SDKException(code=Constants.TOKEN_ERROR, details=error)

        if refresh_token is not None and not isinstance(refresh_token, str):
            error[Constants.FIELD] = Constants.REFRESH_TOKEN
            error[Constants.EXPECTED_TYPE] = Constants.STRING
            error[Constants.CLASS] = OAuthToken.__name__
            raise SDKException(code=Constants.TOKEN_ERROR, details=error)

        if redirect_url is not None and not isinstance(redirect_url, str):
            error[Constants.FIELD] = Constants.REDIRECT_URI
            error[Constants.EXPECTED_TYPE] = Constants.STRING
            error[Constants.CLASS] = OAuthToken.__name__
            raise SDKException(code=Constants.TOKEN_ERROR, details=error)

        if id is not None and not isinstance(id, str):
            error[Constants.FIELD] = Constants.ID
            error[Constants.EXPECTED_TYPE] = Constants.STRING
            error[Constants.CLASS] = OAuthToken.__name__
            raise SDKException(code=Constants.TOKEN_ERROR, details=error)

        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__redirect_url = redirect_url
        self.__grant_token = grant_token
        self.__refresh_token = refresh_token
        self.__id = id
        self.__access_token = None
        self.__expires_in = None
        self.__user_mail = None

    def get_client_id(self):
        """
        This is a getter method to get __client_id.

        Returns:
            string: A string representing __client_id
        """

        return self.__client_id

    def get_client_secret(self):
        """
        This is a getter method to get __client_secret.

        Returns:
            string: A string representing __client_secret
        """

        return self.__client_secret

    def get_redirect_url(self):
        """
        This is a getter method to get __redirect_url.

        Returns:
            string: A string representing __redirect_url
        """

        return self.__redirect_url

    def get_grant_token(self):
        """
        This is a getter method to get __grant_token.

        Returns:
            string: A string representing __grant_token
        """
        return self.__grant_token

    def get_refresh_token(self):
        """
        This is a getter method to get __refresh_token.

        Returns:
            string: A string representing __refresh_token
        """

        return self.__refresh_token

    def get_access_token(self):
        """
        This is a getter method to get __access_token.

        Returns:
            string: A string representing __access_token
        """

        return self.__access_token

    def get_id(self):
        """
        This is a getter method to get __id.

        Returns:
            string: A string representing __id
        """

        return self.__id

    def get_expires_in(self):
        """
        This is a getter method to get __expires_in.

        Returns:
            string: A string representing __expires_in
        """

        return self.__expires_in

    def get_user_mail(self):
        """
        This is a getter method to get __user_mail.

        Returns:
            string: A string representing __user_mail
        """

        return self.__user_mail

    def set_refresh_token(self, refresh_token):
        """
        This is a setter method to set __refresh_token.

        """
        self.__refresh_token = refresh_token

    def set_access_token(self, access_token):
        """
        This is a setter method to set __access_token.

        """

        self.__access_token = access_token

    def set_id(self, id):
        """
        This is a setter method to set __id.

        """

        self.__id = id

    def set_expires_in(self, expires_in):
        """
        This is a setter method to set __expires_in.

        """

        self.__expires_in = expires_in

    def set_user_mail(self, user_mail):
        """
        This is a setter method to set __user_mail.

        """

        self.__user_mail = user_mail


    def authenticate(self, url_connection):
        with OAuthToken.lock:
            initializer = Initializer.get_initializer()
            store = initializer.store
            user = initializer.user

            if self.__id is not None:
                oauth_token = initializer.store.get_token_by_id(self.__id, self)
            else:
                oauth_token = initializer.store.get_token(user, self)

            if oauth_token is None:
                token = self.generate_access_token(user, store).get_access_token() if (
                            self.__refresh_token is None) else self.refresh_access_token(user, store).get_access_token()

            elif int(oauth_token.get_expires_in()) - int(time.time() * 1000) < 5000:
                OAuthToken.logger.info(Constants.REFRESH_TOKEN_MESSAGE)
                token = oauth_token.refresh_access_token(user, store).get_access_token()

            else:
                token = oauth_token.get_access_token()

            url_connection.add_header(Constants.AUTHORIZATION, Constants.OAUTH_HEADER_PREFIX + token)

    def refresh_access_token(self, user, store):
        try:
            url = Initializer.get_initializer().environment.accounts_url

            body = {
                Constants.REFRESH_TOKEN: self.__refresh_token,
                Constants.CLIENT_ID: self.__client_id,
                Constants.REDIRECT_URI: self.__redirect_url if self.__redirect_url is not None else None,
                Constants.CLIENT_SECRET: self.__client_secret,
                Constants.GRANT_TYPE: Constants.REFRESH_TOKEN
            }

            response = requests.post(url, data=body, params=None, headers=None, allow_redirects=False).json()
            self.parse_response(response)
            self.generate_id()
            store.save_token(user, self)

        except SDKException as ex:
            raise ex

        except Exception as ex:
            raise SDKException(code=Constants.SAVE_TOKEN_ERROR, cause=ex)

        return self

    def generate_access_token(self, user, store):
        try:
            url = Initializer.get_initializer().environment.accounts_url

            body = {
                Constants.GRANT_TYPE: Constants.GRANT_TYPE_AUTH_CODE,
                Constants.CLIENT_ID: self.__client_id,
                Constants.CLIENT_SECRET: self.__client_secret,
                Constants.REDIRECT_URI: self.__redirect_url if self.__redirect_url is not None else None,
                Constants.CODE: self.__grant_token
            }
            headers = dict()
            headers[Constants.USER_AGENT_KEY] = Constants.USER_AGENT
            response = requests.post(url, data=body, params=None, headers=headers, allow_redirects=True).json()
            self.parse_response(response)
            self.generate_id()
            store.save_token(user, self)

        except SDKException as ex:
            raise ex

        except Exception as ex:
            raise SDKException(code=Constants.SAVE_TOKEN_ERROR, cause=ex)

        return self

    def parse_response(self, response):
        response_json = dict(response)

        if Constants.ACCESS_TOKEN not in response_json:
            raise SDKException(code=Constants.INVALID_TOKEN_ERROR, message=str(response_json.get(Constants.ERROR_KEY))if Constants.ERROR_KEY in response_json else Constants.NO_ACCESS_TOKEN_ERROR)

        self.__access_token = response_json.get(Constants.ACCESS_TOKEN)
        self.__expires_in = str(int(time.time() * 1000) + self.get_token_expires_in(response=response_json))

        if Constants.REFRESH_TOKEN in response_json:
            self.__refresh_token = response_json.get(Constants.REFRESH_TOKEN)

        return self

    @staticmethod
    def get_token_expires_in(response):
        return int(response[Constants.EXPIRES_IN]) if Constants.EXPIRES_IN_SEC in response else int(
            response[Constants.EXPIRES_IN]) * 1000

    def generate_id(self):
        id = ""
        email = str(Initializer.get_initializer().user.get_email())
        environment = str(Initializer.get_initializer().environment.name)
        id += "python_" + email[0:email.find(Constants.AT)] + Constants.UNDERSCORE
        id += environment + Constants.UNDERSCORE + self.__refresh_token[len(self.__refresh_token)-4:]
        self.__id = id
        return self.__id

    def remove(self):
        try:
            Initializer.get_initializer().store.delete_token(self)
            return True
        except Exception:
            return False
