try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants


class CancelMeetingsOperations(object):
	def __init__(self, event_id):
		"""
		Creates an instance of CancelMeetingsOperations with the given parameters

		Parameters:
			event_id (int) : An int representing the event_id
		"""

		if not isinstance(event_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: event_id EXPECTED TYPE: int', None, None)
		
		self.__event_id = event_id


	def cancel_meetings(self, request):
		"""
		The method to cancel meetings

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.cancel_meetings.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2.1/Events/'
		api_path = api_path + str(self.__event_id)
		api_path = api_path + '/actions/cancel'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		try:
			from zcrmsdk.src.com.zoho.crm.api.cancel_meetings.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')
