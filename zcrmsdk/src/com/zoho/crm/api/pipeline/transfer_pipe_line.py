try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class TransferPipeLine(object):
	def __init__(self):
		"""Creates an instance of TransferPipeLine"""

		self.__pipeline = None
		self.__stages = None
		self.__key_modified = dict()

	def get_pipeline(self):
		"""
		The method to get the pipeline

		Returns:
			Pipeline: An instance of Pipeline
		"""

		return self.__pipeline

	def set_pipeline(self, pipeline):
		"""
		The method to set the value to pipeline

		Parameters:
			pipeline (Pipeline) : An instance of Pipeline
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.pipeline.pipeline import Pipeline
		except Exception:
			from .pipeline import Pipeline

		if pipeline is not None and not isinstance(pipeline, Pipeline):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pipeline EXPECTED TYPE: Pipeline', None, None)
		
		self.__pipeline = pipeline
		self.__key_modified['pipeline'] = 1

	def get_stages(self):
		"""
		The method to get the stages

		Returns:
			list: An instance of list
		"""

		return self.__stages

	def set_stages(self, stages):
		"""
		The method to set the value to stages

		Parameters:
			stages (list) : An instance of list
		"""

		if stages is not None and not isinstance(stages, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: stages EXPECTED TYPE: list', None, None)
		
		self.__stages = stages
		self.__key_modified['stages'] = 1

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
