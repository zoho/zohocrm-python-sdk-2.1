try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class HistoryTracking(object):
	def __init__(self):
		"""Creates an instance of HistoryTracking"""

		self.__module = None
		self.__duration_configured_field = None
		self.__key_modified = dict()

	def get_module(self):
		"""
		The method to get the module

		Returns:
			Module: An instance of Module
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (Module) : An instance of Module
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.fields.module import Module
		except Exception:
			from .module import Module

		if module is not None and not isinstance(module, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Module', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_duration_configured_field(self):
		"""
		The method to get the duration_configured_field

		Returns:
			Field: An instance of Field
		"""

		return self.__duration_configured_field

	def set_duration_configured_field(self, duration_configured_field):
		"""
		The method to set the value to duration_configured_field

		Parameters:
			duration_configured_field (Field) : An instance of Field
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.fields.field import Field
		except Exception:
			from .field import Field

		if duration_configured_field is not None and not isinstance(duration_configured_field, Field):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: duration_configured_field EXPECTED TYPE: Field', None, None)
		
		self.__duration_configured_field = duration_configured_field
		self.__key_modified['duration_configured_field'] = 1

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
