from zcrmsdk.src.com.zoho.crm.api.assignment_rules import *
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class AssignmentRules(object):

    @staticmethod
    def get_assignment_rules():
        """
        This method is used to get a assignment_rules' details with ID and print the response.

        """
        # Get instance of AssignmentRulesOperations Class

        assignment_rules_operations = AssignmentRulesOperations()

        # Possible parameters for Get AssignmentRules Operation

        # Call get_assignment_rules method that takes ParameterMap instance as parameter
        response = assignment_rules_operations.get_assignment_rules()

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
                    assignment_rules_list = response_object.get_assignment_rules()

                    for assignment_rule in assignment_rules_list:

                        # Get the ID of each Assignment Rule
                        print(" ID " + str(assignment_rule.get_id()))

                        # Get the name of each Assignment Rule
                        print("Name: " + str(assignment_rule.get_name()))

                        # Get the description of each Assignment Rule
                        print("description: " +
                              str(assignment_rule.get_description()))

                        # Get the Modified Time of each Assignment Rule
                        print("Modified Time: " +
                              str(assignment_rule.get_modified_time()))

                        # Get the Created Time of each Assignment Rule
                        print("Created Time: " +
                              str(assignment_rule.get_created_time()))

                        # Get the modified_by User instance of each currency
                        modified_by = assignment_rule.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Modified By - Name: " +
                                  modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Modified By - ID: " +
                                  str(modified_by.get_id()))

                            # Get the email of the created_by User
                            print("Modified By - ID: " +
                                  str(modified_by.get_email()))

                        created_by = assignment_rule.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Created By - Name: " +
                                  created_by.get_name())

                            # Get the ID of the created_by User
                            print("Created By - ID: " +
                                  str(created_by.get_id()))

                            # Get the email of the created_by User
                            print("Created By - email: " +
                                  str(created_by.get_email()))

                        # Check if DefaultUser is not None
                        default_assignee = assignment_rule.get_default_assignee()
                        if default_assignee is not None:
                            # Get the Name of the default_assignee User
                            print("Created By - Name: " +
                                  default_assignee.get_name())

                            # Get the ID of the default_assignee User
                            print("Created By - ID: " +
                                  str(default_assignee.get_id()))

                         # Check if Module is not None
                        module = assignment_rule.get_module()
                        if module is not None:
                            # Get the API Name of the module User
                            print("Module - API Name: " +
                                  module.get_api_name())

                            # Get the ID of the default_assignee User
                            print("Module - ID: " + str(module.get_id()))

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
    def get_assignment_rule(rule_id):
        """
        This method is used to get  assignment_rules' details with ID and print the response.

        """

        # Get instance of AssignmentRulesOperations Class
        assignment_rules_operations = AssignmentRulesOperations()

        # Possible parameters for Get AssignmentRules Operation
        param_instance = ParameterMap()

        param_instance.add(GetAssignmentRuleParam.module, "Leads")

        # Call get_assignment_rules method that takes ParameterMap instance as parameter
        response = assignment_rules_operations.get_assignment_rule(
            rule_id, param_instance)

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
                    assignment_rules_list = response_object.get_assignment_rules()

                    for assignment_rule in assignment_rules_list:

                        # Get the ID of each Assignment Rule
                        print(" ID " + str(assignment_rule.get_id()))

                        # Get the name of each Assignment Rule
                        print("Name: " + str(assignment_rule.get_name()))

                        # Get the description of each Assignment Rule
                        print("description: " +
                              str(assignment_rule.get_description()))

                        # Get the Modified Time of each Assignment Rule
                        print("Modified Time: " +
                              str(assignment_rule.get_modified_time()))

                        # Get the Created Time of each Assignment Rule
                        print("Created Time: " +
                              str(assignment_rule.get_created_time()))

                        created_by = assignment_rule.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Created By - Name: " +
                                  created_by.get_name())

                            # Get the ID of the created_by User
                            print("Created By - ID: " +
                                  str(created_by.get_id()))

                            # Get the email of the created_by User
                            print("Created By - email: " +
                                  str(created_by.get_email()))

                        # Check if DefaultUser is not None
                        default_assignee = assignment_rule.get_default_assignee()
                        if default_assignee is not None:
                            # Get the Name of the default_assignee User
                            print("Created By - Name: " +
                                  default_assignee.get_name())

                            # Get the ID of the default_assignee User
                            print("Created By - ID: " +
                                  str(default_assignee.get_id()))

                         # Check if Module is not None
                        module = assignment_rule.get_module()
                        if module is not None:
                            # Get the API Name of the module User
                            print("Module - API Name: " +
                                  module.get_api_name())

                            # Get the ID of the default_assignee User
                            print("Module - ID: " + str(module.get_id()))

                        # Get the modified_by User instance of each currency
                        modified_by = assignment_rule.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Modified By - Name: " +
                                  modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Modified By - ID: " +
                                  str(modified_by.get_id()))

                            # Get the email of the created_by User
                            print("Modified By - ID: " +
                                  str(modified_by.get_email()))

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
