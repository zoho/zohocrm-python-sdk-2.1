
try:
    import os
    import csv
    from zcrmsdk.src.com.zoho.api.authenticator.store.token_store import TokenStore
    from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
    from ....crm.api.util.constants import Constants
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException

except Exception as e:
    import os
    import csv
    from .token_store import TokenStore
    from ..oauth_token import OAuthToken
    from ....crm.api.util.constants import Constants
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException


class FileStore(TokenStore):

    """
    The class to store user token details to the file.
    """

    def __init__(self, file_path):

        """
        Creates an FileStore class instance with the specified parameters.

        Parameters:
            file_path (str) : A string containing the absolute file path of the file to store tokens

        """

        self.file_path = file_path
        self.headers = [Constants.ID, Constants.USER_MAIL, Constants.CLIENT_ID, Constants.CLIENT_SECRET, Constants.REFRESH_TOKEN, Constants.ACCESS_TOKEN, Constants.GRANT_TOKEN, Constants.EXPIRY_TIME, Constants.REDIRECT_URI]

        if (os.path.exists(file_path) and os.stat(file_path).st_size == 0) or not os.path.exists(file_path):
            with open(self.file_path, mode='w') as token_file:
                csv_writer = csv.writer(token_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(self.headers)

    def get_token(self, user, token):
        try:
            if isinstance(token, OAuthToken):
                with open(self.file_path, mode='r') as f:
                    data = csv.reader(f, delimiter=',')
                    next(data, None)
                    for next_record in data:
                        if len(next_record) == 0:
                            continue
                        if self.check_token_exists(user.get_email(), token, next_record):
                            grant_token = next_record[6] if next_record[6] is not None and len(
                                next_record[6]) > 0 else None
                            redirect_url = next_record[8] if next_record[8] is not None and len(
                                next_record[8]) > 0 else None

                            oauthtoken = OAuthToken(client_id=next_record[2], client_secret=next_record[3],
                                                     grant_token=grant_token,
                                                     redirect_url=redirect_url, refresh_token=next_record[4])
                            oauthtoken.set_id(next_record[0])
                            oauthtoken.set_user_mail(next_record[1])
                            oauthtoken.set_expires_in(next_record[7])
                            oauthtoken.set_access_token(next_record[5])

                            return oauthtoken

        except IOError as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKEN_FILE_ERROR, cause=ex)

        return None

    def save_token(self, user, token):
        if isinstance(token, OAuthToken):
            token.set_user_mail(user.get_email())
            self.delete_token(token)

            try:
                with open(self.file_path, mode='a+') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow([token.get_id(), user.get_email(), token.get_client_id(), token.get_client_secret(), token.get_refresh_token(), token.get_access_token(), token.get_grant_token(), token.get_expires_in(), token.get_redirect_url()])

            except IOError as ex:
                raise SDKException(code=Constants.TOKEN_STORE, message=Constants.SAVE_TOKEN_FILE_ERROR, cause=ex)

    def delete_token(self, token):
        lines = list()

        if isinstance(token, OAuthToken):
            try:
                with open(self.file_path, mode='r') as f:
                    data = csv.reader(f, delimiter=',')
                    for next_record in data:
                        if len(next_record) == 0:
                            continue
                        lines.append(next_record)
                        if self.check_token_exists(token.get_user_mail(), token, next_record):
                            lines.remove(next_record)

                with open(self.file_path, mode='w') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerows(lines)

            except IOError as ex:
                raise SDKException(code=Constants.TOKEN_STORE, message=Constants.DELETE_TOKEN_FILE_ERROR, cause=ex)

    def get_tokens(self):
        tokens = []

        try:
            with open(self.file_path, mode='r') as f:
                data = csv.reader(f, delimiter=',')
                next(data, None)
                for next_record in data:
                    if len(next_record) == 0:
                        continue
                    grant_token = next_record[6] if next_record[6] is not None and len(
                        next_record[6]) > 0 else None

                    redirect_url = next_record[8] if next_record[8] is not None and len(
                        next_record[8]) > 0 else None

                    token = OAuthToken(client_id=next_record[2], client_secret=next_record[3], grant_token=grant_token, redirect_url=redirect_url, refresh_token=next_record[4])
                    token.set_id(next_record[0])
                    token.set_user_mail(next_record[1])
                    token.set_expires_in(next_record[7])
                    token.set_access_token(next_record[5])
                    tokens.append(token)

            return tokens
        except Exception as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKENS_FILE_ERROR, cause=ex)

    def delete_tokens(self):
        try:
            with open(self.file_path, mode='w') as token_file:
                csv_writer = csv.writer(token_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(self.headers)
        except Exception as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.DELETE_TOKENS_FILE_ERROR, cause=ex)

    def get_token_by_id(self, id, token):
        try:
            if isinstance(token, OAuthToken):
                is_row_present = False
                with open(self.file_path, mode='r') as f:
                    data = csv.reader(f, delimiter=',')
                    next(data, None)
                    for next_record in data:
                        if len(next_record) == 0:
                            continue

                        if next_record[0] == id:
                            is_row_present = True
                            grant_token = next_record[6] if next_record[6] is not None and len(
                                next_record[6]) > 0 else None
                            redirect_url = next_record[8] if next_record[8] is not None and len(
                                next_record[8]) > 0 else None

                            oauthtoken = OAuthToken(client_id=next_record[2], client_secret=next_record[3], grant_token=grant_token,
                                               redirect_url=redirect_url, refresh_token=next_record[4])
                            oauthtoken.set_id(next_record[0])
                            oauthtoken.set_user_mail(next_record[1])
                            oauthtoken.set_expires_in(next_record[7])
                            oauthtoken.set_access_token(next_record[5])

                            return oauthtoken
                    if not is_row_present:
                        raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKEN_BY_ID_FILE_ERROR)

        except IOError as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKEN_BY_ID_FILE_ERROR, cause=ex)

        return None

    @staticmethod
    def check_token_exists(email, token, row):
        if email is None:
            raise SDKException(Constants.USER_MAIL_NULL_ERROR, Constants.USER_MAIL_NULL_ERROR_MESSAGE)

        client_id = token.get_client_id()
        grant_token = token.get_grant_token()
        refresh_token = token.get_refresh_token()
        token_check = grant_token == row[6] if grant_token is not None else refresh_token == row[4]

        if row[1] == email and row[2] == client_id and token_check:
            return True

        return False
