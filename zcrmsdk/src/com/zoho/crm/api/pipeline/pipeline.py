try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Pipeline(object):
	def __init__(self):
		"""Creates an instance of Pipeline"""

		self.__from_1 = None
		self.__to = None
		self.__parent = None
		self.__child_available = None
		self.__display_value = None
		self.__default = None
		self.__maps = None
		self.__actual_value = None
		self.__id = None
		self.__key_modified = dict()

	def get_from(self):
		"""
		The method to get the from

		Returns:
			int: An int representing the from_1
		"""

		return self.__from_1

	def set_from(self, from_1):
		"""
		The method to set the value to from

		Parameters:
			from_1 (int) : An int representing the from_1
		"""

		if from_1 is not None and not isinstance(from_1, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_1 EXPECTED TYPE: int', None, None)
		
		self.__from_1 = from_1
		self.__key_modified['from'] = 1

	def get_to(self):
		"""
		The method to get the to

		Returns:
			int: An int representing the to
		"""

		return self.__to

	def set_to(self, to):
		"""
		The method to set the value to to

		Parameters:
			to (int) : An int representing the to
		"""

		if to is not None and not isinstance(to, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: to EXPECTED TYPE: int', None, None)
		
		self.__to = to
		self.__key_modified['to'] = 1

	def get_parent(self):
		"""
		The method to get the parent

		Returns:
			Pipeline: An instance of Pipeline
		"""

		return self.__parent

	def set_parent(self, parent):
		"""
		The method to set the value to parent

		Parameters:
			parent (Pipeline) : An instance of Pipeline
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.pipeline import Pipeline
		except Exception:
			from .pipeline import Pipeline

		if parent is not None and not isinstance(parent, Pipeline):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent EXPECTED TYPE: Pipeline', None, None)
		
		self.__parent = parent
		self.__key_modified['parent'] = 1

	def get_child_available(self):
		"""
		The method to get the child_available

		Returns:
			bool: A bool representing the child_available
		"""

		return self.__child_available

	def set_child_available(self, child_available):
		"""
		The method to set the value to child_available

		Parameters:
			child_available (bool) : A bool representing the child_available
		"""

		if child_available is not None and not isinstance(child_available, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: child_available EXPECTED TYPE: bool', None, None)
		
		self.__child_available = child_available
		self.__key_modified['child_available'] = 1

	def get_display_value(self):
		"""
		The method to get the display_value

		Returns:
			string: A string representing the display_value
		"""

		return self.__display_value

	def set_display_value(self, display_value):
		"""
		The method to set the value to display_value

		Parameters:
			display_value (string) : A string representing the display_value
		"""

		if display_value is not None and not isinstance(display_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_value EXPECTED TYPE: str', None, None)
		
		self.__display_value = display_value
		self.__key_modified['display_value'] = 1

	def get_default(self):
		"""
		The method to get the default

		Returns:
			bool: A bool representing the default
		"""

		return self.__default

	def set_default(self, default):
		"""
		The method to set the value to default

		Parameters:
			default (bool) : A bool representing the default
		"""

		if default is not None and not isinstance(default, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default EXPECTED TYPE: bool', None, None)
		
		self.__default = default
		self.__key_modified['default'] = 1

	def get_maps(self):
		"""
		The method to get the maps

		Returns:
			list: An instance of list
		"""

		return self.__maps

	def set_maps(self, maps):
		"""
		The method to set the value to maps

		Parameters:
			maps (list) : An instance of list
		"""

		if maps is not None and not isinstance(maps, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: maps EXPECTED TYPE: list', None, None)
		
		self.__maps = maps
		self.__key_modified['maps'] = 1

	def get_actual_value(self):
		"""
		The method to get the actual_value

		Returns:
			string: A string representing the actual_value
		"""

		return self.__actual_value

	def set_actual_value(self, actual_value):
		"""
		The method to set the value to actual_value

		Parameters:
			actual_value (string) : A string representing the actual_value
		"""

		if actual_value is not None and not isinstance(actual_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: actual_value EXPECTED TYPE: str', None, None)
		
		self.__actual_value = actual_value
		self.__key_modified['actual_value'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

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
