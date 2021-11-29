from zcrmsdk.src.com.zoho.crm.api.field_attachments import *
import os

class FieldAttachments(object):

    @staticmethod
    def get_field_attachments(module_api_name, record_id, attachment_id, destination_folder):
        """
        This method is used to get a field_attachments' details with ID and print the response.

        """
        # Get instance of FieldAttachmentsOperations Class
        # destination_folder = "/Users/test/Desktop"
        field_attachments_operations = FieldAttachmentsOperations(module_api_name, record_id, attachment_id)

        # Possible parameters for Get field_attachments Operation

        # Call get_field_attachments method
        response = field_attachments_operations.get_field_attachments()

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
                if isinstance(response_object, FileBodyWrapper):
                    # Get StreamWrapper instance from the returned FileBodyWrapper instance
                    stream_wrapper = response_object.get_file()

                    # Construct the file name by joining the destinationFolder and the name from StreamWrapper instance
                    file_name = os.path.join(destination_folder, stream_wrapper.get_name())

                    # Open the destination file where the file needs to be written in 'wb' mode
                    with open(file_name, 'wb') as f:
                        # Get the stream from StreamWrapper instance
                        for chunk in stream_wrapper.get_stream():
                            f.write(chunk)

                        f.close()

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
