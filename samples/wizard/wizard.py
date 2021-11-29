from zcrmsdk.src.com.zoho.crm.api.wizards import *
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class Wizard(object):

    @staticmethod
    def get_wizards():
        """
        This method is used to get a wizard' details with ID and print(the response.

        """
        # Get instance of WizardOperations Class

        wizard_operations = WizardsOperations()

        # Possible parameters for Get Wizard Operation

        # Call get_wizard method that takes ParameterMap instance as parameter
        response = wizard_operations.get_wizards()

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ResponseWrapper instance is received
                if isinstance(response_object, ResponseWrapper):
                    wizard_list = response_object.get_wizards()
                    for wizard in wizard_list:

                        # Get the ID of each Wizard
                        print(" ID " + str(wizard.get_id()))

                        # Get the name of each Wizard
                        print("Name: " + str(wizard.get_name()))

                        # Get the Modified Time of each Wizard
                        print("Modified Time: " + str(wizard.get_modified_time()))

                        # Get the Created Time of each Wizard
                        print("Created Time: " + str(wizard.get_created_time()))

                        # Get the Draft of each Wizard
                        print("Draft: " + str(wizard.get_draft()))

                        # Get the active of each Wizard
                        print("active: " + str(wizard.get_active()))

                        created_by = wizard.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Created By - ID: " + str(created_by.get_id()))

                             # Get the email of the created_by User
                            print("Created By - email: " + str(created_by.get_email()))

                        # Check if parent_wizard is not None
                        parent_wizard = wizard.get_parent_wizard()
                        if parent_wizard is not None:
                            # Get the ID of the folder
                            print("Wizard parent_wizard ID: " + parent_wizard.get_parent_wizard())

                            # Get the Name of the folder
                            print("Wizard parent_wizard Name:" + str(parent_wizard.get_id()))

                         # get module 
                        module = wizard.get_module()
                        if module is not None:
                            # Get the API Name of the module 
                            print("Module - API Name: " + module.get_api_name())

                            # Get the ID of the module
                            print("Module - ID: " + str(module.get_id()))

                        # get profiles 
                        profiles = wizard.get_profiles()

                        for profile in profiles:
                            print("Wizard Profile ID: " + str(profile.get_id()))
                            print("Wizard Profile Name: " + profile.get_name())

                        # Get the modified_by User instance of each Wizard
                        modified_by = wizard.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Modified By - ID: " + str(modified_by.get_id()))

                             # Get the email of the created_by User
                            print("Modified By - ID: " + str(modified_by.get_email()))
                        
                        # Get the Containers  of each Wizard

                        containers = wizard.get_containers()

                        if containers is not None:
                            for container in containers:
                                print("\n Container Id: " + str(container.get_id()))
                                # Get the Layout
                                layout = container.get_layout()
                                if layout is not None:
                                    print("\n Layout id" + str(layout.get_id()))
                                    print("\n Layout name"+layout.get_name())

                                # Get the Chart Data
                                chart_data = container.get_chart_data()
                                if chart_data is not None:
                                    # Get the nodes
                                    nodes = chart_data.get_nodes()
                                    for node in nodes:
                                        print("\n Chart Data Node poistion y: ")
                                        print(node.get_pos_y())
                                        print("\n Chart Data Node poistion x: ")
                                        print(node.get_pos_x())
                                        print("\n Chart Data Node start node : ")
                                        print(node.get_start_node())
                                        node_screen = node.get_screen()
                                        if node_screen is not None:
                                            print("\n Screen id")
                                            print(node_screen.get_id())
                                            print("\n Screen display label")
                                            print(node_screen.get_display_label())


                                    # Get the connections
                                    connections = chart_data.get_connections()
                                    for connection in connections:
                                        # Get the target screen
                                        connection_screen = connection.get_target_screen()
                                        if connection_screen is not None:
                                            print("\n connection_screen id")
                                            print(connection_screen.get_id())
                                            print("\n connection_screen display label")
                                            print(connection_screen.get_display_label())

                                        # Get the connection source button
                                        connection_button = connection_screen.get_source_button()
                                        if connection_button is not None:
                                            print("\n connection_button id")
                                            print(connection_button.get_id())
                                            print("\n connection_button display label")
                                            print(connection_button.get_display_label())



                                # Get chart data
                                chart_data = container.get_chart_data()
                                if chart_data is not None:
                                    print("\n Chart Data Canvas width: ")
                                    print(chart_data.get_canvas_width())
                                    print("\n Chart Data Canvas height: ")
                                    print(chart_data.get_canvas_height())

                                # Get container screens
                                screens = container.get_screens()
                                if screens is not None:
                                    for screen in screens:
                                        print("\n screen id")
                                        print(screen.get_id())
                                        print("\n screen display label")
                                        print(screen.get_display_label())
                                        # Get container screens segments
                                        segments = screen.get_segments()
                                        for segment in segments:
                                            print("\n segment id")
                                            print(segment.get_id())
                                            print("\n segment display label")
                                            print(segment.get_display_label())
                                            print("\n segment  sequence number")
                                            print(segment.get_sequence_number())
                                            print("\n segment type")
                                            print(segment.get_type())
                                            print("\n segment column count")
                                            print(segment.get_column_count())
                                            fields = segment.get_fields()
                                            for field in fields:
                                                print("\n field id")
                                                print(field.get_id())
                                                print("\n field api_name")
                                                print(field.get_api_name())

                                            buttons = segment.get_buttons()
                                            for button in buttons:
                                                criteria = button.get_criteria()
                                                if criteria is not None:
                                                    Wizard.print_criteria(criteria)

                                                target_screen = button.get_target_screen()
                                                if target_screen is not None:
                                                    print("\n target screen id")
                                                    print(target_screen.get_id())
                                                    print("\n target screen display label")
                                                    print(target_screen.get_display_label())

                                                print("\n  Button display label:")
                                                print(button.get_display_label())
                                                print("\n  Button id:")
                                                print(button.get_id())
                                                print("\n  Button type:")
                                                print(button.get_type())
                                                print("\n  Button background color:")
                                                print(button.get_background_color())
                                                print("\n  Button sequence number:")
                                                print(button.get_sequence_number())
                                                print("\n  Button color:")
                                                print(button.get_color())
                                                print("\n  Button type:")
                                                print(button.get_type())
                                                print("\n  Button shape:")
                                                print(button.get_shape())

                # Check if the request returned an exception
                elif isinstance(response_object, APIException):
                    # Get the Status
                    print("Status: " + response_object.get_status().get_value())

                    # Get the Code
                    print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = response_object.get_details()

                    if details is not None:
                        if details is not None:
                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def get_wizard(wizard_id):
        """
        This method is used to get  wizard' details with ID and print(the response.

        """


        # Get instance of WizardOperations Class
        wizard_operations = WizardsOperations()

        # Possible parameters for Get Wizard Operation
        param_instance = ParameterMap()

        param_instance.add(GetWizardbyIDParam.layout_id, "34770610091055")

        # Call get_wizard method that takes ParameterMap instance as parameter
        response = wizard_operations.get_wizard_by_id(wizard_id,param_instance)

        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ResponseWrapper instance is received
                if isinstance(response_object, ResponseWrapper):
                    wizard_list = response_object.get_wizards()
                    for wizard in wizard_list:

                        # Get the ID of each Wizard
                        print(" ID " + str(wizard.get_id()))

                        # Get the name of each Wizard
                        print("Name: " + str(wizard.get_name()))

                        # Get the Modified Time of each Wizard
                        print("Modified Time: " + str(wizard.get_modified_time()))

                        # Get the Created Time of each Wizard
                        print("Created Time: " + str(wizard.get_created_time()))

                        # Get the Draft of each Wizard
                        print("Draft: " + str(wizard.get_draft()))

                        # Get the active of each Wizard
                        print("active: " + str(wizard.get_active()))

                        created_by = wizard.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Created By - ID: " + str(created_by.get_id()))

                             # Get the email of the created_by User
                            print("Created By - email: " + str(created_by.get_email()))

                        # Check if parent_wizard is not None
                        parent_wizard = wizard.get_parent_wizard()
                        if parent_wizard is not None:
                            # Get the ID of the folder
                            print("Wizard parent_wizard ID: " + parent_wizard.get_parent_wizard())

                            # Get the Name of the folder
                            print("Wizard parent_wizard Name:" + str(parent_wizard.get_id()))

                         # get module 
                        module = wizard.get_module()
                        if module is not None:
                            # Get the API Name of the module 
                            print("Module - API Name: " + module.get_api_name())

                            # Get the ID of the module
                            print("Module - ID: " + str(module.get_id()))

                        # get profiles 
                        profiles = wizard.get_profiles()

                        for profile in profiles:
                            print("Wizard Profile ID: " + str(profile.get_id))
                            print("Wizard Profile Name: " + profile.get_name())

                        # Get the modified_by User instance of each Wizard
                        modified_by = wizard.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Modified By - ID: " + str(modified_by.get_id()))

                             # Get the email of the created_by User
                            print("Modified By - ID: " + str(modified_by.get_email()))
                        
                        # Get the Containers  of each Wizard

                        containers = wizard.get_containers()
                        if containers is not None:
                            for container in containers:
                                # Get the Container ID
                                print("\n Container Id: " + str(container.get_id()))
                                # Get the Layout
                                layout = container.get_layout()
                                if layout is not None:
                                    print("\n Layout id" + str(layout.get_id()))
                                    print("\n Layout name" + layout.get_name())

                                # Get the Chart Data
                                chart_data = container.get_chart_data()
                                if chart_data is not None:
                                    # Get the nodes
                                    nodes = chart_data.get_nodes()
                                    for node in nodes:
                                        print("\n Chart Data Node poistion y: ")
                                        print(node.get_pos_y())
                                        print("\n Chart Data Node poistion x: ")
                                        print(node.get_pos_x())
                                        print("\n Chart Data Node start node : ")
                                        print(node.get_start_node())
                                        node_screen = node.get_screen()
                                        if node_screen is not None:
                                            print("\n Screen id")
                                            print(node_screen.get_id())
                                            print("\n Screen display label")
                                            print(node_screen.get_display_label())


                                    # Get the connections
                                    connections = chart_data.get_connections()
                                    if connections is not None:
                                        for connection in connections:
                                            # Get the target screen
                                            connection_screen = connection.get_target_screen()
                                            if connection_screen is not None:
                                                print("\n connection_screen id")
                                                print(connection_screen.get_id())
                                                print("\n connection_screen display label")
                                                print(connection_screen.get_display_label())

                                            # Get the connection source button
                                            connection_button = connection_screen.get_source_button()
                                            if connection_button is not None:
                                                print("\n connection_button id")
                                                print(connection_button.get_id())
                                                print("\n connection_button display label")
                                                print(connection_button.get_display_label())

                                # Get chart data
                                chart_data = container.get_chart_data()
                                if chart_data is not None:
                                    print("\n Chart Data Canvas width: ")
                                    print(chart_data.get_canvas_width())
                                    print("\n Chart Data Canvas height: ")
                                    print(chart_data.get_canvas_height())

                            # Get container screens
                            screens = container.get_screens()
                            if screens is not None:
                                for screen in screens:
                                    print("\n screen id")
                                    print(screen.get_id())
                                    print("\n screen display label")
                                    print(screen.get_display_label())
                                    # Get container screens segments
                                    segments = screen.get_segments()
                                    for segment in segments:
                                        print("\n segment id")
                                        print(segment.get_id())
                                        print("\n segment display label")
                                        print(segment.get_display_label())
                                        print("\n segment  sequence number")
                                        print(segment.get_sequence_number())
                                        print("\n segment type")
                                        print(segment.get_type())
                                        print("\n segment column count")
                                        print(segment.get_column_count())
                                        fields = segment.get_fields()
                                        if fields is not None:
                                            for field in fields:
                                                print("\n field id")
                                                print(field.get_id())
                                                print("\n field api_name")
                                                print(field.get_api_name())

                                        buttons = segment.get_buttons()
                                        if buttons is not None:
                                            for button in buttons:
                                                criteria = button.get_criteria()
                                                if criteria is not None:
                                                    Wizard.print_criteria(criteria)

                                                target_screen = button.get_target_screen()
                                                if target_screen is not None:
                                                    print("\n target screen id")
                                                    print(target_screen.get_id())
                                                    print("\n target screen display label")
                                                    print(target_screen.get_display_label())

                                                print("\n  Button display label:")
                                                print(button.get_display_label())
                                                print("\n  Button id:")
                                                print(button.get_id())
                                                print("\n  Button type:")
                                                print(button.get_type())
                                                print("\n  Button background color:")
                                                print(button.get_background_color())
                                                print("\n  Button sequence number:")
                                                print(button.get_sequence_number())
                                                print("\n  Button color:")
                                                print(button.get_color())
                                                print("\n  Button type:")
                                                print(button.get_type())
                                                print("\n  Button shape:")
                                                print(button.get_shape())

                elif isinstance(response_object, APIException):
                    # Get the Status
                    print("Status: " + response_object.get_status().get_value())

                    # Get the Code
                    print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = response_object.get_details()

                    if details is not None:
                        if details is not None:
                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())


    @staticmethod
    def print_criteria(criteria):

        if criteria.get_comparator() is not None:
            # Get the Comparator of the Criteria
            print('Field Criteria Comparator: ' + criteria.get_comparator().get_value())

        if criteria.get_field() is not None:
            # Get the Field of the Criteria
            print('Field Criteria Field: ' + criteria.get_field())

        if criteria.get_value() is not None:
            # Get the Value of the Criteria
            print('Field Criteria Value: ' + str(criteria.get_value()))

        # Get the List of Criteria instance of each Criteria
        criteria_group = criteria.get_group()

        if criteria_group is not None:
            for each_criteria in criteria_group:
                Wizard.print_criteria(each_criteria)

        if criteria.get_group_operator() is not None:
            # Get the Group Operator of the Criteria
            print('Field Criteria Group Operator: ' + criteria.get_group_operator().get_value())