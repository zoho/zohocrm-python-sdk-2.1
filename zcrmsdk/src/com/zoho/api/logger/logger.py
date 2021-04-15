try:
    import logging
    from zcrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
    from ...crm.api.util.constants import Constants
except:
    from ...crm.api.util.constants import Constants
    from zcrmsdk.src.com.zoho.crm.api.exception import SDKException


class Logger(object):

    """
    This class represents the Logger level and the file path.
    """

    def __init__(self, level, file_path):
        self.__level = level
        self.__file_path = file_path

    def get_level(self):
        """
        This is a getter method to get __level.

        Returns:
            string: A enum representing __level
        """

        return self.__level

    def get_file_path(self):
        """
        This is a getter method to get __file_path.

        Returns:
            string: A string representing __file_path
        """

        return self.__file_path

    @staticmethod
    def get_instance(level, file_path):

        """
        Creates an Logger class instance with the specified log level and file path.
        :param level: A Levels class instance containing the log level.
        :param file_path: A str containing the log file path.
        :return: A Logger class instance.
        """

        return Logger(level=level, file_path=file_path)

    import enum

    class Levels(enum.Enum):

        """
        This class represents the possible logger levels
        """

        CRITICAL = logging.CRITICAL
        ERROR = logging.ERROR
        WARNING = logging.WARNING
        INFO = logging.INFO
        DEBUG = logging.DEBUG
        NOTSET = logging.NOTSET


class SDKLogger(object):

    """
    The class to initialize the SDK logger.
    """

    def __init__(self, logger_instance):

        logger = logging.getLogger('SDKLogger')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(filename)s - %(funcName)s - %(lineno)d  - %(message)s')
        logger.setLevel(logger_instance.get_level().name)
        file_handler = logging.FileHandler(logger_instance.get_file_path())
        file_handler.setLevel(logger_instance.get_level().name)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    @staticmethod
    def initialize(logger_instance):
        try:
            SDKLogger(logger_instance=logger_instance)
        except Exception as ex:
            raise SDKException(message=Constants.LOGGER_INITIALIZATION_ERROR, Exception=ex)
