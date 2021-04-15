try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zcrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class PipelineOperations(object):
	def __init__(self, layout_id=None):
		"""
		Creates an instance of PipelineOperations with the given parameters

		Parameters:
			layout_id (int) : An int representing the layout_id
		"""

		if layout_id is not None and not isinstance(layout_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layout_id EXPECTED TYPE: int', None, None)
		
		self.__layout_id = layout_id


	def transfer_and_delete(self, request):
		"""
		The method to transfer and delete

		Parameters:
			request (TransferAndDeleteWrapper) : An instance of TransferAndDeleteWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.transfer_and_delete_wrapper import TransferAndDeleteWrapper
		except Exception:
			from .transfer_and_delete_wrapper import TransferAndDeleteWrapper

		if request is not None and not isinstance(request, TransferAndDeleteWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: TransferAndDeleteWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/settings/pipeline/actions/transfer'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.TransferAndDeleteParam'), self.__layout_id)
		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.transfer_action_handler import TransferActionHandler
		except Exception:
			from .transfer_action_handler import TransferActionHandler
		return handler_instance.api_call(TransferActionHandler.__module__, 'application/json')

	def get_pipelines(self):
		"""
		The method to get pipelines

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/settings/pipeline'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.GetPipelinesParam'), self.__layout_id)
		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def create_pipelines(self, request):
		"""
		The method to create pipelines

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/settings/pipeline'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.CreatePipelinesParam'), self.__layout_id)
		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_pipelines(self, request):
		"""
		The method to update pipelines

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/settings/pipeline'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.UpdatePipelinesParam'), self.__layout_id)
		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_pipeline(self, pipeline_id):
		"""
		The method to get pipeline

		Parameters:
			pipeline_id (int) : An int representing the pipeline_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(pipeline_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pipeline_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/settings/pipeline/'
		api_path = api_path + str(pipeline_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.GetPipelineParam'), self.__layout_id)
		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_pipeline(self, pipeline_id, request):
		"""
		The method to update pipeline

		Parameters:
			pipeline_id (int) : An int representing the pipeline_id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(pipeline_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pipeline_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/settings/pipeline/'
		api_path = api_path + str(pipeline_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.UpdatePipelineParam'), self.__layout_id)
		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class TransferAndDeleteParam(object):
	pass


class GetPipelinesParam(object):
	pass


class CreatePipelinesParam(object):
	pass


class UpdatePipelinesParam(object):
	pass


class GetPipelineParam(object):
	pass


class UpdatePipelineParam(object):
	pass
