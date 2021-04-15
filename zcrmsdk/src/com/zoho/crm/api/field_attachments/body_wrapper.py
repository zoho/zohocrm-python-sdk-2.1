try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import StreamWrapper, Constants
except Exception:
	from ..exception import SDKException
	from ..util import StreamWrapper, Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__file = None
		self.__key_modified = dict()

	def get_file(self):
		"""
		The method to get the file

		Returns:
			list: An instance of list
		"""

		return self.__file

	def set_file(self, file):
		"""
		The method to set the value to file

		Parameters:
			file (list) : An instance of list
		"""

		if file is not None and not isinstance(file, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file EXPECTED TYPE: list', None, None)
		
		self.__file = file
		self.__key_modified['file'] = 1

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
