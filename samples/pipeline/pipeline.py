from zcrmsdk.src.com.zoho.crm.api.pipeline import *
from zcrmsdk.src.com.zoho.crm.api import ParameterMap


class Pipelines(object):

    @staticmethod
    def transfer_and_delete(layout_id):

        transfer_and_delete_wrapper = TransferAndDeleteWrapper()
        transfer_pipeline = TransferPipeLine()

        pipeline = Pipeline()
        pipeline.set_from(36523973712004)
        pipeline.set_to(36523973712004)
        stage = Stage()
        stage.set_to(36523976819)
        stage.set_from(36523976817)
        transfer_pipeline.set_pipeline(pipeline)
        transfer_pipeline.set_stages([stage])
        transfer_and_delete_wrapper.set_transfer_pipeline([transfer_pipeline])

        pipeline_operations = PipelineOperations(layout_id)
        response = pipeline_operations.transfer_and_delete(transfer_and_delete_wrapper)
        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_pipelines()

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

    @staticmethod
    def get_pipelines(layout_id):
        # layout_id = 35240330091055
        pipeline_operations = PipelineOperations(layout_id)
        response = pipeline_operations.get_pipelines()
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
                    pipelines_list = response_object.get_pipeline()

                    for pipeline in pipelines_list:
                        # Get the ID of each Pipeline
                        print("ID: " + str(pipeline.get_id()))

                        # Get the Display value of each Pipeline
                        print("Display value: " + str(pipeline.get_display_value()))

                        # Get the Actual value of each Pipeline
                        print("Actual value: " + str(pipeline.get_actual_value()))

                         # Get the default of each Pipeline
                        print("default: " + str(pipeline.get_default()))

                        # Get the child available of each Pipeline
                        print("child available: " + str(pipeline.get_child_available()))

                        # Get the parent of each Pipeline
                        parent = pipeline.get_parent()
                        if parent is not None:
                            # Get pipeline parent of each Pipeline
                            print("pipeline parent: " + str(parent.get_id()))
                        
                        maps = pipeline.get_maps()

                        for map_instance in maps:
                            # Get the PickListValue Actual Value 
                            print("PickListValue Actual Value: " + str(map_instance.get_actual_value()))

                            # Get the PickListValue delete Value 
                            print("PickListValue delete Value: " + str(map_instance.get_delete()))

                            # Get the PickListValue Display Value 
                            print("PickListValue Display Value: " + str(map_instance.get_display_value()))

                            # Get the PickListValue forecast type
                            print("PickListValue forecast type: " + str(map_instance.get_forecast_type()))

                            forecast_category = map_instance.get_forecast_category()

                            if forecast_category is not None:
                                # Get Forecast Category Name 
                                print("Forecast Category Name: " + str(forecast_category.get_name()))

                                # Get Forecast Category ID 
                                print("Forecast Category ID: " + str(forecast_category.get_id()))

                            # Get the PickListValue id
                            print("PickListValue id: " + str(map_instance.get_id()))

                            # Get the PickListValue sequence number
                            print("PickListValue sequence number: " + str(map_instance.get_sequence_number()))

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
    def create_pipelines(layout_id):
        # layout_id = 35240330091055
        pipeline_operations = PipelineOperations(layout_id)
        pipeline = Pipeline()
        pipeline.set_display_value("Pipeline2")
        pipeline.set_default(True)
        map = PickListValue()
        map.set_sequence_number(1)
        map.set_id(36523976815)
        map.set_display_value("Closed Won")
        maps =[map]
        pipeline.set_maps(maps)
        request = BodyWrapper()
        request.set_pipeline([pipeline])
        response = pipeline_operations.create_pipelines(request)
        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_pipeline()

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

    @staticmethod
    def update_pipelines(layout_id):
        # layout_id = 35240330091055

        pipeline_operations = PipelineOperations(layout_id)
        pipeline = Pipeline()
        pipeline_id = 36523976815
        pipeline.set_display_value("Pipeline2")
        pipeline.set_default(True)
        pipeline.set_id(pipeline_id)
        map = PickListValue()
        map.set_sequence_number(1)
        map.set_id(36523976815)
        map.set_display_value("Closed Won")
        maps = [map]
        pipeline.set_maps(maps)
        request = BodyWrapper()
        request.set_pipeline([pipeline])
        response = pipeline_operations.update_pipelines(request)
        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_pipeline()

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

    @staticmethod
    def get_pipeline(pipeline_id, layout_id):
        # layout_id = 35240330091055
        pipeline_operations = PipelineOperations(layout_id)
        pipeline_id = 13213
        response = pipeline_operations.get_pipeline(pipeline_id)
        if response is not None:

            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            response_object = response.get_object()

            # Check if expected ResponseWrapper instance is received
            if isinstance(response_object, ResponseWrapper):
                pipelines_list = response_object.get_pipelines()

                for pipeline in pipelines_list:
                    # Get the ID of each Pipeline
                    print("ID: " + str(pipeline.get_id()))

                    # Get the Display value of each Pipeline
                    print("Display value: " + str(pipeline.get_display_value()))

                    # Get the Actual value of each Pipeline
                    print("Actual value: " + str(pipeline.get_actual_value()))

                     # Get the default of each Pipeline
                    print("default: " + str(pipeline.get_default()))

                    # Get the child available of each Pipeline
                    print("child available: " + str(pipeline.get_child_available()))

                    # Get the parent of each Pipeline
                    parent = pipeline.parent
                    if parent is not None:
                        # Get pipeline parent of each Pipeline
                        print("pipeline parent: " + str(parent.get_id()))

                    maps = pipeline.maps

                    for map_instance in maps:
                        # Get the PickListValue Actual Value
                        print("PickListValue Actual Value: " + str(map_instance.get_actual_value()))

                        # Get the PickListValue delete Value
                        print("PickListValue delete Value: " + str(map_instance.get_delete_value()))

                        # Get the PickListValue Display Value
                        print("PickListValue Display Value: " + str(map_instance.get_display_value()))

                        # Get the PickListValue forecast type
                        print("PickListValue forecast type: " + str(map_instance.get_forecast_type()))

                        forecast_category = map_instance.forcast_catergory

                        if forecast_category is not None:
                            # Get Forecast Category Name
                            print("Forecast Category Name: " + str(forecast_category.get_name()))

                            # Get Forecast Category ID
                            print("Forecast Category ID: " + str(forecast_category.get_id()))

                        # Get the PickListValue id
                        print("PickListValue id: " + str(map_instance.get_id()))

                        # Get the PickListValue sequence number
                        print("PickListValue sequence number: " + str(map_instance.get_sequence_number()))

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
    def update_pipeline(pipeline_id, layout_id):
        # layout_id = 35240330091055
        pipeline_operations = PipelineOperations(layout_id)
        pipeline = Pipeline()
        pipeline.set_display_value("Pipeline2")
        pipeline.set_default(True)
        map = PickListValue()
        map.set_sequence_number(1)
        map.set_id(36523976815)
        map.set_display_value("Closed Won")
        maps = [map]
        pipeline.set_maps(maps)
        request = BodyWrapper()
        request.set_pipeline([pipeline])
        response = pipeline_operations.update_pipeline(pipeline_id, request)
        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_pipelines()

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
