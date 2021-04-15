try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
	from zcrmsdk.src.com.zoho.crm.api.record.record import Record
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .record import Record


class PriceBook(Record):
	def __init__(self):
		"""Creates an instance of PriceBook"""
		super().__init__()


	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.get_key_value('name')

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.add_key_value('name', name)
