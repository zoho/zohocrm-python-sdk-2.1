try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.parameter_map import ParameterMap
	from zcrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Utility, Constants
	from zcrmsdk.src.com.zoho.crm.api.param import Param
	from zcrmsdk.src.com.zoho.crm.api.header import Header
	from zcrmsdk.src.com.zoho.crm.api.header_map import HeaderMap
except Exception:
	from ..exception import SDKException
	from ..parameter_map import ParameterMap
	from ..util import APIResponse, CommonAPIHandler, Utility, Constants
	from ..param import Param
	from ..header import Header
	from ..header_map import HeaderMap


class RelatedRecordsOperations(object):
	def __init__(self, related_list_api_name, module_api_name, x_external=None):
		"""
		Creates an instance of RelatedRecordsOperations with the given parameters

		Parameters:
			related_list_api_name (string) : A string representing the related_list_api_name
			module_api_name (string) : A string representing the module_api_name
			x_external (string) : A string representing the x_external
		"""

		if not isinstance(related_list_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_list_api_name EXPECTED TYPE: str', None, None)
		
		if not isinstance(module_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_api_name EXPECTED TYPE: str', None, None)
		
		if x_external is not None and not isinstance(x_external, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: x_external EXPECTED TYPE: str', None, None)
		
		self.__related_list_api_name = related_list_api_name
		self.__module_api_name = module_api_name
		self.__x_external = x_external


	def get_related_records(self, record_id, param_instance=None, header_instance=None):
		"""
		The method to get related records

		Parameters:
			record_id (int) : An int representing the record_id
			param_instance (ParameterMap) : An instance of ParameterMap
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsHeader'), self.__x_external)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_related_records(self, record_id, request):
		"""
		The method to update related records

		Parameters:
			record_id (int) : An int representing the record_id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.UpdateRelatedRecordsHeader'), self.__x_external)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delink_records(self, record_id, param_instance=None):
		"""
		The method to delink records

		Parameters:
			record_id (int) : An int representing the record_id
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.DelinkRecordsHeader'), self.__x_external)
		handler_instance.set_param(param_instance)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_related_records_using_external_id(self, external_value, param_instance=None, header_instance=None):
		"""
		The method to get related records using external id

		Parameters:
			external_value (string) : A string representing the external_value
			param_instance (ParameterMap) : An instance of ParameterMap
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsUsingExternalIDHeader'), self.__x_external)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_related_records_using_external_id(self, external_value, request):
		"""
		The method to update related records using external id

		Parameters:
			external_value (string) : A string representing the external_value
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.UpdateRelatedRecordsUsingExternalIDHeader'), self.__x_external)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_related_records_using_external_id(self, external_value, param_instance=None):
		"""
		The method to delete related records using external id

		Parameters:
			external_value (string) : A string representing the external_value
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.DeleteRelatedRecordsUsingExternalIDHeader'), self.__x_external)
		handler_instance.set_param(param_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_related_record(self, related_record_id, record_id, header_instance=None):
		"""
		The method to get related record

		Parameters:
			related_record_id (int) : An int representing the related_record_id
			record_id (int) : An int representing the record_id
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(related_record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(related_record_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordHeader'), self.__x_external)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_related_record(self, related_record_id, record_id, request):
		"""
		The method to update related record

		Parameters:
			related_record_id (int) : An int representing the related_record_id
			record_id (int) : An int representing the record_id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(related_record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(related_record_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.UpdateRelatedRecordHeader'), self.__x_external)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delink_record(self, related_record_id, record_id):
		"""
		The method to delink record

		Parameters:
			related_record_id (int) : An int representing the related_record_id
			record_id (int) : An int representing the record_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(related_record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(related_record_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.DelinkRecordHeader'), self.__x_external)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_related_record_using_external_id(self, external_field_value, external_value, header_instance=None):
		"""
		The method to get related record using external id

		Parameters:
			external_field_value (string) : A string representing the external_field_value
			external_value (string) : A string representing the external_value
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(external_field_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_field_value EXPECTED TYPE: str', None, None)
		
		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_field_value)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordUsingExternalIDHeader'), self.__x_external)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_related_record_using_external_id(self, external_field_value, external_value, request):
		"""
		The method to update related record using external id

		Parameters:
			external_field_value (string) : A string representing the external_field_value
			external_value (string) : A string representing the external_value
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(external_field_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_field_value EXPECTED TYPE: str', None, None)
		
		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_field_value)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.UpdateRelatedRecordUsingExternalIDHeader'), self.__x_external)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_related_record_using_external_id(self, external_field_value, external_value):
		"""
		The method to delete related record using external id

		Parameters:
			external_field_value (string) : A string representing the external_field_value
			external_value (string) : A string representing the external_value

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(external_field_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_field_value EXPECTED TYPE: str', None, None)
		
		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_field_value)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.add_header(Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.DeleteRelatedRecordUsingExternalIDHeader'), self.__x_external)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class GetRelatedRecordsHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsHeader')


class GetRelatedRecordsParam(object):
	page = Param('page', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsParam')
	per_page = Param('per_page', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsParam')


class UpdateRelatedRecordsHeader(object):
	pass


class DelinkRecordsHeader(object):
	pass


class DelinkRecordsParam(object):
	ids = Param('ids', 'com.zoho.crm.api.RelatedRecords.DelinkRecordsParam')


class GetRelatedRecordsUsingExternalIDHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsUsingExternalIDHeader')


class GetRelatedRecordsUsingExternalIDParam(object):
	page = Param('page', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsUsingExternalIDParam')
	per_page = Param('per_page', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsUsingExternalIDParam')


class UpdateRelatedRecordsUsingExternalIDHeader(object):
	pass


class DeleteRelatedRecordsUsingExternalIDHeader(object):
	pass


class DeleteRelatedRecordsUsingExternalIDParam(object):
	ids = Param('ids', 'com.zoho.crm.api.RelatedRecords.DeleteRelatedRecordsUsingExternalIDParam')


class GetRelatedRecordHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordHeader')


class UpdateRelatedRecordHeader(object):
	pass


class DelinkRecordHeader(object):
	pass


class GetRelatedRecordUsingExternalIDHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordUsingExternalIDHeader')


class UpdateRelatedRecordUsingExternalIDHeader(object):
	pass


class DeleteRelatedRecordUsingExternalIDHeader(object):
	pass
