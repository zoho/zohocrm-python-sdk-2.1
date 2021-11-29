try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.parameter_map import ParameterMap
	from zcrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Utility, Constants
	from zcrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..parameter_map import ParameterMap
	from ..util import APIResponse, CommonAPIHandler, Utility, Constants
	from ..param import Param


class ContactRolesOperations(object):
	def __init__(self):
		"""Creates an instance of ContactRolesOperations"""
		pass

	def get_contact_roles(self):
		"""
		The method to get contact roles

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/Contacts/roles'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def create_contact_roles(self, request):
		"""
		The method to create contact roles

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/Contacts/roles'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_contact_roles(self, request):
		"""
		The method to update contact roles

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/Contacts/roles'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_contact_roles(self, param_instance=None):
		"""
		The method to delete contact roles

		Parameters:
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/Contacts/roles'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_param(param_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_contact_role(self, id):
		"""
		The method to get contact role

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
		api_path = api_path + '/crm/v2.1/Contacts/roles/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_contact_role(self, id, request):
		"""
		The method to update contact role

		Parameters:
			id (int) : An int representing the id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/Contacts/roles/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_contact_role(self, id):
		"""
		The method to delete contact role

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
		api_path = api_path + '/crm/v2.1/Contacts/roles/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_all_contact_roles_of_deal(self, deal_id, param_instance=None):
		"""
		The method to get all contact roles of deal

		Parameters:
			deal_id (int) : An int representing the deal_id
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(deal_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal_id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/Deals/'
		api_path = api_path + str(deal_id)
		api_path = api_path + '/Contact_Roles'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_module_api_name("Contacts")
		Utility.get_fields("Contacts", handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.record_response_handler import RecordResponseHandler
		except Exception:
			from .record_response_handler import RecordResponseHandler
		return handler_instance.api_call(RecordResponseHandler.__module__, 'application/json')

	def get_contact_role_of_deal(self, contact_id, deal_id):
		"""
		The method to get contact role of deal

		Parameters:
			contact_id (int) : An int representing the contact_id
			deal_id (int) : An int representing the deal_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(contact_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(deal_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/Deals/'
		api_path = api_path + str(deal_id)
		api_path = api_path + '/Contact_Roles/'
		api_path = api_path + str(contact_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_module_api_name("Contacts")
		Utility.get_fields("Contacts", handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.record_response_handler import RecordResponseHandler
		except Exception:
			from .record_response_handler import RecordResponseHandler
		return handler_instance.api_call(RecordResponseHandler.__module__, 'application/json')

	def add_contact_role_to_deal(self, contact_id, deal_id, request):
		"""
		The method to add contact role to deal

		Parameters:
			contact_id (int) : An int representing the contact_id
			deal_id (int) : An int representing the deal_id
			request (RecordBodyWrapper) : An instance of RecordBodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.record_body_wrapper import RecordBodyWrapper
		except Exception:
			from .record_body_wrapper import RecordBodyWrapper

		if not isinstance(contact_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(deal_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, RecordBodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: RecordBodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/Deals/'
		api_path = api_path + str(deal_id)
		api_path = api_path + '/Contact_Roles/'
		api_path = api_path + str(contact_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.record_action_handler import RecordActionHandler
		except Exception:
			from .record_action_handler import RecordActionHandler
		return handler_instance.api_call(RecordActionHandler.__module__, 'application/json')

	def remove_contact_role_from_deal(self, contact_id, deal_id):
		"""
		The method to remove contact role from deal

		Parameters:
			contact_id (int) : An int representing the contact_id
			deal_id (int) : An int representing the deal_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(contact_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(deal_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/Deals/'
		api_path = api_path + str(deal_id)
		api_path = api_path + '/Contact_Roles/'
		api_path = api_path + str(contact_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		try:
			from zcrmsdk.src.com.zoho.crm.api.contact_roles.record_action_handler import RecordActionHandler
		except Exception:
			from .record_action_handler import RecordActionHandler
		return handler_instance.api_call(RecordActionHandler.__module__, 'application/json')


class DeleteContactRolesParam(object):
	ids = Param('ids', 'com.zoho.crm.api.ContactRoles.DeleteContactRolesParam')


class GetAllContactRolesOfDealParam(object):
	ids = Param('ids', 'com.zoho.crm.api.ContactRoles.GetAllContactRolesOfDealParam')
