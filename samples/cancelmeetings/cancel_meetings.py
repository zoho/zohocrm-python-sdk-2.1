from zcrmsdk.src.com.zoho.crm.api.cancel_meetings import *


class CancelMeetings(object):

    @staticmethod
    def cancel_meetings(event_id, send_cancel_mail):

        #get the instance of CancelMeetingsOperations Class
        cancel_meeting_operation = CancelMeetingsOperations(event_id)

        #get the instance of BodyWrapper Class
        bodywrapper = BodyWrapper()

        #get the instance of Notify Class
        notify = Notify()

        #set sendCancelMail to instance of Notify Class
        notify.set_send_cancelling_mail(send_cancel_mail)

        #List to store the instance of Notify Class
        notify_list = []

        # add the instance of Notify Class to List
        notify_list.append(notify)

        # set the List to data of BodyWrapper instance
        bodywrapper.set_data(notify_list)

        #Get the response by calling cancel_meetings method with BodyWrapper instance as the parameter
        response = cancel_meeting_operation.cancel_meetings(bodywrapper)

        if response is not None:

            print('Status Code: ' + str(response.get_status_code()))

            response_object = response.get_object()

            if response_object is not None:

                if isinstance(response_object, ActionWrapper):

                    action_response_list = response_object.get_data()

                    for action_response in action_response_list:

                        if isinstance(action_response, SuccessResponse):

                            print("Status: " + action_response.get_status().get_value())

                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            print("Message: " + action_response.get_message().get_value())

                        elif isinstance(action_response, APIException):

                            print("Status: " + action_response.get_status().get_value())

                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            print("Message: " + action_response.get_message().get_value())

                elif isinstance(response_object, APIException):

                    print("Status: " + response_object.get_status().get_value())

                    print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    details = response_object.get_details()

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    print("Message: " + response_object.get_message().get_value())
