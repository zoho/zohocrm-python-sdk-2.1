from zcrmsdk.src.com.zoho.crm.api.email_templates import *
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class EmailTemplates(object):

    @staticmethod
    def get_email_templates():
        """
        This method is used to get a email_templates' details with ID and print the response.

        """
        # Get instance of EmailTemplatesOperations Class

        email_templates_operations = EmailTemplatesOperations()


        # Call get_email_templates method that takes ParameterMap instance as parameter
        response = email_templates_operations.get_email_templates()

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
                    email_templates_list = response_object.get_email_templates()

                    for email_template in email_templates_list:

                        # Get the ID of each Email Template
                        print(" ID " + str(email_template.get_id()))

                        # Get the name of each Email Template
                        print("Name: " + str(email_template.get_name()))

                        # Get the description of each Email Template
                        print("description: " + str(email_template.get_description()))

                        # Get the Modified Time of each Email Template
                        print("Modified Time: " + str(email_template.get_modified_time()))

                        # Get the Created Time of each Email Template
                        print("Created Time: " + str(email_template.get_created_time()))

                         # Get the Subject of each Email Template
                        print("Subject: " + str(email_template.get_subject()))

                        # Get the type of each Email Template
                        print("Type: " + str(email_template.get_type()))

                        # Get the Last Usage Time of each Email Template
                        print("Last Usage Time: " + str(email_template.get_last_usage_time()))

                        # Get the Consent Linked of each Email Template
                        print("Consent Linked: " + str(email_template.get_consent_linked()))

                        # Get the Associated of each Email Template
                        print("Associated: " + str(email_template.get_associated()))

                        # Get the Content of each Email Template
                        print("Content: " + str(email_template.get_content()))

                        # Get the EditorMode of each Email Template
                        print("EditorMode: " + str(email_template.get_editor_mode()))

                        created_by = email_template.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Created By - ID: " + str(created_by.get_id()))

                             # Get the email of the created_by User
                            print("Created By - email: " + str(created_by.get_email()))

                        # Check if Folder is not None
                        folder = email_template.get_folder()
                        if folder is not None:
                            # Get the ID of the folder
                            print("EmailTemplate folder ID: " + folder.get_name())

                            # Get the Name of the folder
                            print("EmailTemplate folder Name:" + str(folder.get_id()))

                         # get module 
                        module = email_template.get_module()
                        if module is not None:
                            # Get the API Name of the module User
                            print("Module - API Name: " + module.get_api_name())

                            # Get the ID of the default_assignee User
                            print("Module - ID: " + str(module.get_id()))

                        # get attachments 
                        attachments = email_template.get_attachments()
                        if attachments is not None:
                            for attachment in attachments:
                                print ("EmailTemplate Attachment File ID: " + attachment.get_file_id)
                                print ("EmailTemplate Attachment File Name: " + attachment.get_file_name)
                                print ("EmailTemplate Attachment File Size: " + attachment.get_size)
                                print ("EmailTemplate Attachment File ID: " + attachment.get_id)


                        # Get the modified_by User instance of each currency
                        modified_by = email_template.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Modified By - ID: " + str(modified_by.get_id()))

                             # Get the email of the created_by User
                            print("Modified By - ID: " + str(modified_by.get_email()))

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
    def get_email_template_by_id(id):
        """
        This method is used to get  email_templates' details with ID and print the response.

        """


        # Get instance of EmailTemplatesOperations Class
        email_templates_operations = EmailTemplatesOperations()


        response = email_templates_operations.get_email_template_by_id(id)

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
                    email_templates_list = response_object.get_email_templates()

                    for email_template in email_templates_list:

                        # Get the ID of each Email Template
                        print(" ID " + str(email_template.get_id()))

                        # Get the name of each Email Template
                        print("Name: " + str(email_template.get_name()))

                        # Get the description of each Email Template
                        print("description: " + str(email_template.get_description()))

                        # Get the Modified Time of each Email Template
                        print("Modified Time: " + str(email_template.get_modified_time()))

                        # Get the Created Time of each Email Template
                        print("Created Time: " + str(email_template.get_created_time()))

                         # Get the Subject of each Email Template
                        print("Subject: " + str(email_template.get_subject()))

                        # Get the type of each Email Template
                        print("Type: " + str(email_template.get_type()))

                        # Get the Last Usage Time of each Email Template
                        print("Last Usage Time: " + str(email_template.get_last_usage_time()))

                        # Get the Consent Linked of each Email Template
                        print("Consent Linked: " + str(email_template.get_consent_linked()))

                        # Get the Associated of each Email Template
                        print("Associated: " + str(email_template.get_associated()))

                        # Get the Content of each Email Template
                        print("Content: " + str(email_template.get_content()))

                        # Get the EditorMode of each Email Template
                        print("EditorMode: " + str(email_template.get_editor_mode()))


                        created_by = email_template.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Created By - Name: " + created_by.get_name())

                            # Get the ID of the created_by User
                            print("Created By - ID: " + str(created_by.get_id()))

                             # Get the email of the created_by User
                            print("Created By - email: " + str(created_by.get_email()))

                        # Check if Folder is not None
                        folder = email_template.get_folder()
                        if folder is not None:
                            # Get the ID of the folder
                            print("EmailTemplate folder ID: " + folder.get_name())

                            # Get the Name of the folder
                            print("EmailTemplate folder Name:" + str(folder.get_id()))

                         # get module 
                        module = email_template.get_module()
                        if module is not None:
                            # Get the API Name of the module 
                            print("Module - API Name: " + module.get_api_name())

                            # Get the ID of the module
                            print("Module - ID: " + str(module.get_id()))

                        # get attachments 
                        attachments = email_template.get_attachments()
                        if attachments is not None:
                            for attachment in attachments:
                                print ("EmailTemplate Attachment File ID: " + attachment.get_file_id)
                                print ("EmailTemplate Attachment File Name: " + attachment.get_file_name)
                                print ("EmailTemplate Attachment File Size: " + attachment.get_size)
                                print ("EmailTemplate Attachment File ID: " + attachment.get_id)


                        # Get the modified_by User instance of each currency
                        modified_by = email_template.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modifiedBy User
                            print("Modified By - Name: " + modified_by.get_name())

                            # Get the ID of the modifiedBy User
                            print("Modified By - ID: " + str(modified_by.get_id()))

                             # Get the email of the created_by User
                            print("Modified By - ID: " + str(modified_by.get_email()))


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

