try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ValidationError(object):
	def __init__(self):
		"""Creates an instance of ValidationError"""

		self.__api_name = None
		self.__info_message = None
		self.__message = None
		self.__index = None
		self.__parent_api_name = None
		self.__key_modified = dict()

	def get_api_name(self):
		"""
		The method to get the api_name

		Returns:
			string: A string representing the api_name
		"""

		return self.__api_name

	def set_api_name(self, api_name):
		"""
		The method to set the value to api_name

		Parameters:
			api_name (string) : A string representing the api_name
		"""

		if api_name is not None and not isinstance(api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_name EXPECTED TYPE: str', None, None)
		
		self.__api_name = api_name
		self.__key_modified['api_name'] = 1

	def get_info_message(self):
		"""
		The method to get the info_message

		Returns:
			string: A string representing the info_message
		"""

		return self.__info_message

	def set_info_message(self, info_message):
		"""
		The method to set the value to info_message

		Parameters:
			info_message (string) : A string representing the info_message
		"""

		if info_message is not None and not isinstance(info_message, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: info_message EXPECTED TYPE: str', None, None)
		
		self.__info_message = info_message
		self.__key_modified['info_message'] = 1

	def get_message(self):
		"""
		The method to get the message

		Returns:
			string: A string representing the message
		"""

		return self.__message

	def set_message(self, message):
		"""
		The method to set the value to message

		Parameters:
			message (string) : A string representing the message
		"""

		if message is not None and not isinstance(message, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: message EXPECTED TYPE: str', None, None)
		
		self.__message = message
		self.__key_modified['message'] = 1

	def get_index(self):
		"""
		The method to get the index

		Returns:
			int: An int representing the index
		"""

		return self.__index

	def set_index(self, index):
		"""
		The method to set the value to index

		Parameters:
			index (int) : An int representing the index
		"""

		if index is not None and not isinstance(index, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: index EXPECTED TYPE: int', None, None)
		
		self.__index = index
		self.__key_modified['index'] = 1

	def get_parent_api_name(self):
		"""
		The method to get the parent_api_name

		Returns:
			string: A string representing the parent_api_name
		"""

		return self.__parent_api_name

	def set_parent_api_name(self, parent_api_name):
		"""
		The method to set the value to parent_api_name

		Parameters:
			parent_api_name (string) : A string representing the parent_api_name
		"""

		if parent_api_name is not None and not isinstance(parent_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent_api_name EXPECTED TYPE: str', None, None)
		
		self.__parent_api_name = parent_api_name
		self.__key_modified['parent_api_name'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification
