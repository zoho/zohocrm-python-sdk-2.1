try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ContactRoleWrapper(object):
	def __init__(self):
		"""Creates an instance of ContactRoleWrapper"""

		self.__contact_role = None
		self.__key_modified = dict()

	def get_contact_role(self):
		"""
		The method to get the contact_role

		Returns:
			string: A string representing the contact_role
		"""

		return self.__contact_role

	def set_contact_role(self, contact_role):
		"""
		The method to set the value to contact_role

		Parameters:
			contact_role (string) : A string representing the contact_role
		"""

		if contact_role is not None and not isinstance(contact_role, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_role EXPECTED TYPE: str', None, None)
		
		self.__contact_role = contact_role
		self.__key_modified['Contact_Role'] = 1

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
