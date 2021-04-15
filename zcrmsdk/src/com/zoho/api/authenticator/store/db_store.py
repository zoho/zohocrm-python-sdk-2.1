
try:
    import mysql.connector
    from mysql.connector import Error
    from zcrmsdk.src.com.zoho.api.authenticator.store.token_store import TokenStore
    from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
    from zcrmsdk.src.com.zoho.crm.api.util.constants import Constants
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException

except Exception as e:
    import mysql.connector
    from mysql.connector import Error
    from .token_store import TokenStore
    from ..oauth_token import OAuthToken
    from ....crm.api.util.constants import Constants
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException


class DBStore(TokenStore):

    """
    This class to store user token details to the MySQL DataBase.
    """

    def __init__(self, host=Constants.MYSQL_HOST, database_name=Constants.MYSQL_DATABASE_NAME,
                 user_name=Constants.MYSQL_USER_NAME, password="", port_number=Constants.MYSQL_PORT_NUMBER,
                 table_name=Constants.MYSQL_TABLE_NAME):

        """
        Creates a DBStore class instance with the specified parameters.

        Parameters:
            host (str) : A string containing the DataBase host name. Default value is localhost
            database_name (str) : A string containing the DataBase name. Default value is zohooauth
            user_name (str) : A string containing the DataBase user name. Default value is root
            password (str) : A string containing the DataBase password. Default value is an empty string
            port_number (str) : A string containing the DataBase port number. Default value is 3306
        """

        self.__host = host
        self.__database_name = database_name
        self.__user_name = user_name
        self.__password = password
        self.__port_number = port_number
        self.__table_name = table_name

    def get_host(self):
        """
        This is a getter method to get __host.

        Returns:
            string: A string representing __host
        """

        return self.__host

    def get_database_name(self):
        """
        This is a getter method to get __database_name.

        Returns:
            string: A string representing __database_name
        """

        return self.__database_name

    def get_user_name(self):
        """
        This is a getter method to get __user_name.

        Returns:
            string: A string representing __user_name
        """

        return self.__user_name

    def get_password(self):
        """
        This is a getter method to get __password.

        Returns:
            string: A string representing __password
        """
        return self.__password

    def get_port_number(self):
        """
        This is a getter method to get __port_number.

        Returns:
            string: A string representing __port_number
        """

        return self.__port_number

    def get_table_name(self):
        """
        This is a getter method to get __table_name.

        Returns:
            string: A string representing __table_name
        """

        return self.__table_name

    def get_token(self, user, token):
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)
            try:
                if isinstance(token, OAuthToken):
                    cursor = connection.cursor()
                    query = self.construct_dbquery(user.get_email(), token, False)
                    cursor.execute(query)
                    result = cursor.fetchone()

                    if result is not None:
                        oauthtoken = OAuthToken(client_id=result[2], client_secret=result[3], grant_token=result[6],
                                                 refresh_token=result[4], redirect_url=result[8])
                        oauthtoken.set_id(result[0])
                        oauthtoken.set_access_token(result[5])
                        oauthtoken.set_expires_in(str(result[7]))
                        oauthtoken.set_user_mail(result[1])
                        return oauthtoken

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKEN_DB_ERROR, cause=ex)

    def save_token(self, user, token):
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)

            try:
                if isinstance(token, OAuthToken):
                    token.set_user_mail(user.get_email())
                    self.delete_token(token)
                    cursor = connection.cursor()
                    query = "insert into "+self.__table_name+" (id,user_mail,client_id,client_secret,refresh_token,access_token,grant_token,expiry_time,redirect_url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                    val = (token.get_id(), user.get_email(), token.get_client_id(), token.get_client_secret(), token.get_refresh_token(), token.get_access_token(), token.get_grant_token(), token.get_expires_in(), token.get_redirect_url())
                    cursor.execute(query, val)
                    connection.commit()

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.SAVE_TOKEN_DB_ERROR, cause=ex)

    def delete_token(self, token):
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)

            try:
                if isinstance(token, OAuthToken):
                    cursor = connection.cursor()
                    query = self.construct_dbquery(token.get_user_mail(), token, True)
                    cursor.execute(query)
                    connection.commit()

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.DELETE_TOKEN_DB_ERROR, cause=ex)

    def get_tokens(self):
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)
            tokens = []

            try:
                cursor = connection.cursor()
                query = 'select * from ' + self.__table_name + ";"
                cursor.execute(query)
                results = cursor.fetchall()

                for result in results:

                    token = OAuthToken(client_id=result[2], client_secret=result[3], grant_token=result[6], refresh_token=result[4], redirect_url=result[8])
                    token.set_id(result[0])
                    token.set_expires_in(str(result[7]))
                    token.set_user_mail(result[1])
                    token.set_access_token(result[5])
                    tokens.append(token)

                return tokens

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(Constants.TOKEN_STORE, Constants.GET_TOKENS_DB_ERROR, None, ex)

    def delete_tokens(self):
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)

            try:
                cursor = connection.cursor()
                query = 'delete from ' + self.__table_name + ";"
                cursor.execute(query)
                connection.commit()

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None
        except Error as ex:
            raise SDKException(Constants.TOKEN_STORE, Constants.DELETE_TOKENS_DB_ERROR, Exception=ex)

    def get_token_by_id(self, id, token):
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)
            try:
                if isinstance(token, OAuthToken):

                    query = "select * from " + self.__table_name + " where id='" + id + "'"
                    cursor = connection.cursor()
                    cursor.execute(query)
                    results = cursor.fetchall()

                    for result in results:
                        if result[0] == id:

                            oauthtoken = OAuthToken(client_id=result[2], client_secret=result[3], grant_token=result[6], refresh_token=result[4], redirect_url=result[8])
                            oauthtoken.set_id(result[0])
                            oauthtoken.set_access_token(result[5])
                            oauthtoken.set_expires_in(str(result[7]))
                            oauthtoken.set_user_mail(result[1])
                            return oauthtoken

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKEN_BY_ID_DB_ERROR, cause=ex)

    def construct_dbquery(self, email, token, is_delete):
        if email is None:
            raise SDKException(Constants.USER_MAIL_NULL_ERROR, Constants.USER_MAIL_NULL_ERROR_MESSAGE)

        query = "delete from " if is_delete is True else "select * from "
        query += self.__table_name + " where user_mail ='" + email + "' and client_id='" + token.get_client_id() + "' and "

        if token.get_grant_token() is not None:
            query += "grant_token='" + token.get_grant_token() + "'"

        else:
            query += "refresh_token='" + token.get_refresh_token() + "'"

        return query
