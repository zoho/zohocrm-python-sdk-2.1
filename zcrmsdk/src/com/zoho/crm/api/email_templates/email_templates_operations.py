try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zcrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class EmailTemplatesOperations(object):
	def __init__(self, module=None):
		"""
		Creates an instance of EmailTemplatesOperations with the given parameters

		Parameters:
			module (string) : A string representing the module
		"""

		if module is not None and not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__module = module


	def get_email_templates(self):
		"""
		The method to get email templates

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/settings/email_templates'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.EmailTemplates.GetEmailTemplatesParam'), self.__module)
		try:
			from zcrmsdk.src.com.zoho.crm.api.email_templates.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_email_template_by_id(self, id):
		"""
		The method to get email template by id

		Parameters:
			id (int) : An int representing the id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/settings/email_templates/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.EmailTemplates.GetEmailTemplatebyIDParam'), self.__module)
		try:
			from zcrmsdk.src.com.zoho.crm.api.email_templates.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetEmailTemplatesParam(object):
	pass


class GetEmailTemplatebyIDParam(object):
	pass
