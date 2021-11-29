from zcrmsdk.src.com.zoho.crm.api.send_mail import *
from zcrmsdk.src.com.zoho.crm.api import ParameterMap
from datetime import date, datetime
from zcrmsdk.src.com.zoho.crm.api.attachments import Attachment
from zcrmsdk.src.com.zoho.crm.api.email_templates import EmailTemplate



class SendMail(object):

    @staticmethod
    def get_email_addresses():
        """
        This method is used to get a send_mail' details with ID and print(the response.

        """
        # Get instance of SendMailOperations Class

        send_mail_operations = SendMailOperations()


        # Call get_send_mail method that takes ParameterMap instance as parameter
        response = send_mail_operations.get_email_addresses()

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
                    send_mail_list = response_object.get_from_addresses()
                    for from_address in send_mail_list:
                        # Get the email of From addresses
                        print("\From address email: "+from_address.get_email())
                        # Get the Type of From addresses
                        print("\From address Type: "+from_address.get_type())
                        # Get the UserName of From addresses
                        print("\From address UserName: "+from_address.get_user_name())
                        # Get the ID of each From addresses
                        print("\n From address ID: "+str(from_address.get_id()))
                        # Get the Default of each From addresses
                        print("\n From address Default: "+str(from_address.get_default()))

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
    def send_mail(record_id,module_api_name):
        """
        This method is used to   send_mail'

        """


        # Get instance of SendMailOperations Class
        send_mail_operations = SendMailOperations()

        request = BodyWrapper()
        mail = Mail()
        user_address_from = UserAddress()
        user_address_to = UserAddress()
        user_address_cc = UserAddress()
        user_address_bcc = UserAddress()
        user_address_reply_to = UserAddress()
        attachment = Attachment()
        # attachment.set_id("2cceafa194d037b63f2181dd81864b4812b1f8b0b4fe0949a982de89fa75a")
        template = EmailTemplate()
        template.set_id(36523972497001)
        user_address_from.set_user_name("abc Boyle")
        user_address_from.set_email("abc.a@zoho.com")
        user_address_to.set_user_name("Jason Smith")
        user_address_to.set_email("abc.a@zoho.com")
        user_address_cc.set_user_name("Jasweon Smith")
        user_address_cc.set_email("abc.a@zoho.com")
        user_address_bcc.set_user_name("Jassdon Smith")
        user_address_bcc.set_email("abc.a@zoho.com")
        user_address_reply_to.set_user_name("Jassdon Smith")
        user_address_reply_to.set_email("abc.a@zoho.com")

        mail.set_from(user_address_from)
        mail.set_to([user_address_to])
        mail.set_bcc([user_address_bcc])
        mail.set_cc([user_address_cc])
        mail.set_reply_to(user_address_reply_to)
        mail.set_org_email(False)
        mail.set_in_reply_to("2cceafa194d037b63f2181dd8186486f1eb0360aee76d802b6d376dea97e7")
        mail.set_scheduled_time(datetime(2021, 4, 8, 0, 42, 10))
        mail.set_subject("Testing Send Mail API")
        mail.set_content("<h3><span style=\"background-color: rgb(254, 255, 102)\">Mail is of rich text format</span></h3><h3><span style=\"background-color: rgb(254, 255, 102)\"><img src=\"https://www.zohoapis.com/crm/viewInLineImage?fileContent=2cceafa194d037b63f2181dd818646fd5e5167a274098b625c35654a20ed2\"></span></h3><h3><span style=\"background-color: rgb(254, 255, 102)\">REGARDS,</span></h3><div><span style=\"background-color: rgb(254, 255, 102)\">AZ</span></div><div><span style=\"background-color: rgb(254, 255, 102)\">ADMIN</span></div> <div></div>")
        mail.set_mail_format("html")
        # mail.set_attachments([attachment])
        # mail.set_template(template)
        request.set_data([mail])
        response = send_mail_operations.send_mail(record_id, module_api_name, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_data()

                    for action_response in action_response_list:

                        # Check if the request is successful
                        if isinstance(action_response, SuccessResponse):
                            # Get the Status
                            print("Status: " + action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " + action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " + action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " + action_response.get_message().get_value())

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
