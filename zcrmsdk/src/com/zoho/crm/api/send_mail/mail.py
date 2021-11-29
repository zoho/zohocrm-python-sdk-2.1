try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Mail(object):
	def __init__(self):
		"""Creates an instance of Mail"""

		self.__from_1 = None
		self.__to = None
		self.__cc = None
		self.__bcc = None
		self.__reply_to = None
		self.__template = None
		self.__email = None
		self.__id = None
		self.__in_reply_to = None
		self.__scheduled_time = None
		self.__subject = None
		self.__content = None
		self.__paper_type = None
		self.__view_type = None
		self.__mail_format = None
		self.__consent_email = None
		self.__org_email = None
		self.__attachments = None
		self.__inventory_details = None
		self.__data_subject_request = None
		self.__key_modified = dict()

	def get_from(self):
		"""
		The method to get the from

		Returns:
			UserAddress: An instance of UserAddress
		"""

		return self.__from_1

	def set_from(self, from_1):
		"""
		The method to set the value to from

		Parameters:
			from_1 (UserAddress) : An instance of UserAddress
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.send_mail.user_address import UserAddress
		except Exception:
			from .user_address import UserAddress

		if from_1 is not None and not isinstance(from_1, UserAddress):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_1 EXPECTED TYPE: UserAddress', None, None)
		
		self.__from_1 = from_1
		self.__key_modified['from'] = 1

	def get_to(self):
		"""
		The method to get the to

		Returns:
			list: An instance of list
		"""

		return self.__to

	def set_to(self, to):
		"""
		The method to set the value to to

		Parameters:
			to (list) : An instance of list
		"""

		if to is not None and not isinstance(to, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: to EXPECTED TYPE: list', None, None)
		
		self.__to = to
		self.__key_modified['to'] = 1

	def get_cc(self):
		"""
		The method to get the cc

		Returns:
			list: An instance of list
		"""

		return self.__cc

	def set_cc(self, cc):
		"""
		The method to set the value to cc

		Parameters:
			cc (list) : An instance of list
		"""

		if cc is not None and not isinstance(cc, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: cc EXPECTED TYPE: list', None, None)
		
		self.__cc = cc
		self.__key_modified['cc'] = 1

	def get_bcc(self):
		"""
		The method to get the bcc

		Returns:
			list: An instance of list
		"""

		return self.__bcc

	def set_bcc(self, bcc):
		"""
		The method to set the value to bcc

		Parameters:
			bcc (list) : An instance of list
		"""

		if bcc is not None and not isinstance(bcc, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: bcc EXPECTED TYPE: list', None, None)
		
		self.__bcc = bcc
		self.__key_modified['bcc'] = 1

	def get_reply_to(self):
		"""
		The method to get the reply_to

		Returns:
			UserAddress: An instance of UserAddress
		"""

		return self.__reply_to

	def set_reply_to(self, reply_to):
		"""
		The method to set the value to reply_to

		Parameters:
			reply_to (UserAddress) : An instance of UserAddress
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.send_mail.user_address import UserAddress
		except Exception:
			from .user_address import UserAddress

		if reply_to is not None and not isinstance(reply_to, UserAddress):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reply_to EXPECTED TYPE: UserAddress', None, None)
		
		self.__reply_to = reply_to
		self.__key_modified['reply_to'] = 1

	def get_template(self):
		"""
		The method to get the template

		Returns:
			Template: An instance of Template
		"""

		return self.__template

	def set_template(self, template):
		"""
		The method to set the value to template

		Parameters:
			template (Template) : An instance of Template
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.send_mail.template import Template
		except Exception:
			from .template import Template

		if template is not None and not isinstance(template, Template):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: template EXPECTED TYPE: Template', None, None)
		
		self.__template = template
		self.__key_modified['template'] = 1

	def get_email(self):
		"""
		The method to get the email

		Returns:
			int: An int representing the email
		"""

		return self.__email

	def set_email(self, email):
		"""
		The method to set the value to email

		Parameters:
			email (int) : An int representing the email
		"""

		if email is not None and not isinstance(email, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email EXPECTED TYPE: int', None, None)
		
		self.__email = email
		self.__key_modified['email'] = 1

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

	def get_in_reply_to(self):
		"""
		The method to get the in_reply_to

		Returns:
			string: A string representing the in_reply_to
		"""

		return self.__in_reply_to

	def set_in_reply_to(self, in_reply_to):
		"""
		The method to set the value to in_reply_to

		Parameters:
			in_reply_to (string) : A string representing the in_reply_to
		"""

		if in_reply_to is not None and not isinstance(in_reply_to, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: in_reply_to EXPECTED TYPE: str', None, None)
		
		self.__in_reply_to = in_reply_to
		self.__key_modified['in_reply_to'] = 1

	def get_scheduled_time(self):
		"""
		The method to get the scheduled_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__scheduled_time

	def set_scheduled_time(self, scheduled_time):
		"""
		The method to set the value to scheduled_time

		Parameters:
			scheduled_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if scheduled_time is not None and not isinstance(scheduled_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: scheduled_time EXPECTED TYPE: datetime', None, None)
		
		self.__scheduled_time = scheduled_time
		self.__key_modified['scheduled_time'] = 1

	def get_subject(self):
		"""
		The method to get the subject

		Returns:
			string: A string representing the subject
		"""

		return self.__subject

	def set_subject(self, subject):
		"""
		The method to set the value to subject

		Parameters:
			subject (string) : A string representing the subject
		"""

		if subject is not None and not isinstance(subject, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: subject EXPECTED TYPE: str', None, None)
		
		self.__subject = subject
		self.__key_modified['subject'] = 1

	def get_content(self):
		"""
		The method to get the content

		Returns:
			string: A string representing the content
		"""

		return self.__content

	def set_content(self, content):
		"""
		The method to set the value to content

		Parameters:
			content (string) : A string representing the content
		"""

		if content is not None and not isinstance(content, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: content EXPECTED TYPE: str', None, None)
		
		self.__content = content
		self.__key_modified['content'] = 1

	def get_paper_type(self):
		"""
		The method to get the paper_type

		Returns:
			string: A string representing the paper_type
		"""

		return self.__paper_type

	def set_paper_type(self, paper_type):
		"""
		The method to set the value to paper_type

		Parameters:
			paper_type (string) : A string representing the paper_type
		"""

		if paper_type is not None and not isinstance(paper_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: paper_type EXPECTED TYPE: str', None, None)
		
		self.__paper_type = paper_type
		self.__key_modified['paper_type'] = 1

	def get_view_type(self):
		"""
		The method to get the view_type

		Returns:
			string: A string representing the view_type
		"""

		return self.__view_type

	def set_view_type(self, view_type):
		"""
		The method to set the value to view_type

		Parameters:
			view_type (string) : A string representing the view_type
		"""

		if view_type is not None and not isinstance(view_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: view_type EXPECTED TYPE: str', None, None)
		
		self.__view_type = view_type
		self.__key_modified['view_type'] = 1

	def get_mail_format(self):
		"""
		The method to get the mail_format

		Returns:
			string: A string representing the mail_format
		"""

		return self.__mail_format

	def set_mail_format(self, mail_format):
		"""
		The method to set the value to mail_format

		Parameters:
			mail_format (string) : A string representing the mail_format
		"""

		if mail_format is not None and not isinstance(mail_format, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mail_format EXPECTED TYPE: str', None, None)
		
		self.__mail_format = mail_format
		self.__key_modified['mail_format'] = 1

	def get_consent_email(self):
		"""
		The method to get the consent_email

		Returns:
			bool: A bool representing the consent_email
		"""

		return self.__consent_email

	def set_consent_email(self, consent_email):
		"""
		The method to set the value to consent_email

		Parameters:
			consent_email (bool) : A bool representing the consent_email
		"""

		if consent_email is not None and not isinstance(consent_email, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: consent_email EXPECTED TYPE: bool', None, None)
		
		self.__consent_email = consent_email
		self.__key_modified['consent_email'] = 1

	def get_org_email(self):
		"""
		The method to get the org_email

		Returns:
			bool: A bool representing the org_email
		"""

		return self.__org_email

	def set_org_email(self, org_email):
		"""
		The method to set the value to org_email

		Parameters:
			org_email (bool) : A bool representing the org_email
		"""

		if org_email is not None and not isinstance(org_email, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: org_email EXPECTED TYPE: bool', None, None)
		
		self.__org_email = org_email
		self.__key_modified['org_email'] = 1

	def get_attachments(self):
		"""
		The method to get the attachments

		Returns:
			list: An instance of list
		"""

		return self.__attachments

	def set_attachments(self, attachments):
		"""
		The method to set the value to attachments

		Parameters:
			attachments (list) : An instance of list
		"""

		if attachments is not None and not isinstance(attachments, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: attachments EXPECTED TYPE: list', None, None)
		
		self.__attachments = attachments
		self.__key_modified['attachments'] = 1

	def get_inventory_details(self):
		"""
		The method to get the inventory_details

		Returns:
			InventoryDetails: An instance of InventoryDetails
		"""

		return self.__inventory_details

	def set_inventory_details(self, inventory_details):
		"""
		The method to set the value to inventory_details

		Parameters:
			inventory_details (InventoryDetails) : An instance of InventoryDetails
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.send_mail.inventory_details import InventoryDetails
		except Exception:
			from .inventory_details import InventoryDetails

		if inventory_details is not None and not isinstance(inventory_details, InventoryDetails):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: inventory_details EXPECTED TYPE: InventoryDetails', None, None)
		
		self.__inventory_details = inventory_details
		self.__key_modified['inventory_details'] = 1

	def get_data_subject_request(self):
		"""
		The method to get the data_subject_request

		Returns:
			DataSubjectRequest: An instance of DataSubjectRequest
		"""

		return self.__data_subject_request

	def set_data_subject_request(self, data_subject_request):
		"""
		The method to set the value to data_subject_request

		Parameters:
			data_subject_request (DataSubjectRequest) : An instance of DataSubjectRequest
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.send_mail.data_subject_request import DataSubjectRequest
		except Exception:
			from .data_subject_request import DataSubjectRequest

		if data_subject_request is not None and not isinstance(data_subject_request, DataSubjectRequest):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data_subject_request EXPECTED TYPE: DataSubjectRequest', None, None)
		
		self.__data_subject_request = data_subject_request
		self.__key_modified['data_subject_request'] = 1

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
