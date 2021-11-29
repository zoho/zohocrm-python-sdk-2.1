from zcrmsdk.src.com.zoho.crm.api.fields import *
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class Field(object):

    @staticmethod
    def get_fields(module_api_name):
        """
        This method is used to get metadata about all the fields of a module and print the response.
        :param module_api_name: The API Name of the module to get fields
        """

        """
        example
        module_api_name = "Leads";
        """

        # Get instance of FieldsOperations Class that takes module_api_name as parameter
        fields_operations = FieldsOperations(module_api_name)

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for get_fields operation
        # param_instance.add(GetFieldsParam.type, "unused")

        # Call get_fields method that takes paramInstance as parameter
        response = fields_operations.get_fields(param_instance)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code()
                      == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ResponseWrapper instance is received
                if isinstance(response_object, ResponseWrapper):

                    # Get the list of obtained Field instances
                    fields_list = response_object.get_fields()

                    for field in fields_list:
                       # Get the Webhook of each Field
                        print("Webhook: " + str(field.get_webhook()))

                        # Get the JsonType of each Field
                        print("JsonType: " + str(field.get_json_type()))

                        # Get the DisplayLabel of each Field
                        print("DisplayLabel: " + field.get_display_label())

                        # Get the SystemMandatory of each Field
                        print("SystemMandatory: " +
                              str(field.get_system_mandatory()))

                        print("\n Field is Private :")
                        print(field.get_private())
                        print("\n Field is UiType :")
                        print(field.get_ui_type())
                        print("\n Field  PickListValuesSortedLexically :")
                        print(field.get_pick_list_values_sorted_lexically())

                        # Get the DataType of each Field
                        print("DataType: " + field.get_data_type())

                        # Get the ColumnName of each Field
                        print("ColumnName: " + str(field.get_column_name()))

                        # Get the PersonalityName of each Field
                        print("PersonalityName: " +
                              str(field.get_personality_name()))

                        # Get the ID of each Field
                        print("ID: " + str(field.get_id()))

                        # Get the Sortable of each Field
                        print("Sortable: " + str(field.get_sortable()))

                         # Get the TransitionSequence of each Field
                        print("TransitionSequence: " +
                              str(field.get_transition_sequence()))

                        if field.get_mandatory() is not None:
                               # Get the Mandatory of each Field
                            print("Mandatory: " +
                                  str(field.get_mandatory()))
                        if field.get_external() is not None:
                            external = field.get_external()
                            # Get the External Show of each Field
                            print("External Show: " +
                                  str(external.get_show()))
                            # Get the External Type of each Field
                            print("External Type: " +
                                  str(external.get_type()))
                            # Get the External Type of each Field
                            print("External Type: " +
                                  str(external.get_allow_multiple_config()))
                        if field.get_unique() is not None:
                            # Get the Mandatory of each Field
                            print(
                                "Mandatory: ")
                            print(field.get_unique().get_casesensitive())
                        if field.get_history_tracking() is not None:
                            # Get the HistoryTracking of each Field
                            history_tracking = field.get_history_tracking()
                            module = history_tracking.get_module()
                            if module is not None:
                                module_layout = module.get_layout()
                                if module_layout is not None:
                                    print("Module layout id: " +
                                          str(module_layout.get_id()))
                                    print("Module display label: " +
                                          str(module.get_api_name()))
                                    print("Module api name: " +
                                          str(module.get_id()))
                                    print("Module module: " +
                                          str(module.get_module()))
                                    print("Module module name: " +
                                          str(module.get_module_name()))

                            duration_configured = history_tracking.get_duration_configured_field()
                            if duration_configured is not None:
                                print(
                                    "historytracking duration configured field: " + str(duration_configured.get_id()))
                        # Get the obtained Layout instance
                        layout = field.get_layouts()

                        # Check if layout is not null
                        if layout is not None:
                            # Get the ID of the Layout
                            print("Layout ID: " + str(layout.get_id()))

                            # Get the Name of the Layout
                            print("Layout Name: " + str(layout.get_name()))

                        # Get the APIName of each Field
                        print("APIName : " + str(field.get_api_name()))

                        # Get the Content of each Field
                        print("Content: " + str(field.get_content()))

                        # Get the Message of each Field
                        print("Message :" + str(field.get_message()))

                        # Get the obtained Crypt instance
                        crypt = field.get_crypt()

                        if crypt is not None:
                            print("Crypt Details")

                            # Get the Crypt Mode
                            print("Mode: " + crypt.get_mode())

                            # Get the Crypt Column
                            print("Column: ")
                            print(crypt.get_column())

                            # Get the Crypt Table
                            print("Table: ")
                            print(crypt.get_table())

                            # Get the Crypt Status
                            print("Status: " )
                            print(crypt.get_status())

                            print("\n Crypt Notify:")
                            print(crypt.get_notify())

                            enc_fld_ids = crypt.get_encfldids()
                            if enc_fld_ids is not None:
                                print("\nEncFldIds : ")
                                for enc_fld_id in enc_fld_ids:
                                    print(enc_fld_id)

                        # Get the FieldLabel of each Field
                        print("FieldLabel: " + str(field.get_field_label()))

                        tool_tip = field.get_tooltip()

                        if tool_tip is not None:
                            # Get the Name of the ToolTip
                            print("ToolTip Name: " + tool_tip.get_name())

                            # Get the Value of the ToolTip
                            print("ToolTip Value: " + tool_tip.get_value())

                        currency = field.get_currency()

                        if currency is not None:
                            # Get the RoundingOption of the Currency
                            print("Currency RoundingOption: ")
                            print(currency.get_rounding_option())

                            # Get the Precision of the Currency
                            print("Currency Precision: ")
                            print(currency.get_precision())

                        # Get the CreatedSource of each Field
                        print("CreatedSource: " +
                              str(field.get_created_source()))

                        if field.get_display_type() is not None:
                            # Get the DisplayType of the Field
                            print("Field DisplayType: ")
                            print(field.get_display_type().get_value())

                        # Get the FieldReadOnly of each Field
                        print("FieldReadOnly: " +
                              str(field.get_field_read_only()))
                        # Get the Filterable of each Field
                        print("Filterable: " + str(field.get_filterable()))

                        # Get the Criteria of each Field
                        criteria = field.get_criteria()

                        if criteria is not None:
                            Field.print_criteria(criteria)

                        # Get the Related Details of each Field
                        related_details = field.get_related_details()

                        if related_details is not None:
                            # Get the display label of related detail
                            if related_details.get_display_label() is not None:
                                print("RelatedDetails Display Label: " +
                                      related_details.get_display_label())

                            # Get the API Name of related detail
                            print("Related Details API Name: " +
                                  str(related_details.get_api_name()))

                            # Get the module of related detail
                            if related_details.get_module() is not None:
                                module = related_details.get_module()

                                # Get the layout of the module
                                if module.get_layout() is not None:
                                    layout = module.get_layout()

                                    print(
                                        "Related Details Module Layout ID: " + layout.get_id())

                                    print(
                                        "Related Details Module Layout Name: " + layout.get_name())

                                # Get the display label of the module
                                if module.get_display_label() is not None:
                                    print(
                                        "Related Details Module Display Label: " + module.get_display_label())

                                # Get the Module API Name of the Related detail module
                                print(
                                    "Related Details Module API Name: " + str(module.get_api_name()))

                                # Get the Module of the Related detail module
                                print("Related Details Module: " +
                                        str(module.get_module()))

                                # Get the Module Name of the Related detail module
                                print("Related Details Module Name: " +
                                        module.get_module_name())

                            # Get the ID of the Related detail
                            print("Related Details ID: " +
                                    str(related_details.get_id()))

                            # Get the Type of the Related detail
                            print("Related Details Type: " +
                                      str(related_details.get_type()))

                            # Get the ReadOnly of each Field
                            if field.get_read_only() is not None:
                                print("ReadOnly: " + str(field.get_read_only()))

                            # Get the obtained AssociationDetails instance
                            association_details = field.get_association_details()

                            if association_details is not None:

                                # Get the obtained LookupField instance
                                lookup_field = association_details.get_lookup_field()

                                if lookup_field is not None:
                                    # Get the ID of the LookupField
                                    print(
                                        "AssociationDetails LookupField ID: " + lookup_field.get_id())

                                    # Get the Name of the LookupField
                                    print(
                                        'AssociationDetails LookupField Name: ' + lookup_field.get_name())

                                # Get the obtained LookupField instance
                                related_field = association_details.get_related_field()

                                if related_field is not None:
                                    # Get the ID of the RelatedField
                                    print(
                                        "AssociationDetails RelatedField ID: " + related_field.get_id())

                                    # Get the Name of the RelatedField
                                    print(
                                        'AssociationDetails RelatedField Name: ' + related_field.get_name())

                            if field.get_quick_sequence_number() is not None:
                                # Get the QuickSequenceNumber of each Field
                                print('QuickSequenceNumber: ' +
                                      str(field.get_quick_sequence_number()))

                            # Get the DisplayLabel of each Field
                            print("DisplayLabel: " + field.get_display_label())

                            if field.get_custom_field() is not None:
                                # Get if the Field is a CustomField
                                print("CustomField: " +
                                      str(field.get_custom_field()))

                            if field.get_visible() is not None:
                                # Get the Visible of each Field
                                print("Visible: " + str(field.get_visible()))

                            if field.get_length() is not None:
                                # Get the Length of each Field
                                print("Length: " + str(field.get_length()))

                            if field.get_decimal_place() is not None:
                                # Get the DecimalPlace of each Field
                                print("DecimalPlace: " +
                                      str(field.get_decimal_place()))

                            # Get the ViewType of each Field
                            view_type = field.get_view_type()

                            if view_type is not None:
                                # Get the View of the ViewType
                                print("View: " + str(view_type.get_view()))

                                # Get the Edit of the ViewType
                                print("Edit: " + str(view_type.get_edit()))

                                # Get the Create of the ViewType
                                print("Create: " + str(view_type.get_create()))

                                # Get the QuickCreate of the ViewType
                                print("QuickCreate: " +
                                      str(view_type.get_quick_create()))

                            pick_list_values = field.get_pick_list_values()

                            if pick_list_values is not None:
                                for pick_list_value in pick_list_values:

                                   Field.print_pick_list_value(pick_list_value)

                            multi_module_lookup = field.get_multi_module_lookup()

                            if multi_module_lookup is not None:
                                print("Lookup name : " +
                                      str(multi_module_lookup.get_id()))
                                print("Lookup Id: " +
                                      str(multi_module_lookup.get_name()))

                                module = multi_module_lookup.get_module()
                                if module is not None:
                                    print("module Id: "+module.get_id())
                                    print("module Id: " +
                                          module.get_api_name())

                            multi_select_lookup = field.get_multiselectlookup()

                            # Check if multiSelectLookup is not None
                            if multi_select_lookup is not None:
                                # Get the DisplayLabel of the MultiSelectLookup
                                print(
                                    "DisplayLabel: " + str(multi_select_lookup.get_display_label()))

                                # Get the LinkingModule of the MultiSelectLookup
                                print(
                                    "LinkingModule: " + str(multi_select_lookup.get_linking_module()))

                                # Get the LookupApiname of the MultiSelectLookup
                                print(
                                    "LookupApiname: " + str(multi_select_lookup.get_lookup_apiname()))

                                # Get the APIName of the MultiSelectLookup
                                print("APIName: " +
                                      str(multi_select_lookup.get_api_name()))

                                # Get the ConnectedlookupApiname of the MultiSelectLookup
                                print(
                                    "ConnectedlookupApiname: " + str(multi_select_lookup.get_connectedlookup_apiname()))

                                # Get the ID of the MultiSelectLookup
                                print("ID: " + str(multi_select_lookup.get_id()))

                               # Get the Connected Module of the MultiSelectLookup
                                print(
                                    "Connected Module: " + str(multi_select_lookup.get_connected_module()))
                            multi_user_lookup = field.get_multiuserlookup()

                            # Check if MultiUserLookup is not None
                            if multi_user_lookup is not None:
                                # Get the DisplayLabel of the MultiUserLookup
                                print("DisplayLabel: " +
                                      str(multi_user_lookup.get_display_label()))

                                # Get the LinkingModule of the MultiUserLookup
                                print("LinkingModule: " +
                                      str(multi_user_lookup.get_linking_module()))

                                # Get the LookupApiname of the MultiUserLookup
                                print("LookupApiname: " +
                                      str(multi_user_lookup.get_lookup_apiname()))

                                # Get the APIName of the MultiUserLookup
                                print("APIName: " +
                                      str(multi_user_lookup.get_api_name()))

                                # Get the ConnectedlookupApiname of the MultiUserLookup
                                print(
                                    "ConnectedlookupApiname: " + str(multi_user_lookup.get_connectedlookup_apiname()))

                                # Get the ID of the MultiUserLookup
                                print("ID: " + str(multi_user_lookup.get_id()))

                               # Get the Connected Module of the MultiUserLookup
                                print("Connected Module: " +
                                      str(multi_user_lookup.get_connected_module()))
                            lookup = field.get_lookup()
                            if lookup.get_nil() is not None:
                                layout = lookup.get_layout()
                                if layout is not None:
                                    #Get the ID of the Layout
                                    print("\n Field ModuleLookup Layout ID: ")
                                    print(layout.get_id())
                                    #Get the Name of the Layout
                                    print("\n Field ModuleLookup Layout Name: ")
                                    print(layout.get_name())

                                formula = field.get_formula()
                                # Check if formula is not null
                                if formula is not None:
                                    # Get the ReturnType of the Formula
                                    print("\nField Formula ReturnType : ")
                                    print(formula.get_return_type())
                                    # Get the Expression of the Formula
                                    if formula.get_expression() is not None:
                                        print("\nField Formula Expression : ")
                                        print(formula.get_expression())

                                if field.get_decimal_place() is not None:
                                    # Get the DecimalPlace of each Field
                                    print("\nField DecimalPlace: ")
                                    print(field.get_decimal_place())

                                #Get the DisplayLabel of the Module
                                print("Field ModuleLookup DisplayLabel: ")
                                print(lookup.get_display_label())

                                #Get the APIName of the Module
                                print("Field ModuleLookup APIName: ")
                                print(lookup.get_api_name())

                                #Get the Module of the Module
                                print("Field ModuleLookup Module: ")

                                print(lookup.get_module1())
                                print("Field ModuleLookup ID: ")
                                print(lookup.get_id())

                            auto_number = field.get_auto_number()
                            # Check if ConvertMapping is not None
                            if field.get_convert_mapping() is not None:
                                # Get the ConvertMapping dict
                                for key, value in field.get_convert_mapping().items():
                                    print(key + " : " + str(value))
                            profiles = field.get_profiles()
                            for profile in profiles:

                                print("\n Field Profile PermissionType: ")
                                print(profile.get_permission_type())
                                print("\n Field Profile Name: ")
                                print(profile.get_name())
                                print("\n Field Profile ID: ")
                                print(profile.get_id())

                            # Check if autoNumber is not None
                            if auto_number is not None:
                                # Get the Prefix of the AutoNumber
                                print('Prefix: ' + str(auto_number.get_prefix()))

                                # Get the Suffix of the AutoNumber
                                print('Suffix: ' + str(auto_number.get_suffix()))

                                if auto_number.get_start_number() is not None:
                                    # Get the StartNumber of the AutoNumber
                                    print('Start Number: ' +
                                          str(auto_number.get_start_number()))

                # Check if the request returned an exception
                elif isinstance(response_object, APIException):

                    # Get the Status
                    print("Status: " + response_object.get_status().get_value())

                    # Get the Code
                    print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = response_object.get_details()

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def get_field(module_api_name, field_id):
        """
        This method is used to get metadata about a single field of a module with fieldID and print the response.
        :param module_api_name: The API Name of the field's module
        :param field_id: The ID of the field to be obtained
        """

        """
        example
        module_api_name = "Leads"
        field_id = 34096432293043
        """

        # Get instance of FieldsOperations Class that takes module_api_name as parameter
        fields_operations = FieldsOperations(module_api_name)

        # Call get_field method which takes field_id as parameter
        response = fields_operations.get_field(field_id)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code()
                      == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ResponseWrapper instance is received
                if isinstance(response_object, ResponseWrapper):

                    fields = response_object.get_fields()
                    for field in fields:
                        # Get the Webhook of each Field
                        print("Webhook: " + str(field.get_webhook()))

                        # Get the JsonType of each Field
                        print("JsonType: " + str(field.get_json_type()))

                        # Get the DisplayLabel of each Field
                        print("DisplayLabel: " + field.get_display_label())

                        # Get the SystemMandatory of each Field
                        print("SystemMandatory: " +
                              str(field.get_system_mandatory()))

                        print("\n Field is Private :")
                        print(field.get_private())
                        print("\n Field is UiType :")
                        print(field.get_ui_type())
                        print("\n Field  PickListValuesSortedLexically :")
                        print(field.get_pick_list_values_sorted_lexically())

                        # Get the DataType of each Field
                        print("DataType: " + field.get_data_type())

                        # Get the ColumnName of each Field
                        print("ColumnName: " + str(field.get_column_name()))

                        # Get the PersonalityName of each Field
                        print("PersonalityName: " +
                              str(field.get_personality_name()))

                        # Get the ID of each Field
                        print("ID: " + str(field.get_id()))

                        # Get the Sortable of each Field
                        print("Sortable: " + str(field.get_sortable()))

                        # Get the TransitionSequence of each Field
                        print("TransitionSequence: " +
                              str(field.get_transition_sequence()))

                        multi_module_lookup = field.get_multi_module_lookup()
                        if multi_module_lookup is not None:
                            print("Lookup name : " +
                                  str(multi_module_lookup.get_id()))
                            print("Lookup Id: " +
                                  str(multi_module_lookup.get_name()))

                            module = multi_module_lookup.get_module()
                            if module is not None:
                                print("module Id: " + module.get_id())
                                print("module Id: " + module.get_api_name())

                        if field.get_mandatory() is not None:
                            # Get the Mandatory of each Field
                            print("Mandatory: " + str(field.get_mandatory()))
                        if field.get_external() is not None:
                            external = field.get_external()
                            # Get the External Show of each Field
                            print("External Show: " + str(external.get_show()))
                            # Get the External Type of each Field
                            print("External Type: " + str(external.get_type()))
                            # Get the External Type of each Field
                            print("External Type: " +
                                  str(external.get_allow_multiple_config()))
                        if field.get_unique() is not None:
                            # Get the Mandatory of each Field
                            print("Mandatory: " +
                                  str(field.get_unique().get_casesensitive()))
                        if field.get_history_tracking() is not None:
                            # Get the HistoryTracking of each Field
                            history_tracking = field.get_history_tracking()
                            module = history_tracking.get_module()
                            if module is not None:
                                module_layout = module.get_layout()
                                if module_layout is not None:
                                    print("Module layout id: " +
                                          str(module_layout.get_id()))
                                    print("Module display label: " +
                                          str(module.get_api_name()))
                                    print("Module api name: " +
                                          str(module.get_id()))
                                    print("Module module: " +
                                          str(module.get_module()))
                                    print("Module module name: " +
                                          str(module.get_module_name()))

                            duration_configured = history_tracking.get_duration_configured_field()
                            if duration_configured is not None:
                                print(
                                    "historytracking duration configured field: " + str(duration_configured.get_id()))
                        # Get the obtained Layout instance
                        layout = field.get_layouts()

                        # Check if layout is not null
                        if layout is not None:
                            # Get the ID of the Layout
                            print("Layout ID: " + str(layout.get_id()))

                            # Get the Name of the Layout
                            print("Layout Name: " + str(layout.get_name()))

                        # Get the APIName of each Field
                        print("APIName : " + str(field.get_api_name()))

                        # Get the Content of each Field
                        print("Content: " + str(field.get_content()))

                        # Get the Message of each Field
                        print("Message :" + str(field.get_message()))

                        # Get the obtained Crypt instance
                        crypt = field.get_crypt()

                        if crypt is not None:
                            print("Crypt Details")

                            # Get the Crypt Mode
                            print("Mode: " + crypt.get_mode())

                            # Get the Crypt Column
                            print("Column: ")
                            print(crypt.get_column())

                            # Get the Crypt Table
                            print("Table: ")
                            print(crypt.get_table())

                            # Get the Crypt Status
                            print("Status: " + str(crypt.get_status()))

                            print("\n Crypt Notify:")
                            print(crypt.get_notify())

                            enc_fld_ids = crypt.get_encfldids()
                            if enc_fld_ids is not None:
                                print("\nEncFldIds : ")
                                for enc_fld_id in enc_fld_ids:
                                    print(enc_fld_id)

                        # Get the FieldLabel of each Field
                        print("FieldLabel: " + str(field.get_field_label()))

                        tool_tip = field.get_tooltip()

                        if tool_tip is not None:
                            # Get the Name of the ToolTip
                            print("ToolTip Name: " + tool_tip.get_name())

                            # Get the Value of the ToolTip
                            print("ToolTip Value: " + tool_tip.get_value())

                        currency = field.get_currency()

                        if currency is not None:
                            # Get the RoundingOption of the Currency
                            print("Currency RoundingOption: " +
                                  str(currency.get_rounding_option()))

                            # Get the Precision of the Currency
                            print("Currency Precision: " +
                                  str(currency.get_precision()))

                        # Get the CreatedSource of each Field
                        print("CreatedSource: " +
                              str(field.get_created_source()))

                        if field.get_display_type() is not None:
                            # Get the DisplayType of the Field
                            print("Field DisplayType: " +
                                  str(field.get_display_type()))

                        # Get the FieldReadOnly of each Field
                        print("FieldReadOnly: " +
                              str(field.get_field_read_only()))
                        # Get the Filterable of each Field
                        print("Filterable: " + str(field.get_filterable()))

                        # Get the Criteria of each Field
                        criteria = field.get_criteria()

                        if criteria is not None:
                            Field.print_criteria(criteria)

                        # Get the Related Details of each Field
                        related_details = field.get_related_details()

                        if related_details is not None:
                            # Get the display label of related detail
                            if related_details.get_display_label() is not None:
                                print("RelatedDetails Display Label: " +
                                      related_details.get_display_label())

                            # Get the API Name of related detail
                            print("Related Details API Name: " +
                                  str(related_details.get_api_name()))

                            # Get the module of related detail
                            if related_details.get_module() is not None:
                                module = related_details.get_module()

                                # Get the layout of the module
                                if module.get_layout() is not None:
                                    layout = module.get_layout()

                                    print(
                                        "Related Details Module Layout ID: " + layout.get_id())

                                    print(
                                        "Related Details Module Layout Name: " + layout.get_name())

                                # Get the display label of the module
                                if module.get_display_label() is not None:
                                    print(
                                        "Related Details Module Display Label: " + module.get_display_label())

                                # Get the Module API Name of the Related detail module
                                print("Related Details Module API Name: " +
                                      str(module.get_api_name()))

                                # Get the Module of the Related detail module
                                print("Related Details Module: " +
                                      str(module.get_module()))

                                # Get the Module Name of the Related detail module
                                print("Related Details Module Name: " +
                                      module.get_module_name())

                            # Get the ID of the Related detail
                            print("Related Details ID: " +
                                  str(related_details.get_id()))

                            # Get the Type of the Related detail
                            print("Related Details Type: " +
                                  str(related_details.get_type()))

                        # Get the ReadOnly of each Field
                        if field.get_read_only() is not None:
                            print("ReadOnly: " + str(field.get_read_only()))

                        # Get the obtained AssociationDetails instance
                        association_details = field.get_association_details()

                        if association_details is not None:

                            # Get the obtained LookupField instance
                            lookup_field = association_details.get_lookup_field()

                            if lookup_field is not None:
                                # Get the ID of the LookupField
                                print(
                                    "AssociationDetails LookupField ID: " + lookup_field.get_id())

                                # Get the Name of the LookupField
                                print(
                                    'AssociationDetails LookupField Name: ' + lookup_field.get_name())

                            # Get the obtained LookupField instance
                            related_field = association_details.get_related_field()

                            if related_field is not None:
                                # Get the ID of the RelatedField
                                print(
                                    "AssociationDetails RelatedField ID: " + related_field.get_id())

                                # Get the Name of the RelatedField
                                print(
                                    'AssociationDetails RelatedField Name: ' + related_field.get_name())

                        if field.get_quick_sequence_number() is not None:
                            # Get the QuickSequenceNumber of each Field
                            print('QuickSequenceNumber: ' +
                                  str(field.get_quick_sequence_number()))

                        # Get the DisplayLabel of each Field
                        print("DisplayLabel: " + field.get_display_label())

                        if field.get_custom_field() is not None:
                            # Get if the Field is a CustomField
                            print("CustomField: " +
                                  str(field.get_custom_field()))

                        if field.get_visible() is not None:
                            # Get the Visible of each Field
                            print("Visible: " + str(field.get_visible()))

                        if field.get_length() is not None:
                            # Get the Length of each Field
                            print("Length: " + str(field.get_length()))

                        if field.get_decimal_place() is not None:
                            # Get the DecimalPlace of each Field
                            print("DecimalPlace: " +
                                  str(field.get_decimal_place()))
                        multi_user_lookup = field.get_multiuserlookup()

                        # Check if MultiUserLookup is not None
                        if multi_user_lookup is not None:
                            # Get the DisplayLabel of the MultiUserLookup
                            print("DisplayLabel: " +
                                  str(multi_user_lookup.get_display_label()))

                            # Get the LinkingModule of the MultiUserLookup
                            print("LinkingModule: " +
                                  str(multi_user_lookup.get_linking_module()))

                            # Get the LookupApiname of the MultiUserLookup
                            print("LookupApiname: " +
                                  str(multi_user_lookup.get_lookup_apiname()))

                            # Get the APIName of the MultiUserLookup
                            print("APIName: " +
                                  str(multi_user_lookup.get_api_name()))

                            # Get the ConnectedlookupApiname of the MultiUserLookup
                            print("ConnectedlookupApiname: " +
                                  str(multi_user_lookup.get_connectedlookup_apiname()))

                            # Get the ID of the MultiUserLookup
                            print("ID: " + str(multi_user_lookup.get_id()))

                           # Get the Connected Module of the MultiUserLookup
                            print("Connected Module: " +
                                  str(multi_user_lookup.get_connected_module()))

                        # Get the ViewType of each Field
                        view_type = field.get_view_type()

                        if view_type is not None:
                            # Get the View of the ViewType
                            print("View: " + str(view_type.get_view()))

                            # Get the Edit of the ViewType
                            print("Edit: " + str(view_type.get_edit()))

                            # Get the Create of the ViewType
                            print("Create: " + str(view_type.get_create()))

                            # Get the QuickCreate of the ViewType
                            print("QuickCreate: " +
                                  str(view_type.get_quick_create()))

                        pick_list_values = field.get_pick_list_values()

                        if pick_list_values is not None:
                            for pick_list_value in pick_list_values:

                               Field.print_pick_list_value(pick_list_value)

                        multi_select_lookup = field.get_multiselectlookup()

                        # Check if multiSelectLookup is not None
                        if multi_select_lookup is not None:
                            # Get the DisplayLabel of the MultiSelectLookup
                            print("DisplayLabel: " +
                                  str(multi_select_lookup.get_display_label()))

                            # Get the LinkingModule of the MultiSelectLookup
                            print("LinkingModule: " +
                                  str(multi_select_lookup.get_linking_module()))

                            # Get the LookupApiname of the MultiSelectLookup
                            print("LookupApiname: " +
                                  str(multi_select_lookup.get_lookup_apiname()))

                            # Get the APIName of the MultiSelectLookup
                            print("APIName: " +
                                  str(multi_select_lookup.get_api_name()))

                            # Get the ConnectedlookupApiname of the MultiSelectLookup
                            print("ConnectedlookupApiname: " +
                                  str(multi_select_lookup.get_connectedlookup_apiname()))

                            # Get the ID of the MultiSelectLookup
                            print("ID: " + str(multi_select_lookup.get_id()))

                           # Get the Connected Module of the MultiSelectLookup
                            print("Connected Module: " +
                                  str(multi_select_lookup.get_connected_module()))

                        lookup = field.get_lookup()
                        if lookup is not None:
                            layout = lookup.get_layout()
                            if layout is not None:
                                #Get the ID of the Layout
                                print("\n Field ModuleLookup Layout ID: ")
                                print(layout.get_id())
                                #Get the Name of the Layout
                                print("\n Field ModuleLookup Layout Name: ")
                                print(layout.get_name())

                            formula = field.get_formula()
                            # Check if formula is not null
                            if formula is not None:
                                # Get the ReturnType of the Formula
                                print("\nField Formula ReturnType : ")
                                print(formula.get_return_type())
                                # Get the Expression of the Formula
                                if formula.get_expression() is not None:
                                    print("\nField Formula Expression : ")
                                    print(formula.get_expression())

                            if field.get_decimal_place() is not None:
                                # Get the DecimalPlace of each Field
                                print("\nField DecimalPlace: ")
                                print(field.get_decimal_place())

                            #Get the DisplayLabel of the Module
                            print("Field ModuleLookup DisplayLabel: ")
                            print(lookup.get_display_label())

                            #Get the APIName of the Module
                            print("Field ModuleLookup APIName: ")
                            print(lookup.get_api_name())

                            #Get the Module of the Module
                            print("Field ModuleLookup Module: ")

                            print(lookup.get_module())
                            print("Field ModuleLookup ID: ")
                            print(lookup.get_id())

                        auto_number = field.get_auto_number()
                        # Check if ConvertMapping is not None
                        if field.get_convert_mapping() is not None:
                            # Get the ConvertMapping dict
                            for key, value in field.get_convert_mapping().items():
                                print(key + " : " + str(value))
                        profiles = field.get_profiles()
                        for profile in profiles:

                            print("\n Field Profile PermissionType: ")
                            print(profile.get_permission_type())
                            print("\n Field Profile Name: ")
                            print(profile.get_name())
                            print("\n Field Profile ID: ")
                            print(profile.get_id())

                        # Check if autoNumber is not None
                        if auto_number is not None:
                            # Get the Prefix of the AutoNumber
                            print('Prefix: ' + str(auto_number.get_prefix()))

                            # Get the Suffix of the AutoNumber
                            print('Suffix: ' + str(auto_number.get_suffix()))

                            if auto_number.get_start_number() is not None:
                                # Get the StartNumber of the AutoNumber
                                print('Start Number: ' +
                                      str(auto_number.get_start_number()))

                # Check if the request returned an exception
                elif isinstance(response_object, APIException):

                    # Get the Status
                    print("Status: " + response_object.get_status().get_value())

                    # Get the Code
                    print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = response_object.get_details()

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def print_pick_list_value(pick_list_value):
        # Get the DisplayValue of each PickListValue
        print("\n DisplayValue:")
        print(pick_list_value.get_display_value())
        # Get the SequenceNumber of each PickListValue
        print("\n SequenceNumber:")
        print(pick_list_value.get_sequence_number())
        # Get the ExpectedDataType of each PickListValue
        print("\n ExpectedDataType:")
        print(pick_list_value.get_expected_data_type())
        # Get the ActualValue of each PickListValue
        print("\n ActualValue :")
        print(pick_list_value.get_actual_value)
        if pick_list_value.get_maps() is not None:
            for map in pick_list_value.get_maps():
                # Get each value from the map
                print("\n")
                print(map)
                pick_list_values = map.get_pick_list_values
                if pick_list_values is not None:
                    for plv in pick_list_values:
                        Field.print_pick_list_value(plv)

        # Get the SysRefName of each PickListValues
        print("\nField PickListValue SysRefName: ")
        print(pick_list_value.get_sys_ref_name())
        # Get the Type of each PickListValues
        print("\nField PickListValue Type: ")
        print(pick_list_value.get_type())
