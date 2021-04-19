try:
    import logging
    import threading
    import datetime
    import time
    import os
    import json
    import zlib
    import base64
    import re
    from zcrmsdk.src.com.zoho.crm.api.util import Constants
    from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
    from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
    from zcrmsdk.src.com.zoho.crm.api.header_map import HeaderMap

except Exception:
    import logging
    import threading
    import os
    import json
    import time
    import datetime
    import zlib
    import base64
    import re
    from .constants import Constants
    from ..initializer import Initializer
    from ..exception import SDKException
    from ..header_map import HeaderMap


class Utility(object):
    """
    This class handles module field details.
    """

    apitype_vs_datatype = {}
    apitype_vs_structurename = {}
    new_file = False
    get_modified_modules = False
    force_refresh = False
    lock = threading.RLock()
    logger = logging.getLogger('SDKLogger')

    @staticmethod
    def set_handler_api_path(module_api_name, handler_instance):

        if handler_instance is None:
            return

        api_path = handler_instance.get_api_path()

        if module_api_name.lower() in api_path.lower():
            api_path_split = api_path.split("/")

            for i in range(len(api_path_split)):
                split_lower = api_path_split[i].lower()
                if split_lower == module_api_name.lower():
                    api_path_split[i] = module_api_name
                elif split_lower in Constants.DEFAULT_MODULENAME_VS_APINAME and Constants.DEFAULT_MODULENAME_VS_APINAME.get(split_lower) is not None:
                    api_path_split[i] = Constants.DEFAULT_MODULENAME_VS_APINAME.get(split_lower)

            api_path = "/".join(api_path_split)
            handler_instance.set_api_path(api_path)

    @staticmethod
    def get_fields(module_api_name, handler_instance=None):

        """
        This method to fetch field details of the current module for the current user and store the result in a JSON file.

        Parameters:
            module_api_name (str) : A string containing the CRM module API name.
            handler_instance (CommonAPIHandler) : A CommonAPIHandler instance.
        """

        try:
            from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
        except Exception:
            from ..initializer import Initializer

        last_modified_time = None

        try:
            with Utility.lock:
                resources_path = os.path.join(Initializer.get_initializer().resource_path,
                                              Constants.FIELD_DETAILS_DIRECTORY)

                if not os.path.exists(resources_path):
                    if module_api_name is not None and Utility.search_json_details(module_api_name) is not None:
                        return
                    os.makedirs(resources_path)

                module_api_name = Utility.verify_module_api_name(module_api_name)

                Utility.set_handler_api_path(module_api_name, handler_instance)

                record_field_details_path = Utility.get_file_name()

                if os.path.exists(record_field_details_path):
                    Utility.file_exists_flow(module_api_name, record_field_details_path, last_modified_time)
                elif Initializer.get_initializer().sdk_config.get_auto_refresh_fields():
                    Utility.new_file = True
                    Utility.fill_data_type()
                    api_supported_modules = Utility.get_modules(None)
                    record_field_details_json = Initializer.get_json(record_field_details_path) if os.path.exists(record_field_details_path) else {}

                    record_field_details_json[Constants.FIELDS_LAST_MODIFIED_TIME] = time.time() * 1000

                    for module in api_supported_modules:
                        if module.lower() not in record_field_details_json:
                            record_field_details_json[module.lower()] = {}
                            Utility.write_to_file(file_path=record_field_details_path,
                                                  file_contents=record_field_details_json)
                            field_details = Utility.get_fields_details(api_supported_modules[module][Constants.API_NAME])
                            record_field_details_json = Initializer.get_json(record_field_details_path)
                            record_field_details_json[module.lower()] = field_details
                            Utility.write_to_file(file_path=record_field_details_path,
                                                  file_contents=record_field_details_json)

                    Utility.new_file = False

                elif Utility.force_refresh and not Utility.get_modified_modules:
                    Utility.get_modified_modules = True
                    record_field_details_json = {}
                    Utility.write_to_file(file_path=record_field_details_path, file_contents=record_field_details_json)
                    Utility.modify_fields(record_field_details_path, last_modified_time)
                    Utility.get_modified_modules = False

                else:
                    Utility.fill_data_type()
                    record_field_details_json = {module_api_name.lower(): {}}
                    Utility.write_to_file(file_path=record_field_details_path, file_contents=record_field_details_json)
                    field_details = Utility.get_fields_details(module_api_name)
                    record_field_details_json = Initializer.get_json(record_field_details_path)
                    record_field_details_json[module_api_name.lower()] = field_details
                    Utility.write_to_file(file_path=record_field_details_path, file_contents=record_field_details_json)

        except Exception as e:
            if record_field_details_path is not None and os.path.exists(record_field_details_path):
                try:
                    record_field_details_json = Initializer.get_json(record_field_details_path)
                    if module_api_name is not None and module_api_name.lower() in record_field_details_json:
                        del record_field_details_json[module_api_name.lower()]

                    if Utility.new_file:
                        if Constants.FIELDS_LAST_MODIFIED_TIME in record_field_details_json:
                            del record_field_details_json[Constants.FIELDS_LAST_MODIFIED_TIME]
                        Utility.new_file = False

                    if Utility.get_modified_modules or Utility.force_refresh:
                        Utility.get_modified_modules = False
                        Utility.force_refresh = False

                        if last_modified_time is not None:
                            record_field_details_json[Constants.FIELDS_LAST_MODIFIED_TIME] = last_modified_time

                    Utility.write_to_file(file_path=record_field_details_path, file_contents=record_field_details_json)
                except Exception as ex:
                    sdk_exception = SDKException(cause=ex)
                    Utility.logger.error(Constants.EXCEPTION + sdk_exception.__str__())
                    raise sdk_exception

            if not isinstance(e, SDKException):
                e = SDKException(cause=e)
            Utility.logger.info(Constants.EXCEPTION + e.__str__())

            raise e

    @staticmethod
    def modify_fields(record_field_details_path, modified_time):
        modified_modules = Utility.get_modules(modified_time)
        record_field_details_json = Initializer.get_json(record_field_details_path)
        record_field_details_json[Constants.FIELDS_LAST_MODIFIED_TIME] = time.time() * 1000
        Utility.write_to_file(file_path=record_field_details_path, file_contents=record_field_details_json)
        if len(modified_modules) > 0:
            for module in modified_modules.keys():
                if module.lower() in record_field_details_json:
                    Utility.delete_fields(record_field_details_json, module)

            Utility.write_to_file(file_path=record_field_details_path, file_contents=record_field_details_json)

            for module in modified_modules.keys():
                module_data = modified_modules[module]
                Utility.get_fields(module_data[Constants.API_NAME])

    @staticmethod
    def file_exists_flow(module_api_name, record_field_details_path, last_modified_time):
        with Utility.lock:
            record_field_details_json = Initializer.get_json(record_field_details_path)

            if Initializer.get_initializer().sdk_config.get_auto_refresh_fields() and not Utility.new_file and not Utility.get_modified_modules and (Constants.FIELDS_LAST_MODIFIED_TIME not in record_field_details_json or Utility.force_refresh or (time.time() * 1000 - record_field_details_json[Constants.FIELDS_LAST_MODIFIED_TIME]) > 3600000):
                Utility.get_modified_modules = True
                last_modified_time = record_field_details_json[Constants.FIELDS_LAST_MODIFIED_TIME] if not Utility.force_refresh and Constants.FIELDS_LAST_MODIFIED_TIME in record_field_details_json else None
                Utility.modify_fields(record_field_details_path, last_modified_time)
                Utility.get_modified_modules = False

            elif not Initializer.get_initializer().sdk_config.get_auto_refresh_fields() and Utility.force_refresh and not Utility.get_modified_modules:
                Utility.get_modified_modules = True
                Utility.modify_fields(record_field_details_path, last_modified_time)
                Utility.get_modified_modules = False

            record_field_details_json = Initializer.get_json(record_field_details_path)

            if module_api_name is None or module_api_name.lower() in record_field_details_json:
                return

            else:
                Utility.fill_data_type()
                record_field_details_json[module_api_name.lower()] = {}
                Utility.write_to_file(file_path=record_field_details_path, file_contents=record_field_details_json)
                field_details = Utility.get_fields_details(module_api_name)
                record_field_details_json = Initializer.get_json(record_field_details_path)
                record_field_details_json[module_api_name.lower()] = field_details
                Utility.write_to_file(file_path=record_field_details_path, file_contents=record_field_details_json)

    @staticmethod
    def verify_module_api_name(module_api_name):
        if module_api_name is not None and Constants.DEFAULT_MODULENAME_VS_APINAME.get(module_api_name.lower()) is not None:
            return Constants.DEFAULT_MODULENAME_VS_APINAME.get(module_api_name.lower())

        record_field_details_path = Utility.get_file_name()
        if os.path.exists(record_field_details_path):
            fields_json = Initializer.get_json(record_field_details_path)
            if Constants.SDK_MODULE_METADATA in fields_json and module_api_name.lower() in fields_json[Constants.SDK_MODULE_METADATA]:
                return fields_json[Constants.SDK_MODULE_METADATA][module_api_name.lower()][Constants.API_NAME]

        return module_api_name

    @staticmethod
    def delete_fields(record_field_details_json, module):
        subform_modules = []
        fields_json = record_field_details_json[module.lower()]
        for key, value in fields_json.items():
            if Constants.SUBFORM in value and value[Constants.SUBFORM] and (value[Constants.MODULE]).lower() in record_field_details_json:
                subform_modules.append(value[Constants.MODULE])

        del record_field_details_json[module.lower()]

        if len(subform_modules) > 0:
            for subform_module in subform_modules:
                Utility.delete_fields(record_field_details_json, subform_module)

    @staticmethod
    def get_file_name():
        import zcrmsdk.src.com.zoho.crm.api.util.converter as Converter

        return os.path.join(Initializer.get_initializer().resource_path, Constants.FIELD_DETAILS_DIRECTORY,Converter.Converter.get_encoded_file_name())

    @staticmethod
    def get_related_lists(related_module_name, module_api_name, common_api_handler):
        with Utility.lock:
            try:
                is_new_data = False
                key = (module_api_name + Constants.UNDERSCORE + Constants.RELATED_LISTS).lower()
                resources_path = os.path.join(Initializer.get_initializer().resource_path,Constants.FIELD_DETAILS_DIRECTORY)

                if not os.path.exists(resources_path):
                    os.makedirs(resources_path)
                record_field_details_path = Utility.get_file_name()

                if not os.path.exists(record_field_details_path) or (
                        os.path.exists(record_field_details_path) and key not in Initializer.get_json(
                    record_field_details_path)):
                    is_new_data = True
                    related_list_values = Utility.get_related_list_details(module_api_name)
                    record_field_details_json = Initializer.get_json(record_field_details_path) if os.path.exists(record_field_details_path) else {}
                    record_field_details_json[key] = related_list_values
                    Utility.write_to_file(file_path=record_field_details_path, file_contents=record_field_details_json)

                record_field_details_json = Initializer.get_json(record_field_details_path)
                module_related_list = record_field_details_json[key]

                if not Utility.check_related_list_exists(related_module_name, module_related_list,common_api_handler) and not is_new_data:
                    del record_field_details_json[key]
                    Utility.write_to_file(file_path=record_field_details_path, file_contents=record_field_details_json)

                    Utility.get_related_lists(related_module_name, module_api_name, common_api_handler)

            except SDKException as e:
                Utility.logger.error(Constants.EXCEPTION + e.__str__())
                raise e

            except Exception as e:
                sdk_exception = SDKException(cause=e)
                Utility.logger.error(Constants.EXCEPTION + sdk_exception.__str__())
                raise sdk_exception

    @staticmethod
    def check_related_list_exists(related_module_name, module_related_list_array, common_api_handler):
        for related_list_jo in module_related_list_array:
            if related_list_jo[Constants.API_NAME] is not None and related_list_jo[Constants.API_NAME].lower() == related_module_name.lower():
                if related_list_jo[Constants.HREF] == Constants.NULL_VALUE:
                    raise SDKException(code=Constants.UNSUPPORTED_IN_API,
                                       message=common_api_handler.get_http_method() + ' ' + common_api_handler.get_api_path() + Constants.UNSUPPORTED_IN_API_MESSAGE)

                if related_list_jo[Constants.MODULE] != Constants.NULL_VALUE:
                    common_api_handler.set_module_api_name(related_list_jo[Constants.MODULE])
                    Utility.get_fields(related_list_jo[Constants.MODULE])
                return True

        return False

    @staticmethod
    def verify_photo_support(module_api_name):
        with Utility.lock:
            try:
                module_api_name = Utility.verify_module_api_name(module_api_name)
                if module_api_name in Constants.PHOTO_SUPPORTED_MODULES:
                    return True

                modules = Utility.get_module_names()
                if module_api_name.lower() in modules and modules[module_api_name.lower()] is not None:
                    module_meta_data = modules[module_api_name.lower()]

                    if module_meta_data[Constants.GENERATED_TYPE] != Constants.GENERATED_TYPE_CUSTOM:
                        raise SDKException(code=Constants.UPLOAD_PHOTO_UNSUPPORTED_ERROR,
                                           message=Constants.UPLOAD_PHOTO_UNSUPPORTED_MESSAGE + module_api_name)
            except SDKException as e:
                raise e

            except Exception as e:
                sdk_exception = SDKException(message=Constants.EXCEPTION, cause=e)
                raise sdk_exception

            return True

    @staticmethod
    def get_module_names():
        module_data = {}
        resources_path = os.path.join(Initializer.get_initializer().resource_path,
                                      Constants.FIELD_DETAILS_DIRECTORY)
        if not os.path.exists(resources_path):
            os.makedirs(resources_path)

        record_field_details_path = Utility.get_file_name()

        is_null = False
        if os.path.exists(record_field_details_path):
            json = Initializer.get_json(record_field_details_path)
            if Constants.SDK_MODULE_METADATA not in json:
                is_null = True
            elif json[Constants.SDK_MODULE_METADATA] is None:
                is_null = True

        if not os.path.exists(record_field_details_path) or is_null:
            module_data = Utility.get_modules(None)
            Utility.write_module_meta_data(record_field_details_path, module_data)
            return module_data

        record_field_details_json = Initializer.get_json(record_field_details_path)
        module_data = record_field_details_json[Constants.SDK_MODULE_METADATA]
        return module_data

    @staticmethod
    def write_module_meta_data(record_field_details_path, module_data):
        field_details_json = Initializer.get_json(record_field_details_path) if os.path.exists(
            record_field_details_path) else {}
        field_details_json[Constants.SDK_MODULE_METADATA] = module_data
        Utility.write_to_file(record_field_details_path, field_details_json)

    @staticmethod
    def get_related_list_details(module_api_name):
        import zcrmsdk.src.com.zoho.crm.api.related_lists as RelatedLists

        related_list_array = []

        response = RelatedLists.RelatedListsOperations(module_api_name).get_related_lists()

        if response is not None:
            if response.get_status_code() == Constants.NO_CONTENT_STATUS_CODE:
                return related_list_array

            data_object = response.get_object()

            if data_object is not None:

                if isinstance(data_object, RelatedLists.ResponseWrapper):
                    related_lists = data_object.get_related_lists()

                    for related_list in related_lists:
                        related_list_detail = {
                            Constants.API_NAME: related_list.get_api_name(),
                            Constants.MODULE: related_list.get_module() if related_list.get_module() is not None else Constants.NULL_VALUE,
                            Constants.NAME: related_list.get_name(),
                            Constants.HREF: related_list.get_href() if related_list.get_href() is not None else Constants.NULL_VALUE
                        }
                        related_list_array.append(related_list_detail)

                elif isinstance(data_object, RelatedLists.APIException):
                    error_response = {
                        Constants.CODE: data_object.get_code().get_value(),
                        Constants.STATUS: data_object.get_status().get_value(),
                        Constants.MESSAGE: data_object.get_message().get_value()
                    }
                    raise SDKException(code=Constants.API_EXCEPTION, details=error_response)

                else:
                    error_response = {
                        Constants.CODE: response.get_status_code()
                    }
                    raise SDKException(code=Constants.API_EXCEPTION, details=error_response)

            else:
                error_response = {
                    Constants.CODE: response.get_status_code()
                }
                raise SDKException(code=Constants.API_EXCEPTION, details=error_response)

        return related_list_array

    @staticmethod
    def get_fields_details(module_api_name):

        """
        This method to get module field data from Zoho CRM.
        :param module_api_name: A str containing the CRM module API name.
        :return: A object representing the Zoho CRM module field details.
        """
        import zcrmsdk.src.com.zoho.crm.api.fields as Field

        fields_details = {}
        response = Field.FieldsOperations(module_api_name).get_fields()

        if response is not None:
            if response.get_status_code() == Constants.NO_CONTENT_STATUS_CODE:
                return fields_details

            response_object = response.get_object()

            if isinstance(response_object, Field.ResponseWrapper):
                fields = response_object.get_fields()

                for field in fields:
                    if field.get_api_name() in Constants.KEYS_TO_SKIP:
                        continue

                    field_detail = {}

                    Utility.set_data_type(field_detail, field, module_api_name)

                    fields_details[field.get_api_name()] = field_detail

                if module_api_name.lower() in Constants.INVENTORY_MODULES:
                    field_detail = {
                        Constants.NAME: Constants.LINE_TAX,
                        Constants.TYPE: Constants.LIST_NAMESPACE,
                        Constants.STRUCTURE_NAME: Constants.LINE_TAX_NAMESPACE
                    }
                    fields_details[Constants.LINE_TAX] = field_detail

                if module_api_name.lower() == Constants.NOTES:
                    field_detail = {
                        Constants.NAME: Constants.ATTACHMENTS,
                        Constants.TYPE: Constants.LIST_NAMESPACE,
                        Constants.STRUCTURE_NAME: Constants.ATTACHMENTS_NAMESPACE
                    }
                    fields_details[Constants.ATTACHMENTS] = field_detail

            elif isinstance(response_object, Field.APIException):
                error_response = {
                    Constants.CODE: response_object.get_code().get_value(),
                    Constants.STATUS: response_object.get_status().get_value(),
                    Constants.MESSAGE: response_object.get_message().get_value()
                }
                raise SDKException(code=Constants.API_EXCEPTION, details=error_response)

        else:
            error_response = {
                Constants.CODE: response.get_status_code()
            }
            raise SDKException(code=Constants.API_EXCEPTION, details=error_response)
        return fields_details

    @staticmethod
    def search_json_details(key):
        package_name = Constants.PACKAGE_NAMESPACE + 'record.' + key

        from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer

        for class_key in Initializer.json_details.keys():
            if class_key == package_name:
                return_json = {
                    Constants.MODULEPACKAGENAME: class_key,
                    Constants.MODULEDETAILS: Initializer.json_details[class_key]
                }

                return return_json

        return None

    @staticmethod
    def get_modules(header):

        import zcrmsdk.src.com.zoho.crm.api.modules as Modules

        api_names = {}
        header_map = HeaderMap()
        if header is not None:
            header_value = datetime.datetime.fromtimestamp(header / 1000.0)
            header_map.add(Modules.GetModulesHeader.if_modified_since, header_value)

        response = Modules.ModulesOperations().get_modules(header_map)

        if response is not None:
            if response.get_status_code() in [Constants.NO_CONTENT_STATUS_CODE, Constants.NOT_MODIFIED_STATUS_CODE]:
                return api_names

            response_object = response.get_object()

            if isinstance(response_object, Modules.ResponseWrapper):
                modules = response_object.get_modules()
                for module in modules:
                    if module.get_api_supported():
                        module_details = dict()
                        module_details[Constants.API_NAME] = module.get_api_name()
                        module_details[Constants.GENERATED_TYPE] = module.get_generated_type().get_value()
                        api_names[module.get_api_name().lower()] = module_details

            elif isinstance(response_object, Modules.APIException):
                error_response = {
                    Constants.CODE: response_object.get_code().get_value(),
                    Constants.STATUS: response_object.get_status().get_value(),
                    Constants.MESSAGE: response_object.get_message().get_value()
                }
                raise SDKException(code=Constants.API_EXCEPTION, details=error_response)

        if Utility.force_refresh:
            try:
                Utility.write_module_meta_data(Utility.get_file_name(), api_names)
            except Exception as e:

                raise SDKException(message=Constants.EXCEPTION, cause=e)

        return api_names

    @staticmethod
    def refresh_modules():
        Utility.force_refresh = True
        Utility.get_fields(None)
        Utility.force_refresh = False

    @staticmethod
    def get_json_object(json, key):
        for key_in_json in json.keys():
            if key_in_json.lower() == key.lower():
                return json[key_in_json]

        return None

    @staticmethod
    def check_data_type(value, type):

        if value is None:
            return False
        if type.lower() == Constants.OBJECT.lower():
            return True
        type = Constants.DATA_TYPE.get(type)
        class_name = value.__class__
        if class_name == type:
            return True
        else:
            return False

    @staticmethod
    def set_data_type(field_detail, field, module_api_name):
        api_type = field.get_data_type()
        module = ''
        key_name = field.get_api_name()

        if field.get_system_mandatory() is not None and field.get_system_mandatory() and not (
                module_api_name.lower() == Constants.CALLS and key_name.lower() == Constants.CALL_DURATION):
            field_detail[Constants.REQUIRED] = True

        if key_name in Constants.KEY_VS_INVENTORY_MODULE and module_api_name.lower() == Constants.KEY_VS_INVENTORY_MODULE.get(
                key_name):
            field_detail[Constants.NAME] = key_name
            field_detail[Constants.TYPE] = Constants.LIST_NAMESPACE
            field_detail[Constants.STRUCTURE_NAME] = Constants.INVENTORY_LINE_ITEMS
            field_detail[Constants.SKIP_MANDATORY] = True

            return

        elif key_name.lower() == Constants.PRICING_DETAILS.lower() and module_api_name.lower() == Constants.PRICE_BOOKS:
            field_detail[Constants.NAME] = key_name
            field_detail[Constants.TYPE] = Constants.LIST_NAMESPACE
            field_detail[Constants.STRUCTURE_NAME] = Constants.PRICINGDETAILS
            field_detail[Constants.SKIP_MANDATORY] = True

            return

        elif key_name.lower() == Constants.PARTICIPANT_API_NAME.lower() and (
                module_api_name.lower() == Constants.EVENTS or module_api_name.lower() == Constants.ACTIVITIES):
            field_detail[Constants.NAME] = key_name
            field_detail[Constants.TYPE] = Constants.LIST_NAMESPACE
            field_detail[Constants.STRUCTURE_NAME] = Constants.PARTICIPANTS
            field_detail[Constants.SKIP_MANDATORY] = True

            return

        elif key_name.lower() == Constants.COMMENTS.lower() and (
                module_api_name.lower() == Constants.SOLUTIONS or module_api_name.lower() == Constants.CASES):
            field_detail[Constants.NAME] = key_name
            field_detail[Constants.TYPE] = Constants.LIST_NAMESPACE
            field_detail[Constants.STRUCTURE_NAME] = Constants.COMMENT_NAMESPACE
            field_detail[Constants.LOOKUP] = True

            return

        elif key_name.lower() == Constants.LAYOUT.lower():
            field_detail[Constants.NAME] = key_name
            field_detail[Constants.TYPE] = Constants.LAYOUT_NAMESPACE
            field_detail[Constants.STRUCTURE_NAME] = Constants.LAYOUT_NAMESPACE
            field_detail[Constants.LOOKUP] = True

            return

        elif (key_name.lower() == Constants.TERRITORIES.lower() or key_name.lower() == Constants.TERRITORY.lower()) and field.get_custom_field() is not None and not field.get_custom_field():
            field_detail[Constants.NAME] = key_name
            field_detail[Constants.TYPE] = Constants.LIST_NAMESPACE
            field_detail[Constants.STRUCTURE_NAME] = Constants.TERRITORY_NAMESPACE
            field_detail[Constants.LOOKUP] = True

            return
        elif key_name.lower() == Constants.TAX.lower() or module_api_name.lower() == Constants.PRODUCTS.lower() :
            field_detail[Constants.NAME] = key_name
            field_detail[Constants.TYPE] = Constants.LIST_NAMESPACE
            field_detail[Constants.STRUCTURE_NAME] = Constants.TAX_NAMESPACE

            return
        elif api_type in Utility.apitype_vs_datatype:
            field_detail[Constants.TYPE] = Utility.apitype_vs_datatype.get(api_type)

        elif api_type.lower() == Constants.FORMULA.lower():
            if field.get_formula() is not None:
                return_type = field.get_formula().get_return_type()
                if return_type in Utility.apitype_vs_datatype:
                    field_detail[Constants.TYPE] = Utility.apitype_vs_datatype.get(return_type)

            field_detail[Constants.READ_ONLY] = True

        else:
            return

        if Constants.LOOKUP in api_type.lower():
            field_detail[Constants.LOOKUP] = True

        if Constants.CONSENT_LOOKUP in api_type.lower():
            field_detail[Constants.SKIP_MANDATORY] = True

        if Constants.MULTI_SELECT_LOOKUP in api_type.lower():
            field_detail[Constants.SKIP_MANDATORY] = True
            if field.get_multiselectlookup() is not None:
                if field.get_multiselectlookup().get_linking_module() is not None:
                    linking_module = field.get_multiselectlookup().get_linking_module()
                    field_detail[Constants.MODULE] = linking_module
                    module = linking_module

            field_detail[Constants.SUBFORM] = True

        if Constants.MULTI_USER_LOOKUP in api_type.lower():
            field_detail[Constants.SKIP_MANDATORY] = True
            if field.get_multiuserlookup() is not None:
                if field.get_multiuserlookup().get_linking_module() is not None:
                    linking_module = field.get_multiuserlookup().get_linking_module()
                    field_detail[Constants.MODULE] = linking_module
                    module = linking_module

            field_detail[Constants.SUBFORM] = True

        if api_type in Utility.apitype_vs_structurename:
            field_detail[Constants.STRUCTURE_NAME] = Utility.apitype_vs_structurename.get(api_type)

        if api_type.lower() == Constants.PICKLIST and field.get_pick_list_values() is not None and len(
                field.get_pick_list_values()) > 0:
            field_detail[Constants.PICKLIST] = True
            values = list(map(lambda x: x.get_display_value(), field.get_pick_list_values()))
            field_detail[Constants.VALUES] = values

        if api_type == Constants.SUBFORM:
            module = field.get_subform().get_module()
            field_detail[Constants.MODULE] = module
            field_detail[Constants.SKIP_MANDATORY] = True
            field_detail[Constants.SUBFORM] = True

        if api_type == Constants.LOOKUP:
            module = field.get_lookup().get_module()

            if module is not None and not module == Constants.SE_MODULE:
                field_detail[Constants.MODULE] = module
                if module.lower() == Constants.ACCOUNTS and not field.get_custom_field():
                    field_detail[Constants.SKIP_MANDATORY] = True

            else:
                module = ''

            field_detail[Constants.LOOKUP] = True

        if len(module) > 0:
            Utility.get_fields(module)

        field_detail[Constants.NAME] = key_name

    @staticmethod
    def fill_data_type():
        if len(Utility.apitype_vs_datatype) > 0:
            return

        field_api_names_string = ["textarea", "text", "website", "email", "phone", "mediumtext",
                                  "profileimage", "autonumber"]

        field_api_names_integer = ['integer']

        field_api_names_boolean = ['boolean']

        field_api_names_double = ['double', 'percent', 'lookup', 'currency']

        field_api_names_long = ['long', 'bigint']

        field_api_names_field_file = ['fileupload']

        field_api_names_datetime = ['datetime', 'event_reminder']

        field_api_names_date = ['date']

        field_api_names_lookup = ['lookup']

        field_api_names_owner_lookup = ['ownerlookup', 'userlookup']

        field_api_names_multiuser_lookup = ['multiuserlookup']

        field_api_names_multimodule_lookup = ['multimodulelookup']

        field_api_names_picklist = ['picklist']

        field_api_names_multiselect_picklist = ['multiselectpicklist']

        field_api_names_subform = ['subform']

        field_api_name_task_remind_at = ['ALARM']

        field_api_name_recurring_activity = ['RRULE']

        field_api_name_reminder = ['multireminder']

        field_api_name_consent_lookup = ['consent_lookup']

        field_api_name_image_upload = ["imageupload"]

        field_api_name_multiselect_lookup = ["multiselectlookup"]

        for field_api_name in field_api_names_string:
            Utility.apitype_vs_datatype[field_api_name] = Constants.STRING_NAMESPACE

        for field_api_name in field_api_names_integer:
            Utility.apitype_vs_datatype[field_api_name] = Constants.INTEGER_NAMESPACE

        for field_api_name in field_api_names_boolean:
            Utility.apitype_vs_datatype[field_api_name] = Constants.BOOLEAN_NAMESPACE

        for field_api_name in field_api_names_double:
            Utility.apitype_vs_datatype[field_api_name] = Constants.DOUBLE_NAMESPACE

        for field_api_name in field_api_names_long:
            Utility.apitype_vs_datatype[field_api_name] = Constants.LONG_NAMESPACE

        for field_api_name in field_api_names_datetime:
            Utility.apitype_vs_datatype[field_api_name] = Constants.DATETIME_NAMESPACE

        for field_api_name in field_api_names_date:
            Utility.apitype_vs_datatype[field_api_name] = Constants.DATE_NAMESPACE

        for field_api_name in field_api_names_lookup:
            Utility.apitype_vs_datatype[field_api_name] = Constants.RECORD_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.RECORD_NAMESPACE

        for field_api_name in field_api_names_owner_lookup:
            Utility.apitype_vs_datatype[field_api_name] = Constants.USER_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.USER_NAMESPACE

        for field_api_name in field_api_names_multiuser_lookup:
            Utility.apitype_vs_datatype[field_api_name] = Constants.LIST_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.RECORD_NAMESPACE

        for field_api_name in field_api_names_multimodule_lookup:
            Utility.apitype_vs_datatype[field_api_name] = Constants.LIST_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.MODULE_NAMESPACE

        for field_api_name in field_api_names_picklist:
            Utility.apitype_vs_datatype[field_api_name] = Constants.CHOICE_NAMESPACE

        for field_api_name in field_api_names_multiselect_picklist:
            Utility.apitype_vs_datatype[field_api_name] = Constants.LIST_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.CHOICE_NAMESPACE

        for field_api_name in field_api_names_subform:
            Utility.apitype_vs_datatype[field_api_name] = Constants.LIST_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.RECORD_NAMESPACE

        for field_api_name in field_api_names_field_file:
            Utility.apitype_vs_datatype[field_api_name] = Constants.LIST_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.FIELD_FILE_NAMESPACE

        for field_api_name in field_api_name_task_remind_at:
            Utility.apitype_vs_datatype[field_api_name] = Constants.REMINDAT_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.REMINDAT_NAMESPACE

        for field_api_name in field_api_name_recurring_activity:
            Utility.apitype_vs_datatype[field_api_name] = Constants.RECURRING_ACTIVITY_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.RECURRING_ACTIVITY_NAMESPACE

        for field_api_name in field_api_name_reminder:
            Utility.apitype_vs_datatype[field_api_name] = Constants.LIST_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.REMINDER_NAMESPACE

        for field_api_name in field_api_name_consent_lookup:
            Utility.apitype_vs_datatype[field_api_name] = Constants.CONSENT_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.CONSENT_NAMESPACE

        for field_api_name in field_api_name_image_upload:
            Utility.apitype_vs_datatype[field_api_name] = Constants.LIST_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.IMAGEUPLOAD_NAMESPACE

        for field_api_name in field_api_name_multiselect_lookup:
            Utility.apitype_vs_datatype[field_api_name] = Constants.LIST_NAMESPACE
            Utility.apitype_vs_structurename[field_api_name] = Constants.RECORD_NAMESPACE

    @staticmethod
    def write_to_file(file_path, file_contents):
        with open(file_path, mode="w") as file:
            json.dump(file_contents, file)
            file.flush()
            file.close()
