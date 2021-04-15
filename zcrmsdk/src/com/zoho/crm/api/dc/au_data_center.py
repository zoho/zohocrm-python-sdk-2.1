try:
    from zcrmsdk.src.com.zoho.crm.api.dc.data_center import DataCenter
except Exception as e:
    from .data_center import DataCenter


class AUDataCenter(DataCenter):

    """
    This class represents the properties of Zoho CRM in AU Domain.
    """

    @classmethod
    def PRODUCTION(cls):

        """
        This method represents the Zoho CRM Production environment in AU domain
        :return: A Environment class instance.
        """

        return DataCenter.Environment("https://www.zohoapis.com.au", cls().get_iam_url(), cls().get_file_upload_url(), "au_prd")

    @classmethod
    def SANDBOX(cls):

        """
        This method represents the Zoho CRM Sandbox environment in AU domain
        :return: A Environment class instance.
        """

        return DataCenter.Environment("https://sandbox.zohoapis.com.au", cls(). get_iam_url(), cls().get_file_upload_url(), "au_sdb")

    @classmethod
    def DEVELOPER(cls):

        """
        This method represents the Zoho CRM Developer environment in AU domain
        :return: A Environment class instance.
        """

        return DataCenter.Environment("https://developer.zohoapis.com.au", cls(). get_iam_url(), cls().get_file_upload_url(), "au_dev")

    def get_iam_url(self):
        return "https://accounts.zoho.com.au/oauth/v2/token"

    def get_file_upload_url(self):
        return "https://content.zohoapis.com.au"
