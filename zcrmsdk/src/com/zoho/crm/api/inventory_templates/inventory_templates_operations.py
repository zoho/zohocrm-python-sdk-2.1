try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.parameter_map import ParameterMap
	from zcrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zcrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..parameter_map import ParameterMap
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class InventoryTemplatesOperations(object):
	def __init__(self, sort_by=None, sort_order=None, category=None):
		"""
		Creates an instance of InventoryTemplatesOperations with the given parameters

		Parameters:
			sort_by (string) : A string representing the sort_by
			sort_order (string) : A string representing the sort_order
			category (string) : A string representing the category
		"""

		if sort_by is not None and not isinstance(sort_by, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sort_by EXPECTED TYPE: str', None, None)
		
		if sort_order is not None and not isinstance(sort_order, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sort_order EXPECTED TYPE: str', None, None)
		
		if category is not None and not isinstance(category, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: category EXPECTED TYPE: str', None, None)
		
		self.__sort_by = sort_by
		self.__sort_order = sort_order
		self.__category = category


	def get_inventory_templates(self, param_instance=None):
		"""
		The method to get inventory templates

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
		api_path = api_path + '/crm/v2.1/settings/inventory_templates'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('sort_by', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatesParam'), self.__sort_by)
		handler_instance.add_param(Param('sort_order', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatesParam'), self.__sort_order)
		handler_instance.add_param(Param('category', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatesParam'), self.__category)
		handler_instance.set_param(param_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.inventory_templates.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_inventory_template_by_id(self, id):
		"""
		The method to get inventory template by id

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
		api_path = api_path + '/crm/v2.1/settings/inventory_templates/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('sort_by', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatebyIDParam'), self.__sort_by)
		handler_instance.add_param(Param('sort_order', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatebyIDParam'), self.__sort_order)
		handler_instance.add_param(Param('category', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatebyIDParam'), self.__category)
		try:
			from zcrmsdk.src.com.zoho.crm.api.inventory_templates.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetInventoryTemplatesParam(object):
	module = Param('module', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatesParam')


class GetInventoryTemplatebyIDParam(object):
	pass
