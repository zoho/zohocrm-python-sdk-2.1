try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ImageUpload(object):
	def __init__(self):
		"""Creates an instance of ImageUpload"""

		self.__description = None
		self.__preview_id = None
		self.__encrypted_id = None
		self.__file_name = None
		self.__state = None
		self.__file_id = None
		self.__size = None
		self.__sequence_number = None
		self.__id = None
		self.__key_modified = dict()

	def get_description(self):
		"""
		The method to get the description

		Returns:
			string: A string representing the description
		"""

		return self.__description

	def set_description(self, description):
		"""
		The method to set the value to description

		Parameters:
			description (string) : A string representing the description
		"""

		if description is not None and not isinstance(description, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: description EXPECTED TYPE: str', None, None)
		
		self.__description = description
		self.__key_modified['Description'] = 1

	def get_preview_id(self):
		"""
		The method to get the preview_id

		Returns:
			string: A string representing the preview_id
		"""

		return self.__preview_id

	def set_preview_id(self, preview_id):
		"""
		The method to set the value to preview_id

		Parameters:
			preview_id (string) : A string representing the preview_id
		"""

		if preview_id is not None and not isinstance(preview_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: preview_id EXPECTED TYPE: str', None, None)
		
		self.__preview_id = preview_id
		self.__key_modified['Preview_Id'] = 1

	def get_encrypted_id(self):
		"""
		The method to get the encrypted_id

		Returns:
			string: A string representing the encrypted_id
		"""

		return self.__encrypted_id

	def set_encrypted_id(self, encrypted_id):
		"""
		The method to set the value to encrypted_id

		Parameters:
			encrypted_id (string) : A string representing the encrypted_id
		"""

		if encrypted_id is not None and not isinstance(encrypted_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: encrypted_id EXPECTED TYPE: str', None, None)
		
		self.__encrypted_id = encrypted_id
		self.__key_modified['Encrypted_Id'] = 1

	def get_file_name(self):
		"""
		The method to get the file_name

		Returns:
			string: A string representing the file_name
		"""

		return self.__file_name

	def set_file_name(self, file_name):
		"""
		The method to set the value to file_name

		Parameters:
			file_name (string) : A string representing the file_name
		"""

		if file_name is not None and not isinstance(file_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_name EXPECTED TYPE: str', None, None)
		
		self.__file_name = file_name
		self.__key_modified['File_Name'] = 1

	def get_state(self):
		"""
		The method to get the state

		Returns:
			string: A string representing the state
		"""

		return self.__state

	def set_state(self, state):
		"""
		The method to set the value to state

		Parameters:
			state (string) : A string representing the state
		"""

		if state is not None and not isinstance(state, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: state EXPECTED TYPE: str', None, None)
		
		self.__state = state
		self.__key_modified['State'] = 1

	def get_file_id(self):
		"""
		The method to get the file_id

		Returns:
			string: A string representing the file_id
		"""

		return self.__file_id

	def set_file_id(self, file_id):
		"""
		The method to set the value to file_id

		Parameters:
			file_id (string) : A string representing the file_id
		"""

		if file_id is not None and not isinstance(file_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_id EXPECTED TYPE: str', None, None)
		
		self.__file_id = file_id
		self.__key_modified['File_Id'] = 1

	def get_size(self):
		"""
		The method to get the size

		Returns:
			int: An int representing the size
		"""

		return self.__size

	def set_size(self, size):
		"""
		The method to set the value to size

		Parameters:
			size (int) : An int representing the size
		"""

		if size is not None and not isinstance(size, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: size EXPECTED TYPE: int', None, None)
		
		self.__size = size
		self.__key_modified['Size'] = 1

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
		self.__key_modified['Sequence_Number'] = 1

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
