try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Button(object):
	def __init__(self):
		"""Creates an instance of Button"""

		self.__id = None
		self.__sequence_number = None
		self.__display_label = None
		self.__criteria = None
		self.__target_screen = None
		self.__type = None
		self.__color = None
		self.__shape = None
		self.__background_color = None
		self.__key_modified = dict()

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

	def get_sequence_number(self):
		"""
		The method to get the sequence_number

		Returns:
			int: An int representing the sequence_number
		"""

		return self.__sequence_number

	def set_sequence_number(self, sequence_number):
		"""
		The method to set the value to sequence_number

		Parameters:
			sequence_number (int) : An int representing the sequence_number
		"""

		if sequence_number is not None and not isinstance(sequence_number, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sequence_number EXPECTED TYPE: int', None, None)
		
		self.__sequence_number = sequence_number
		self.__key_modified['sequence_number'] = 1

	def get_display_label(self):
		"""
		The method to get the display_label

		Returns:
			string: A string representing the display_label
		"""

		return self.__display_label

	def set_display_label(self, display_label):
		"""
		The method to set the value to display_label

		Parameters:
			display_label (string) : A string representing the display_label
		"""

		if display_label is not None and not isinstance(display_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_label EXPECTED TYPE: str', None, None)
		
		self.__display_label = display_label
		self.__key_modified['display_label'] = 1

	def get_criteria(self):
		"""
		The method to get the criteria

		Returns:
			Criteria: An instance of Criteria
		"""

		return self.__criteria

	def set_criteria(self, criteria):
		"""
		The method to set the value to criteria

		Parameters:
			criteria (Criteria) : An instance of Criteria
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.customviews import Criteria
		except Exception:
			from ..custom_views import Criteria

		if criteria is not None and not isinstance(criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__criteria = criteria
		self.__key_modified['criteria'] = 1

	def get_target_screen(self):
		"""
		The method to get the target_screen

		Returns:
			Screen: An instance of Screen
		"""

		return self.__target_screen

	def set_target_screen(self, target_screen):
		"""
		The method to set the value to target_screen

		Parameters:
			target_screen (Screen) : An instance of Screen
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.wizards.screen import Screen
		except Exception:
			from .screen import Screen

		if target_screen is not None and not isinstance(target_screen, Screen):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: target_screen EXPECTED TYPE: Screen', None, None)
		
		self.__target_screen = target_screen
		self.__key_modified['target_screen'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_color(self):
		"""
		The method to get the color

		Returns:
			string: A string representing the color
		"""

		return self.__color

	def set_color(self, color):
		"""
		The method to set the value to color

		Parameters:
			color (string) : A string representing the color
		"""

		if color is not None and not isinstance(color, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: color EXPECTED TYPE: str', None, None)
		
		self.__color = color
		self.__key_modified['color'] = 1

	def get_shape(self):
		"""
		The method to get the shape

		Returns:
			string: A string representing the shape
		"""

		return self.__shape

	def set_shape(self, shape):
		"""
		The method to set the value to shape

		Parameters:
			shape (string) : A string representing the shape
		"""

		if shape is not None and not isinstance(shape, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shape EXPECTED TYPE: str', None, None)
		
		self.__shape = shape
		self.__key_modified['shape'] = 1

	def get_background_color(self):
		"""
		The method to get the background_color

		Returns:
			string: A string representing the background_color
		"""

		return self.__background_color

	def set_background_color(self, background_color):
		"""
		The method to set the value to background_color

		Parameters:
			background_color (string) : A string representing the background_color
		"""

		if background_color is not None and not isinstance(background_color, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: background_color EXPECTED TYPE: str', None, None)
		
		self.__background_color = background_color
		self.__key_modified['background_color'] = 1

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
