import os
from datetime import date, datetime
from zcrmsdk.src.com.zoho.crm.api.record import *
from zcrmsdk.src.com.zoho.crm.api.attachments import Attachment
from zcrmsdk.src.com.zoho.crm.api.tags import Tag
from zcrmsdk.src.com.zoho.crm.api.layouts import Layout
from zcrmsdk.src.com.zoho.crm.api.users import User
from zcrmsdk.src.com.zoho.crm.api import HeaderMap, ParameterMap
from zcrmsdk.src.com.zoho.crm.api.util import Choice, StreamWrapper
from zcrmsdk.src.com.zoho.crm.api.record import Record as ZCRMRecord


class Record(object):

    @staticmethod
    def get_record(module_api_name, record_id, destination_folder):
        """
		This method is used to get a single record of a module with ID and print the response.
		:param module_api_name: The API Name of the record's module.
		:param record_id: The ID of the record to be obtained.
		:param destination_folder: The absolute path of the destination folder to store the downloaded attachment Record
		"""

        """
		example
		module_api_name = 'Leads'
		record_id = 34770616603276
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Get Record operation
        param_instance.add(GetRecordParam.cvid, '34096430087501')

        param_instance.add(GetRecordParam.approved, 'true')

        param_instance.add(GetRecordParam.converted, 'both')

        fields = ['id', 'company']

        for field in fields:
            param_instance.add(GetRecordParam.fields, field)

        start_date_time = datetime(2020, 1, 1, 10, 10, 10)

        param_instance.add(GetRecordParam.startdatetime, start_date_time)

        end_date_time = datetime(2020, 7, 7, 10, 10, 10)

        param_instance.add(GetRecordParam.enddatetime, end_date_time)

        param_instance.add(GetRecordParam.territory_id, '34096430505351')

        param_instance.add(GetRecordParam.include_child, 'true')

        param_instance.add(GetRecordParam.uid, '34096430500741')

        # Get instance of HeaderMap Class
        header_instance = HeaderMap()

        # Possible headers for Get Record operation
        header_instance.add(GetRecordHeader.if_modified_since, datetime.now())

        # header_instance.add(GetRecordHeader.x_external, "Leads.External")

        # Call getRecord method that takes record_id, module_api_name, param_instance and header_instance as parameter
        response = record_operations.get_record(
            record_id, module_api_name, param_instance, header_instance)

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

                # Check if expected ResponseWrapper instance is received.
                if isinstance(response_object, ResponseWrapper):

                    # Get the list of obtained Record instances
                    record_list = response_object.get_data()

                    for record in record_list:
                        # Get the ID of each Record
                        print("Record ID: " + str(record.get_id()))

                        # Get the createdBy User instance of each Record
                        created_by = record.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Record Created By - Name: " +
                                  created_by.get_name())

                            # Get the ID of the created_by User
                            print("Record Created By - ID: " +
                                  str(created_by.get_id()))

                            # Get the Email of the created_by User
                            print("Record Created By - Email: " +
                                  created_by.get_email())

                        # Get the CreatedTime of each Record
                        print("Record CreatedTime: " +
                              str(record.get_created_time()))

                        if record.get_modified_time() is not None:
                            # Get the ModifiedTime of each Record
                            print("Record ModifiedTime: " +
                                  str(record.get_modified_time()))

                        # Get the modified_by User instance of each Record
                        modified_by = record.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modified_by User
                            print("Record Modified By - Name: " +
                                  modified_by.get_name())

                            # Get the ID of the modified_by User
                            print("Record Modified By - ID: " +
                                  str(modified_by.get_id()))

                            # Get the Email of the modified_by User
                            print("Record Modified By - Email: " +
                                  modified_by.get_email())

                        # Get the list of obtained Tag instance of each Record
                        tags = record.get_tag()

                        if tags is not None:
                            for tag in tags:
                                # Get the Name of each Tag
                                print("Record Tag Name: " + tag.get_name())

                                # Get the Id of each Tag
                                print("Record Tag ID: " + str(tag.get_id()))

                        # To get particular field value
                        print("Record Field Value: " +
                              str(record.get_key_value('Last_Name')))

                        print('Record KeyValues: ')

                        key_values = record.get_key_values()

                        for key_name, value in key_values.items():

                            if isinstance(value, list):

                                if len(value) > 0:

                                    if isinstance(value[0], FileDetails):
                                        file_details = value

                                        for file_detail in file_details:
                                            # Get the Extn of each FileDetails
                                            print(
                                                "Record FileDetails Extn: " + file_detail.get_extn())

                                            # Get the IsPreviewAvailable of each FileDetails
                                            print("Record FileDetails IsPreviewAvailable: " + str(
                                                file_detail.get_is_preview_available()))

                                            # Get the DownloadUrl of each FileDetails
                                            print(
                                                "Record FileDetails DownloadUrl: " + file_detail.get_download_url())

                                            # Get the DeleteUrl of each FileDetails
                                            print(
                                                "Record FileDetails DeleteUrl: " + file_detail.get_delete_url())

                                            # Get the EntityId of each FileDetails
                                            print(
                                                "Record FileDetails EntityId: " + file_detail.get_entity_id())

                                            # Get the Mode of each FileDetails
                                            print(
                                                "Record FileDetails Mode: " + file_detail.get_mode())

                                            # Get the OriginalSizeByte of each FileDetails
                                            print(
                                                "Record FileDetails OriginalSizeByte: " + file_detail.get_original_size_byte())

                                            # Get the PreviewUrl of each FileDetails
                                            print(
                                                "Record FileDetails PreviewUrl: " + file_detail.get_preview_url())

                                            # Get the FileName of each FileDetails
                                            print(
                                                "Record FileDetails FileName: " + file_detail.get_file_name())

                                            # Get the FileId of each FileDetails
                                            print(
                                                "Record FileDetails FileId: " + file_detail.get_file_id())

                                            # Get the AttachmentId of each FileDetails
                                            print(
                                                "Record FileDetails AttachmentId: " + file_detail.get_attachment_id())

                                            # Get the FileSize of each FileDetails
                                            print(
                                                "Record FileDetails FileSize: " + file_detail.get_file_size())

                                            # Get the CreatorId of each FileDetails
                                            print(
                                                "Record FileDetails CreatorId: " + file_detail.get_creator_id())

                                            # Get the LinkDocs of each FileDetails
                                            print(
                                                "Record FileDetails LinkDocs: " + str(file_detail.get_link_docs()))

                                    elif isinstance(value[0], Reminder):
                                        reminders = value

                                        for reminder in reminders:
                                            # Get the Reminder Period
                                            print("Reminder Period: " +
                                                  reminder.get_period())

                                            # Get the Reminder Unit
                                            print("Reminder Unit: " +
                                                  reminder.get_unit())

                                    elif isinstance(value[0], Choice):
                                        choice_list = value

                                        print(key_name)

                                        print('Values')

                                        for choice in choice_list:
                                            print(choice.get_value())

                                    elif isinstance(value[0], Participants):
                                        participants = value

                                        for participant in participants:
                                            print("Record Participants Name: ")
                                            print(participant.get_name())

                                            print(
                                                "Record Participants Invited: " + str(participant.get_invited()))

                                            print(
                                                "Record Participants Type: " + participant.get_type())

                                            print(
                                                "Record Participants Participant: " + participant.get_participant())

                                            print(
                                                "Record Participants Status: " + participant.get_status())

                                    elif isinstance(value[0], ImageUpload):
                                        image_uploads = value

                                        for image_upload in image_uploads:
                                            print("Record  Id: " +
                                                  str(image_upload.get_id()))

                                            print("Record  FileId: " +
                                                  image_upload.get_file_id())

                                            print(
                                                "Record  SequenceNumber: " + str(image_upload.get_sequence_number()))

                                            print("Record  Size: " +
                                                  str(image_upload.get_size()))

                                            print("Record  State: " +
                                                  str(image_upload.get_state()))

                                            print("Record  File_Name: " +
                                                  image_upload.get_file_name())

                                            print("Record  PreviewId: " +
                                                  image_upload.get_preview_id())

                                            print("Record  Description: " +
                                                  str(image_upload.get_description()))

                                    elif isinstance(value[0], Tax):
                                        tax = value[0]

                                        print("Record Tax Name: " +
                                              tax.get_value())

                                        print("Record Tax ID: " +
                                              str(tax.get_id()))

                                    elif isinstance(value[0], ImageUpload):
                                        image_uploads = value

                                        for image_upload in image_uploads:
                                            print("RelatedRecord  Id: " +
                                                  str(image_upload.get_id()))

                                            print("RelatedRecord  FileId: " +
                                                  image_upload.get_file_id())

                                            print(
                                                "RelatedRecord  SequenceNumber: " + image_upload.get_sequence_number())

                                            print("RelatedRecord  Size: " +
                                                  str(image_upload.get_size()))

                                            print("RelatedRecord  State: " +
                                                  str(image_upload.get_state()))

                                            print(
                                                "RelatedRecord  File_Name: " + image_upload.get_file_name())

                                            print(
                                                "RelatedRecord  PreviewId: " + image_upload.get_preview_id())

                                            print(
                                                "RelatedRecord  Description: " + str(image_upload.get_description()))

                                    elif isinstance(value[0], Tag):
                                        tags = value

                                        if tags is not None:
                                            for tag in tags:
                                                print(
                                                    "Record Tag Name: " + tag.get_name())

                                                print("Record Tag ID: " +
                                                      str(tag.get_id()))

                                    elif isinstance(value[0], PricingDetails):
                                        pricing_details = value

                                        for pricing_detail in pricing_details:
                                            print(
                                                "Record PricingDetails ToRange: " + str(pricing_detail.get_to_range()))

                                            print(
                                                "Record PricingDetails Discount: " + str(pricing_detail.get_discount()))

                                            print(
                                                "Record PricingDetails ID: " + str(pricing_detail.get_id()))

                                            print("Record PricingDetails FromRange: " + str(
                                                pricing_detail.get_from_range()))

                                    elif isinstance(value[0], ZCRMRecord):
                                        record_list = value

                                        for each_record in record_list:
                                            for key, val in each_record.get_key_values().items():
                                                print(
                                                    str(key) + " : " + str(val))

                                    elif isinstance(value[0], LineTax):
                                        line_taxes = value

                                        for line_tax in line_taxes:
                                            print("Record LineTax Percentage: " + str(
                                                line_tax.get_percentage()))

                                            print(
                                                "Record LineTax Name: " + line_tax.get_name())

                                            print("Record LineTax Id: " +
                                                  str(line_tax.get_id()))

                                            print("Record LineTax Value: " +
                                                  str(line_tax.get_value()))

                                    elif isinstance(value[0], Comment):
                                        comments = value

                                        for comment in comments:
                                            print("Comment-ID: " +
                                                  str(comment.get_id()))

                                            print("Comment-Content: " +
                                                  comment.get_comment_content())

                                            print("Comment-Commented_By: " +
                                                  comment.get_commented_by())

                                            print("Comment-Commented Time: " +
                                                  str(comment.get_commented_time()))

                                    elif isinstance(value[0], Attachment):
                                        attachments = value

                                        for attachment in attachments:
                                            # Get the ID of each attachment
                                            print('Record Attachment ID : ' +
                                                  str(attachment.get_id()))

                                            # Get the owner User instance of each attachment
                                            owner = attachment.get_owner()

                                            # Check if owner is not None
                                            if owner is not None:
                                                # Get the Name of the Owner
                                                print(
                                                    "Record Attachment Owner - Name: " + owner.get_name())

                                                # Get the ID of the Owner
                                                print(
                                                    "Record Attachment Owner - ID: " + str(owner.get_id()))

                                                # Get the Email of the Owner
                                                print(
                                                    "Record Attachment Owner - Email: " + owner.get_email())

                                            # Get the modified time of each attachment
                                            print("Record Attachment Modified Time: " + str(
                                                attachment.get_modified_time()))

                                            # Get the name of the File
                                            print(
                                                "Record Attachment File Name: " + attachment.get_file_name())

                                            # Get the created time of each attachment
                                            print(
                                                "Record Attachment Created Time: " + str(attachment.get_created_time()))

                                            # Get the Attachment file size
                                            print(
                                                "Record Attachment File Size: " + str(attachment.get_size()))

                                            # Get the parentId Record instance of each attachment
                                            parent_id = attachment.get_parent_id()

                                            if parent_id is not None:
                                                # Get the parent record Name of each attachment
                                                print(
                                                    "Record Attachment parent record Name: ")
                                                print(
                                                    parent_id.get_key_value("name"))

                                                # Get the parent record ID of each attachment
                                                print(
                                                    "Record Attachment parent record ID: " + str(parent_id.get_id()))

                                            # Check if the attachment is Editable
                                            print(
                                                "Record Attachment is Editable: " + str(attachment.get_editable()))

                                            # Get the file ID of each attachment
                                            print(
                                                "Record Attachment File ID: " + str(attachment.get_file_id()))

                                            # Get the type of each attachment
                                            print(
                                                "Record Attachment File Type: " + str(attachment.get_type()))

                                            # Get the seModule of each attachment
                                            print(
                                                "Record Attachment seModule: " + str(attachment.get_se_module()))

                                            # Get the modifiedBy User instance of each attachment
                                            modified_by = attachment.get_modified_by()

                                            # Check if modifiedBy is not None
                                            if modified_by is not None:
                                                # Get the Name of the modifiedBy User
                                                print(
                                                    "Record Attachment Modified By - Name: " + modified_by.get_name())

                                                # Get the ID of the modifiedBy User
                                                print(
                                                    "Record Attachment Modified By - ID: " + str(modified_by.get_id()))

                                                # Get the Email of the modifiedBy User
                                                print(
                                                    "Record Attachment Modified By - Email: " + modified_by.get_email())

                                            # Get the state of each attachment
                                            print(
                                                "Record Attachment State: " + attachment.get_state())

                                            # Get the modifiedBy User instance of each attachment
                                            created_by = attachment.get_created_by()

                                            # Check if created_by is not None
                                            if created_by is not None:
                                                # Get the Name of the modifiedBy User
                                                print(
                                                    "Record Attachment Created By - Name: " + created_by.get_name())

                                                # Get the ID of the modifiedBy User
                                                print(
                                                    "Record Attachment Created By - ID: " + str(created_by.get_id()))

                                                # Get the Email of the modifiedBy User
                                                print(
                                                    "Record Attachment Created By - Email: " + created_by.get_email())

                                            # Get the linkUrl of each attachment
                                            print(
                                                "Record Attachment LinkUrl: " + str(attachment.get_link_url()))

                                    else:
                                        print(key_name)

                                        for each_value in value:
                                            print(str(each_value))

                            elif isinstance(value, User):
                                print("Record " + key_name +
                                      " User-ID: " + str(value.get_id()))

                                print("Record " + key_name +
                                      " User-Name: " + value.get_name())

                                print("Record " + key_name +
                                      " User-Email: " + value.get_email())

                            elif isinstance(value, Layout):
                                print(key_name + " ID: " + str(value.get_id()))

                                print(key_name + " Name: " + value.get_name())

                            elif isinstance(value, ZCRMRecord):
                                print(key_name + " Record ID: " +
                                      str(value.get_id()))

                                print(key_name + " Record Name: " +
                                      value.get_key_value('name'))

                            elif isinstance(value, Choice):
                                print(key_name + " : " + value.get_value())

                            elif isinstance(value, RemindAt):
                                print(key_name + " : " + value.get_alarm())

                            elif isinstance(value, RecurringActivity):
                                print(key_name)

                                print("RRULE: " + value.get_rrule())

                            elif isinstance(value, Consent):
                                print("Record Consent ID: " +
                                      str(value.get_id()))

                                # Get the createdBy User instance of each Record
                                created_by = value.get_created_by()

                                # Check if created_by is not None
                                if created_by is not None:
                                    # Get the Name of the created_by User
                                    print(
                                        "Record Consent Created By - Name: " + created_by.get_name())

                                    # Get the ID of the created_by User
                                    print(
                                        "Record Consent Created By - ID: " + str(created_by.get_id()))

                                    # Get the Email of the created_by User
                                    print(
                                        "Record Consent Created By - Email: " + created_by.get_email())

                                # Get the CreatedTime of each Record
                                print("Record Consent CreatedTime: " +
                                      str(value.get_created_time()))

                                if value.get_modified_time() is not None:
                                    # Get the ModifiedTime of each Record
                                    print("Record Consent ModifiedTime: " +
                                          str(value.get_modified_time()))

                                # Get the Owner User instance of the Consent
                                owner = value.get_owner()

                                if owner is not None:
                                    # Get the Name of the Owner User
                                    print(
                                        "Record Consent Created By - Name: " + owner.get_name())

                                    # Get the ID of the Owner User
                                    print(
                                        "Record Consent Created By - ID: " + str(owner.get_id()))

                                    # Get the Email of the Owner User
                                    print(
                                        "Record Consent Created By - Email: " + owner.get_email())

                                print("Record Consent ContactThroughEmail: " +
                                      str(value.get_contact_through_email()))

                                print("Record Consent ContactThroughSocial: " +
                                      str(value.get_contact_through_social()))

                                print("Record Consent ContactThroughSurvey: " +
                                      str(value.get_contact_through_survey()))

                                print("Record Consent ContactThroughPhone: " +
                                      str(value.get_contact_through_phone()))

                                print("Record Consent MailSentTime: " +
                                      str(value.get_mail_sent_time()))

                                print("Record Consent ConsentDate: " +
                                      str(value.get_consent_date()))

                                print("Record Consent ConsentRemarks: " +
                                      value.get_consent_remarks())

                                print("Record Consent ConsentThrough: " +
                                      value.get_consent_through())

                                print("Record Consent DataProcessingBasis: " +
                                      value.get_data_processing_basis())

                                # To get custom values
                                print("Record Consent Lawful Reason: " +
                                      str(value.get_key_value("Lawful_Reason")))

                            elif isinstance(value, dict):
                                for key, val in value.items():
                                    print(key + " : " + str(val))

                            else:
                                print(key_name + " : " + str(value))

                # Check if expected FileBodyWrapper instance is received.
                elif isinstance(response_object, FileBodyWrapper):

                    # Get StreamWrapper instance from the returned FileBodyWrapper instance
                    stream_wrapper = response_object.get_file()

                    # Construct the file name by joining the destinationFolder and the name from StreamWrapper instance
                    file_name = os.path.join(
                        destination_folder, stream_wrapper.get_name())

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

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def update_record(module_api_name, record_id):
        """
		This method is used to update a single record of a module with ID and print the response.
		:param module_api_name: The API Name of the record's module.
		:param record_id: The ID of the record to be updated
		"""

        """
		example
		module_api_name = 'Leads'
		record_id = 34770616603276
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Record instances
        records_list = []

        # Get instance of Record Class
        record = ZCRMRecord()

        # Get the instance of ApplyFeatureExecution Class
        apply_feature_execution = ApplyFeatureExecution()

        # set name to instance of ApplyFeatureExecution Class
        apply_feature_execution.set_name("layout_rules")

        # Add instance of ApplyFeatureExecution to apply_feature_list
        apply_feature_list = []

        apply_feature_list.append(apply_feature_execution)

        # set the data to BodyWrapper instance
        request.set_apply_feature_execution(apply_feature_list)

        # Value to Record's fields can be provided in any of the following ways

        """
		Call add_field_value method that takes two arguments
		Import the zcrmsdk.src.com.zoho.crm.api.record.field file
		1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field name from the displayed list.
		2 -> Value
		"""

        record.add_field_value(Field.Leads.last_name(), 'Python SDK')

        record.add_field_value(Field.Leads.first_name(), 'New')

        record.add_field_value(Field.Leads.company(), 'Zoho')

        record.add_field_value(Field.Leads.city(), 'City')

        """
		Call add_key_value method that takes two arguments
		1 -> A string that is the Field's API Name
		2 -> Value
		"""

        record.add_key_value('Custom_field', 'Value')

        record.add_key_value('Custom_field_2', 12)

        # record.add_key_value('Date', date(2020, 4, 9))

        record.add_key_value('Discounted', 23.34)

        file_details = []

        file_detail = FileDetails()

        file_detail.set_file_id(
            '479f0f5eebf0fb982f99e3832b35d23e29f67c2868ee4c789f22579895383c8')

        file_details.append(file_detail)

        record.add_key_value('File_Upload', file_details)

        record_owner = User()

        record_owner.set_email("abc@zoho.com")

        record.add_key_value("Owner", record_owner)

        # Used when GDPR is enabled
        data_consent = Consent()

        data_consent.set_consent_remarks("Approved.")

        data_consent.set_consent_through('Email')

        data_consent.set_contact_through_email(True)

        data_consent.set_contact_through_social(False)

        record.add_key_value('Data_Processing_Basis_Details', data_consent)

        """
		Following methods are being used only by Inventory modules
		"""
        deal_name = ZCRMRecord()

        deal_name.add_field_value(Field.Deals.id(), 347706112416012)

        record.add_field_value(Field.Sales_Orders.deal_name(), deal_name)

        contact_name = ZCRMRecord()

        contact_name.add_field_value(Field.Contacts.id(), 347706112263005)

        record.add_field_value(Field.Sales_Orders.contact_name(), contact_name)

        account_name = ZCRMRecord()

        # account_name.add_field_value(Field.Accounts.id(), 34096430692007)

        account_name.add_key_value("name", "automatedAccount")

        record.add_field_value(Field.Sales_Orders.account_name(), account_name)

        record.add_key_value("Discount", 10.5)

        inventory_line_item_list = []

        inventory_line_item = ZCRMRecord()

        line_item_product = LineItemProduct()

        line_item_product.set_id(347706112402032)

        # line_item_product.add_key_value("Products_External", "ProductExternal")

        inventory_line_item.add_key_value("Product_Name", line_item_product)

        inventory_line_item.add_key_value("Quantity", 3.0)

        inventory_line_item.add_key_value("Description", 'productDescription')

        inventory_line_item.add_key_value("ListPrice", 10.0)

        inventory_line_item.add_key_value("Discount", '5.90')

        product_line_taxes = []

        product_line_tax = LineTax()

        product_line_tax.set_name('MyTax1134')

        product_line_tax.set_percentage(12.1)

        product_line_taxes.append(product_line_tax)

        inventory_line_item.add_key_value("Line_Tax", product_line_taxes)

        inventory_line_item_list.append(inventory_line_item)

        record.add_key_value('Quoted_Items', inventory_line_item_list)

        record.add_field_value(Field.Quotes.subject(), "Python- testing")

        line_taxes = []

        line_tax = LineTax()

        line_tax.set_name('MyTax1134')

        line_tax.set_percentage(5.0)

        line_taxes.append(line_tax)

        record.add_key_value("$line_tax", line_taxes)

        vendor_name = ZCRMRecord()

        vendor_name.set_id(34770614996051)

        record.add_field_value(
            Field.Purchase_Orders.vendor_name(), vendor_name)

        """
		End Inventory
		"""

        # Add Record instance to the list
        records_list.append(record)

        # Set the list to data in BodyWrapper instance
        request.set_data(records_list)

        trigger = ["approval", "workflow", "blueprint"]

        # Set the list containing the trigger operations to be run
        request.set_trigger(trigger)

        header_instance = HeaderMap()

        # header_instance.add(UpdateRecordHeader.x_external, "Leads.External")
        # header_instance.add(UpdateRecordHeader.x_external, "Quotes.Quoted_Items.Product_Name.Products_External")

        # Call updateRecord method that takes record_id, module_api_name, BodyWrapper instance and header_instance as parameter.
        response = record_operations.update_record(
            record_id, module_api_name, request, header_instance)

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
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

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
    def delete_record(module_api_name, record_id):
        """
		This method is used to delete a single record of a module with ID and print the response.
		:param module_api_name: The API Name of the record's module.
		:param record_id: The ID of the record to be deleted
		"""

        """
		example
		module_api_name = 'Leads'
		record_id = 34770616603276
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Delete Record operation
        param_instance.add(DeleteRecordParam.wf_trigger, True)

        header_instance = HeaderMap()

        # header_instance.add(DeleteRecordHeader.x_external, "Leads.External")

        # Call deleteRecord method that takes record_id, module_api_name, param_instance and header_instance as parameter.
        response = record_operations.delete_record(
            record_id, module_api_name, param_instance, header_instance)

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
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

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
    def get_record_using_external_id(module_api_name, external_field_value, destination_folder):
        """
		This method is used to get a single record of a module with ID and print the response.
		:param module_api_name: The API Name of the record's module.
		:param external_field_value:
		:param destination_folder: The absolute path of the destination folder to store the downloaded attachment Record
		"""

        """
		example
		module_api_name = 'Leads'
		external_field_value = '34770616603276'
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Get Record operation
        # param_instance.add(GetRecordParam.cvid, '34096430087501')

        # param_instance.add(GetRecordParam.approved, 'true')

        # param_instance.add(GetRecordParam.converted, 'both')

        # fields = ['id', 'company']

        # for field in fields:
        #     param_instance.add(GetRecordParam.fields, field)

        # start_date_time = datetime(2020, 1, 1, 10, 10, 10)

        # param_instance.add(GetRecordParam.startdatetime, start_date_time)

        # end_date_time = datetime(2020, 7, 7, 10, 10, 10)

        # param_instance.add(GetRecordParam.enddatetime, end_date_time)

        # param_instance.add(GetRecordParam.territory_id, '34096430505351')

        # param_instance.add(GetRecordParam.include_child, 'true')

        # param_instance.add(GetRecordParam.uid, '34096430500741')

        # Get instance of HeaderMap Class
        header_instance = HeaderMap()

        # Possible headers for Get Record operation
        # header_instance.add(GetRecordHeader.if_modified_since, datetime.now())

        header_instance.add(GetRecordHeader.x_external, "Leads.External")

        # Call get_record_using_external_id method that takes external_field_value, module_api_name, param_instance and header_instance as parameter
        response = record_operations.get_record_using_external_id(external_field_value, module_api_name, param_instance,
                                                                  header_instance)

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

                # Check if expected ResponseWrapper instance is received.
                if isinstance(response_object, ResponseWrapper):

                    # Get the list of obtained Record instances
                    record_list = response_object.get_data()

                    for record in record_list:
                        # Get the ID of each Record
                        print("Record ID: " + str(record.get_id()))

                        # Get the createdBy User instance of each Record
                        created_by = record.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Record Created By - Name: " +
                                  created_by.get_name())

                            # Get the ID of the created_by User
                            print("Record Created By - ID: " +
                                  str(created_by.get_id()))

                            # Get the Email of the created_by User
                            print("Record Created By - Email: " +
                                  created_by.get_email())

                        # Get the CreatedTime of each Record
                        print("Record CreatedTime: " +
                              str(record.get_created_time()))

                        if record.get_modified_time() is not None:
                            # Get the ModifiedTime of each Record
                            print("Record ModifiedTime: " +
                                  str(record.get_modified_time()))

                        # Get the modified_by User instance of each Record
                        modified_by = record.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modified_by User
                            print("Record Modified By - Name: " +
                                  modified_by.get_name())

                            # Get the ID of the modified_by User
                            print("Record Modified By - ID: " +
                                  str(modified_by.get_id()))

                            # Get the Email of the modified_by User
                            print("Record Modified By - Email: " +
                                  modified_by.get_email())

                        # Get the list of obtained Tag instance of each Record
                        tags = record.get_tag()

                        if tags is not None:
                            for tag in tags:
                                # Get the Name of each Tag
                                print("Record Tag Name: " + tag.get_name())

                                # Get the Id of each Tag
                                print("Record Tag ID: " + str(tag.get_id()))

                        # To get particular field value
                        print("Record Field Value: " +
                              str(record.get_key_value('Last_Name')))

                        print('Record KeyValues: ')

                        key_values = record.get_key_values()

                        for key_name, value in key_values.items():

                            if isinstance(value, list):

                                if len(value) > 0:

                                    if isinstance(value[0], FileDetails):
                                        file_details = value

                                        for file_detail in file_details:
                                            # Get the Extn of each FileDetails
                                            print(
                                                "Record FileDetails Extn: " + file_detail.get_extn())

                                            # Get the IsPreviewAvailable of each FileDetails
                                            print("Record FileDetails IsPreviewAvailable: " + str(
                                                file_detail.get_is_preview_available()))

                                            # Get the DownloadUrl of each FileDetails
                                            print(
                                                "Record FileDetails DownloadUrl: " + file_detail.get_download_url())

                                            # Get the DeleteUrl of each FileDetails
                                            print(
                                                "Record FileDetails DeleteUrl: " + file_detail.get_delete_url())

                                            # Get the EntityId of each FileDetails
                                            print(
                                                "Record FileDetails EntityId: " + file_detail.get_entity_id())

                                            # Get the Mode of each FileDetails
                                            print(
                                                "Record FileDetails Mode: " + file_detail.get_mode())

                                            # Get the OriginalSizeByte of each FileDetails
                                            print(
                                                "Record FileDetails OriginalSizeByte: " + file_detail.get_original_size_byte())

                                            # Get the PreviewUrl of each FileDetails
                                            print(
                                                "Record FileDetails PreviewUrl: " + file_detail.get_preview_url())

                                            # Get the FileName of each FileDetails
                                            print(
                                                "Record FileDetails FileName: " + file_detail.get_file_name())

                                            # Get the FileId of each FileDetails
                                            print(
                                                "Record FileDetails FileId: " + file_detail.get_file_id())

                                            # Get the AttachmentId of each FileDetails
                                            print(
                                                "Record FileDetails AttachmentId: " + file_detail.get_attachment_id())

                                            # Get the FileSize of each FileDetails
                                            print(
                                                "Record FileDetails FileSize: " + file_detail.get_file_size())

                                            # Get the CreatorId of each FileDetails
                                            print(
                                                "Record FileDetails CreatorId: " + file_detail.get_creator_id())

                                            # Get the LinkDocs of each FileDetails
                                            print(
                                                "Record FileDetails LinkDocs: " + str(file_detail.get_link_docs()))

                                    elif isinstance(value[0], Reminder):
                                        reminders = value

                                        for reminder in reminders:
                                            # Get the Reminder Period
                                            print("Reminder Period: " +
                                                  reminder.get_period())

                                            # Get the Reminder Unit
                                            print("Reminder Unit: " +
                                                  reminder.get_unit())

                                    elif isinstance(value[0], Choice):
                                        choice_list = value

                                        print(key_name)

                                        print('Values')

                                        for choice in choice_list:
                                            print(choice.get_value())

                                    elif isinstance(value[0], Participants):
                                        participants = value

                                        for participant in participants:
                                            print("Record Participants Name: ")
                                            print(participant.get_name())

                                            print(
                                                "Record Participants Invited: " + str(participant.get_invited()))

                                            print(
                                                "Record Participants Type: " + participant.get_type())

                                            print(
                                                "Record Participants Participant: " + participant.get_participant())

                                            print(
                                                "Record Participants Status: " + participant.get_status())

                                    elif isinstance(value[0], ImageUpload):
                                        image_uploads = value

                                        for image_upload in image_uploads:
                                            print("Record  Id: " +
                                                  str(image_upload.get_id()))

                                            print("Record  FileId: " +
                                                  image_upload.get_file_id())

                                            print(
                                                "Record  SequenceNumber: " + str(image_upload.get_sequence_number()))

                                            print("Record  Size: " +
                                                  str(image_upload.get_size()))

                                            print("Record  State: " +
                                                  str(image_upload.get_state()))

                                            print("Record  File_Name: " +
                                                  image_upload.get_file_name())

                                            print("Record  PreviewId: " +
                                                  image_upload.get_preview_id())

                                            print("Record  Description: " +
                                                  str(image_upload.get_description()))

                                    elif isinstance(value[0], Tax):
                                        tax = value[0]

                                        print("Record Tax Name: " +
                                              tax.get_value())

                                        print("Record Tax ID: " +
                                              str(tax.get_id()))

                                    elif isinstance(value[0], ImageUpload):
                                        image_uploads = value

                                        for image_upload in image_uploads:
                                            print("RelatedRecord  Id: " +
                                                  str(image_upload.get_id()))

                                            print("RelatedRecord  FileId: " +
                                                  image_upload.get_file_id())

                                            print(
                                                "RelatedRecord  SequenceNumber: " + image_upload.get_sequence_number())

                                            print("RelatedRecord  Size: " +
                                                  str(image_upload.get_size()))

                                            print("RelatedRecord  State: " +
                                                  str(image_upload.get_state()))

                                            print(
                                                "RelatedRecord  File_Name: " + image_upload.get_file_name())

                                            print(
                                                "RelatedRecord  PreviewId: " + image_upload.get_preview_id())

                                            print(
                                                "RelatedRecord  Description: " + str(image_upload.get_description()))

                                    elif isinstance(value[0], Tag):
                                        tags = value

                                        if tags is not None:
                                            for tag in tags:
                                                print(
                                                    "Record Tag Name: " + tag.get_name())

                                                print("Record Tag ID: " +
                                                      str(tag.get_id()))

                                    elif isinstance(value[0], PricingDetails):
                                        pricing_details = value

                                        for pricing_detail in pricing_details:
                                            print(
                                                "Record PricingDetails ToRange: " + str(pricing_detail.get_to_range()))

                                            print(
                                                "Record PricingDetails Discount: " + str(pricing_detail.get_discount()))

                                            print(
                                                "Record PricingDetails ID: " + str(pricing_detail.get_id()))

                                            print("Record PricingDetails FromRange: " + str(
                                                pricing_detail.get_from_range()))

                                    elif isinstance(value[0], ZCRMRecord):
                                        record_list = value

                                        for each_record in record_list:
                                            for key, val in each_record.get_key_values().items():
                                                print(
                                                    str(key) + " : " + str(val))

                                    elif isinstance(value[0], LineTax):
                                        line_taxes = value

                                        for line_tax in line_taxes:
                                            print("Record LineTax Percentage: " + str(
                                                line_tax.get_percentage()))

                                            print(
                                                "Record LineTax Name: " + line_tax.get_name())

                                            print("Record LineTax Id: " +
                                                  str(line_tax.get_id()))

                                            print("Record LineTax Value: " +
                                                  str(line_tax.get_value()))

                                    elif isinstance(value[0], Comment):
                                        comments = value

                                        for comment in comments:
                                            print("Comment-ID: " +
                                                  str(comment.get_id()))

                                            print("Comment-Content: " +
                                                  comment.get_comment_content())

                                            print("Comment-Commented_By: " +
                                                  comment.get_commented_by())

                                            print("Comment-Commented Time: " +
                                                  str(comment.get_commented_time()))

                                    elif isinstance(value[0], Attachment):
                                        attachments = value

                                        for attachment in attachments:
                                            # Get the ID of each attachment
                                            print('Record Attachment ID : ' +
                                                  str(attachment.get_id()))

                                            # Get the owner User instance of each attachment
                                            owner = attachment.get_owner()

                                            # Check if owner is not None
                                            if owner is not None:
                                                # Get the Name of the Owner
                                                print(
                                                    "Record Attachment Owner - Name: " + owner.get_name())

                                                # Get the ID of the Owner
                                                print(
                                                    "Record Attachment Owner - ID: " + str(owner.get_id()))

                                                # Get the Email of the Owner
                                                print(
                                                    "Record Attachment Owner - Email: " + owner.get_email())

                                            # Get the modified time of each attachment
                                            print("Record Attachment Modified Time: " + str(
                                                attachment.get_modified_time()))

                                            # Get the name of the File
                                            print(
                                                "Record Attachment File Name: " + attachment.get_file_name())

                                            # Get the created time of each attachment
                                            print(
                                                "Record Attachment Created Time: " + str(attachment.get_created_time()))

                                            # Get the Attachment file size
                                            print(
                                                "Record Attachment File Size: " + str(attachment.get_size()))

                                            # Get the parentId Record instance of each attachment
                                            parent_id = attachment.get_parent_id()

                                            if parent_id is not None:
                                                # Get the parent record Name of each attachment
                                                print(
                                                    "Record Attachment parent record Name: ")
                                                print(
                                                    parent_id.get_key_value("name"))

                                                # Get the parent record ID of each attachment
                                                print(
                                                    "Record Attachment parent record ID: " + str(parent_id.get_id()))

                                            # Check if the attachment is Editable
                                            print(
                                                "Record Attachment is Editable: " + str(attachment.get_editable()))

                                            # Get the file ID of each attachment
                                            print(
                                                "Record Attachment File ID: " + str(attachment.get_file_id()))

                                            # Get the type of each attachment
                                            print(
                                                "Record Attachment File Type: " + str(attachment.get_type()))

                                            # Get the seModule of each attachment
                                            print(
                                                "Record Attachment seModule: " + str(attachment.get_se_module()))

                                            # Get the modifiedBy User instance of each attachment
                                            modified_by = attachment.get_modified_by()

                                            # Check if modifiedBy is not None
                                            if modified_by is not None:
                                                # Get the Name of the modifiedBy User
                                                print(
                                                    "Record Attachment Modified By - Name: " + modified_by.get_name())

                                                # Get the ID of the modifiedBy User
                                                print(
                                                    "Record Attachment Modified By - ID: " + str(modified_by.get_id()))

                                                # Get the Email of the modifiedBy User
                                                print(
                                                    "Record Attachment Modified By - Email: " + modified_by.get_email())

                                            # Get the state of each attachment
                                            print(
                                                "Record Attachment State: " + attachment.get_state())

                                            # Get the modifiedBy User instance of each attachment
                                            created_by = attachment.get_created_by()

                                            # Check if created_by is not None
                                            if created_by is not None:
                                                # Get the Name of the modifiedBy User
                                                print(
                                                    "Record Attachment Created By - Name: " + created_by.get_name())

                                                # Get the ID of the modifiedBy User
                                                print(
                                                    "Record Attachment Created By - ID: " + str(created_by.get_id()))

                                                # Get the Email of the modifiedBy User
                                                print(
                                                    "Record Attachment Created By - Email: " + created_by.get_email())

                                            # Get the linkUrl of each attachment
                                            print(
                                                "Record Attachment LinkUrl: " + str(attachment.get_link_url()))

                                    else:
                                        print(key_name)

                                        for each_value in value:
                                            print(str(each_value))

                            elif isinstance(value, User):
                                print("Record " + key_name +
                                      " User-ID: " + str(value.get_id()))

                                print("Record " + key_name +
                                      " User-Name: " + value.get_name())

                                print("Record " + key_name +
                                      " User-Email: " + value.get_email())

                            elif isinstance(value, Layout):
                                print(key_name + " ID: " + str(value.get_id()))

                                print(key_name + " Name: " + value.get_name())

                            elif isinstance(value, ZCRMRecord):
                                print(key_name + " Record ID: " +
                                      str(value.get_id()))

                                print(key_name + " Record Name: " +
                                      value.get_key_value('name'))

                            elif isinstance(value, Choice):
                                print(key_name + " : " + value.get_value())

                            elif isinstance(value, RemindAt):
                                print(key_name + " : " + value.get_alarm())

                            elif isinstance(value, RecurringActivity):
                                print(key_name)

                                print("RRULE: " + value.get_rrule())

                            elif isinstance(value, Consent):
                                print("Record Consent ID: " +
                                      str(value.get_id()))

                                # Get the createdBy User instance of each Record
                                created_by = value.get_created_by()

                                # Check if created_by is not None
                                if created_by is not None:
                                    # Get the Name of the created_by User
                                    print(
                                        "Record Consent Created By - Name: " + created_by.get_name())

                                    # Get the ID of the created_by User
                                    print(
                                        "Record Consent Created By - ID: " + str(created_by.get_id()))

                                    # Get the Email of the created_by User
                                    print(
                                        "Record Consent Created By - Email: " + created_by.get_email())

                                # Get the CreatedTime of each Record
                                print("Record Consent CreatedTime: " +
                                      str(value.get_created_time()))

                                if value.get_modified_time() is not None:
                                    # Get the ModifiedTime of each Record
                                    print("Record Consent ModifiedTime: " +
                                          str(value.get_modified_time()))

                                # Get the Owner User instance of the Consent
                                owner = value.get_owner()

                                if owner is not None:
                                    # Get the Name of the Owner User
                                    print(
                                        "Record Consent Created By - Name: " + owner.get_name())

                                    # Get the ID of the Owner User
                                    print(
                                        "Record Consent Created By - ID: " + str(owner.get_id()))

                                    # Get the Email of the Owner User
                                    print(
                                        "Record Consent Created By - Email: " + owner.get_email())

                                print("Record Consent ContactThroughEmail: " +
                                      str(value.get_contact_through_email()))

                                print("Record Consent ContactThroughSocial: " +
                                      str(value.get_contact_through_social()))

                                print("Record Consent ContactThroughSurvey: " +
                                      str(value.get_contact_through_survey()))

                                print("Record Consent ContactThroughPhone: " +
                                      str(value.get_contact_through_phone()))

                                print("Record Consent MailSentTime: " +
                                      str(value.get_mail_sent_time()))

                                print("Record Consent ConsentDate: " +
                                      str(value.get_consent_date()))

                                print("Record Consent ConsentRemarks: " +
                                      value.get_consent_remarks())

                                print("Record Consent ConsentThrough: " +
                                      value.get_consent_through())

                                print("Record Consent DataProcessingBasis: " +
                                      value.get_data_processing_basis())

                                # To get custom values
                                print("Record Consent Lawful Reason: " +
                                      str(value.get_key_value("Lawful_Reason")))

                            elif isinstance(value, dict):
                                for key, val in value.items():
                                    print(key + " : " + str(val))

                            else:
                                print(key_name + " : " + str(value))

                # Check if expected FileBodyWrapper instance is received.
                elif isinstance(response_object, FileBodyWrapper):

                    # Get StreamWrapper instance from the returned FileBodyWrapper instance
                    stream_wrapper = response_object.get_file()

                    # Construct the file name by joining the destinationFolder and the name from StreamWrapper instance
                    file_name = os.path.join(
                        destination_folder, stream_wrapper.get_name())

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

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def update_record_using_external_id(module_api_name, external_field_value):
        """
		This method is used to update a single record of a module with ID and print the response.
		:param module_api_name: The API Name of the record's module.
		:param external_field_value:
		"""

        """
		example
		module_api_name = 'Leads'
		external_field_value = '34770616603276'
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Record instances
        records_list = []

        # Get instance of Record Class
        record = ZCRMRecord()

        # Value to Record's fields can be provided in any of the following ways

        """
		Call add_field_value method that takes two arguments
		Import the zcrmsdk.src.com.zoho.crm.api.record.field file
		1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field name from the displayed list.
		2 -> Value
		"""

        record.add_field_value(Field.Leads.last_name(), 'Python SDK')

        record.add_field_value(Field.Leads.first_name(), 'New')

        record.add_field_value(Field.Leads.company(), 'Zoho')

        record.add_field_value(Field.Leads.city(), 'City')

        """
		Call add_key_value method that takes two arguments
		1 -> A string that is the Field's API Name
		2 -> Value
		"""

        record.add_key_value('Custom_field', 'Value')

        record.add_key_value('Custom_field_2', 12)

        # record.add_key_value('Date', date(2020, 4, 9))

        record.add_key_value('Discounted', 23.34)

        file_details = []

        file_detail = FileDetails()

        file_detail.set_file_id(
            '479f0f5eebf0fb982f99e3832b35d23e29f67c2868ee4c789f22579895383c8')

        file_details.append(file_detail)

        record.add_key_value('File_Upload', file_details)

        record_owner = User()

        record_owner.set_email("abc@zoho.com")

        record.add_key_value("Owner", record_owner)

        # Used when GDPR is enabled
        data_consent = Consent()

        data_consent.set_consent_remarks("Approved.")

        data_consent.set_consent_through('Email')

        data_consent.set_contact_through_email(True)

        data_consent.set_contact_through_social(False)

        record.add_key_value('Data_Processing_Basis_Details', data_consent)

        """
		Following methods are being used only by Inventory modules
		"""
        deal_name = ZCRMRecord()

        deal_name.add_field_value(Field.Deals.id(), 347706112416012)

        record.add_field_value(Field.Sales_Orders.deal_name(), deal_name)

        contact_name = ZCRMRecord()

        contact_name.add_field_value(Field.Contacts.id(), 347706112263005)

        record.add_field_value(Field.Sales_Orders.contact_name(), contact_name)

        account_name = ZCRMRecord()

        # account_name.add_field_value(Field.Accounts.id(), 34096430692007)

        account_name.add_key_value("name", "automatedAccount")

        record.add_field_value(Field.Sales_Orders.account_name(), account_name)

        record.add_key_value("Discount", 10.5)

        inventory_line_item_list = []

        inventory_line_item = ZCRMRecord()

        line_item_product = LineItemProduct()

        # line_item_product.set_id(347706112402032)

        line_item_product.add_key_value("Products_External", "ProductExternal")

        inventory_line_item.add_key_value("Product_Name", line_item_product)

        inventory_line_item.add_key_value("Quantity", 3.0)

        inventory_line_item.add_key_value("Description", 'productDescription')

        inventory_line_item.add_key_value("ListPrice", 10.0)

        inventory_line_item.add_key_value("Discount", '5.90')

        product_line_taxes = []

        product_line_tax = LineTax()

        product_line_tax.set_name('MyTax1134')

        product_line_tax.set_percentage(12.1)

        product_line_taxes.append(product_line_tax)

        inventory_line_item.add_key_value("Line_Tax", product_line_taxes)

        inventory_line_item_list.append(inventory_line_item)

        record.add_key_value('Quoted_Items', inventory_line_item_list)

        record.add_field_value(Field.Quotes.subject(), "Python- testing")

        line_taxes = []

        line_tax = LineTax()

        line_tax.set_name('MyTax1134')

        line_tax.set_percentage(5.0)

        line_taxes.append(line_tax)

        record.add_key_value("$line_tax", line_taxes)

        vendor_name = ZCRMRecord()

        vendor_name.set_id(34770614996051)

        # record.add_field_value(Field.Purchase_Orders.vendor_name(), vendor_name)

        """
		End Inventory
		"""

        # Add Record instance to the list
        records_list.append(record)

        # Set the list to data in BodyWrapper instance
        request.set_data(records_list)

        trigger = ["approval", "workflow", "blueprint"]

        # Set the list containing the trigger operations to be run
        request.set_trigger(trigger)

        header_instance = HeaderMap()

        # header_instance.add(UpdateRecordHeader.x_external, "Leads.External")
        header_instance.add(UpdateRecordHeader.x_external,
                            "Quotes.Quoted_Items.Product_Name.Products_External")

        # Call update_record_using_external_id method that takes external_field_value, module_api_name, BodyWrapper instance and header_instance as parameter.
        response = record_operations.update_record_using_external_id(external_field_value, module_api_name, request,
                                                                     header_instance)

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
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

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
    def delete_record_using_external_id(module_api_name, external_field_value):
        """
		This method is used to delete a single record of a module with ID and print the response.
		:param module_api_name: The API Name of the record's module.
		:param external_field_value:
		"""

        """
		example
		module_api_name = 'Leads'
		external_field_value = '34770616603276'
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Delete Record operation
        param_instance.add(DeleteRecordParam.wf_trigger, True)

        header_instance = HeaderMap()

        header_instance.add(DeleteRecordHeader.x_external, "Leads.External")

        # Call delete_record_using_external_id method that takes external_field_value, module_api_name, param_instance and header_instance as parameter.
        response = record_operations.delete_record_using_external_id(external_field_value, module_api_name,
                                                                     param_instance, header_instance)

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
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

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
    def get_records(module_api_name):
        """
		This method is used to get all the records of a module and print the response.
		:param module_api_name: The API Name of the module to fetch records
		"""

        """
		example
		module_api_name = 'Leads'
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Get Records operation
        param_instance.add(GetRecordsParam.page, 1)

        param_instance.add(GetRecordsParam.per_page, 120)

        param_instance.add(GetRecordsParam.approved, 'both')

        param_instance.add(GetRecordsParam.converted, 'both')

        param_instance.add(GetRecordsParam.cvid, '34096430087501')

        ids = ["External1256", "34770614352001"]
        for each_id in ids:
            param_instance.add(GetRecordsParam.ids, each_id)

        param_instance.add(GetRecordsParam.uid, '34096430302031')

        field_names = ["Company", "Email"]

        for field in field_names:
            param_instance.add(GetRecordsParam.fields, field)

        param_instance.add(GetRecordsParam.sort_by, 'Email')

        param_instance.add(GetRecordsParam.sort_order, 'desc')

        start_date_time = datetime(2020, 1, 1, 0, 0, 0)

        param_instance.add(GetRecordsParam.startdatetime, start_date_time)

        end_date_time = datetime(2020, 7, 1, 0, 0, 0)

        param_instance.add(GetRecordsParam.enddatetime, end_date_time)

        param_instance.add(GetRecordsParam.territory_id, '34096430505351')

        param_instance.add(GetRecordsParam.include_child, "true")

        # Get instance of HeaderMap Class
        header_instance = HeaderMap()

        # Possible headers for Get Records operation
        header_instance.add(GetRecordsHeader.if_modified_since,
                            datetime.fromisoformat('2020-01-01T00:00:00+05:30'))

        # header_instance.add(GetRecordsHeader.x_external, "Leads.External")

        # Call get_records method that takes ParameterMap Instance, HeaderMap Instance and module_api_name as parameters
        response = record_operations.get_records(
            module_api_name, param_instance, header_instance)

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

                # Check if expected ResponseWrapper instance is received.
                if isinstance(response_object, ResponseWrapper):

                    # Get the list of obtained Record instances
                    record_list = response_object.get_data()

                    for record in record_list:
                        # Get the ID of each Record
                        print("Record ID: " + str(record.get_id()))

                        # Get the createdBy User instance of each Record
                        created_by = record.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Record Created By - Name: " +
                                  created_by.get_name())

                            # Get the ID of the created_by User
                            print("Record Created By - ID: " +
                                  str(created_by.get_id()))

                            # Get the Email of the created_by User
                            print("Record Created By - Email: " +
                                  created_by.get_email())

                        # Get the CreatedTime of each Record
                        print("Record CreatedTime: " +
                              str(record.get_created_time()))

                        if record.get_modified_time() is not None:
                            # Get the ModifiedTime of each Record
                            print("Record ModifiedTime: " +
                                  str(record.get_modified_time()))

                        # Get the modified_by User instance of each Record
                        modified_by = record.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modified_by User
                            print("Record Modified By - Name: " +
                                  modified_by.get_name())

                            # Get the ID of the modified_by User
                            print("Record Modified By - ID: " +
                                  str(modified_by.get_id()))

                            # Get the Email of the modified_by User
                            print("Record Modified By - Email: " +
                                  modified_by.get_email())

                        # Get the list of obtained Tag instance of each Record
                        tags = record.get_tag()

                        if tags is not None:
                            for tag in tags:
                                # Get the Name of each Tag
                                print("Record Tag Name: " + tag.get_name())

                                # Get the Id of each Tag
                                print("Record Tag ID: " + str(tag.get_id()))

                        # To get particular field value
                        print("Record Field Value: " +
                              str(record.get_key_value('Last_Name')))

                        print('Record KeyValues: ')

                        key_values = record.get_key_values()

                        for key_name, value in key_values.items():

                            if isinstance(value, list):

                                if len(value) > 0:

                                    if isinstance(value[0], FileDetails):
                                        file_details = value

                                        for file_detail in file_details:
                                            # Get the Extn of each FileDetails
                                            print(
                                                "Record FileDetails Extn: " + file_detail.get_extn())

                                            # Get the IsPreviewAvailable of each FileDetails
                                            print("Record FileDetails IsPreviewAvailable: " + str(
                                                file_detail.get_is_preview_available()))

                                            # Get the DownloadUrl of each FileDetails
                                            print(
                                                "Record FileDetails DownloadUrl: " + file_detail.get_download_url())

                                            # Get the DeleteUrl of each FileDetails
                                            print(
                                                "Record FileDetails DeleteUrl: " + file_detail.get_delete_url())

                                            # Get the EntityId of each FileDetails
                                            print(
                                                "Record FileDetails EntityId: " + file_detail.get_entity_id())

                                            # Get the Mode of each FileDetails
                                            print(
                                                "Record FileDetails Mode: " + file_detail.get_mode())

                                            # Get the OriginalSizeByte of each FileDetails
                                            print(
                                                "Record FileDetails OriginalSizeByte: " + file_detail.get_original_size_byte())

                                            # Get the PreviewUrl of each FileDetails
                                            print(
                                                "Record FileDetails PreviewUrl: ")
                                            print(file_detail.get_preview_url())

                                            # Get the FileName of each FileDetails
                                            print(
                                                "Record FileDetails FileName: " + file_detail.get_file_name())

                                            # Get the FileId of each FileDetails
                                            print(
                                                "Record FileDetails FileId: " + file_detail.get_file_id())

                                            # Get the AttachmentId of each FileDetails
                                            print(
                                                "Record FileDetails AttachmentId: " + file_detail.get_attachment_id())

                                            # Get the FileSize of each FileDetails
                                            print(
                                                "Record FileDetails FileSize: " + file_detail.get_file_size())

                                            # Get the CreatorId of each FileDetails
                                            print(
                                                "Record FileDetails CreatorId: " + file_detail.get_creator_id())

                                            # Get the LinkDocs of each FileDetails
                                            print(
                                                "Record FileDetails LinkDocs: ")
                                            print(file_detail.get_link_docs())

                                    elif isinstance(value[0], Reminder):
                                        reminders = value

                                        for reminder in reminders:
                                            # Get the Reminder Period
                                            print("Reminder Period: " +
                                                  reminder.get_period())

                                            # Get the Reminder Unit
                                            print("Reminder Unit: " +
                                                  reminder.get_unit())

                                    elif isinstance(value[0], Choice):
                                        choice_list = value

                                        print(key_name)

                                        print('Values')

                                        for choice in choice_list:
                                            print(choice.get_value())

                                    elif isinstance(value[0], Participants):
                                        participants = value

                                        for participant in participants:
                                            print("Record Participants Name: ")
                                            print(participant.get_name())

                                            print(
                                                "Record Participants Invited: " + str(participant.get_invited()))

                                            print(
                                                "Record Participants Type: " + participant.get_type())

                                            print(
                                                "Record Participants Participant: " + participant.get_participant())

                                            print(
                                                "Record Participants Status: " + participant.get_status())

                                    elif isinstance(value[0], ImageUpload):
                                        image_uploads = value

                                        for image_upload in image_uploads:
                                            print("Record  Id: " +
                                                  str(image_upload.get_id()))

                                            print("Record  FileId: " +
                                                  image_upload.get_file_id())

                                            print(
                                                "Record  SequenceNumber: " + str(image_upload.get_sequence_number()))

                                            print("Record  Size: " +
                                                  str(image_upload.get_size()))

                                            print("Record  State: " +
                                                  str(image_upload.get_state()))

                                            print("Record  File_Name: " +
                                                  image_upload.get_file_name())

                                            print("Record  PreviewId: " +
                                                  image_upload.get_preview_id())

                                            print("Record  Description: " +
                                                  str(image_upload.get_description()))

                                    elif isinstance(value[0], Tax):
                                        tax = value[0]

                                        print("Record Tax Name: " +
                                              tax.get_value())

                                        print("Record Tax ID: " +
                                              str(tax.get_id()))

                                    elif isinstance(value[0], Tag):
                                        tags = value

                                        if tags is not None:
                                            for tag in tags:
                                                print(
                                                    "Record Tag Name: " + tag.get_name())

                                                print("Record Tag ID: " +
                                                      str(tag.get_id()))
                                    elif isinstance(value[0], ImageUpload):
                                        image_uploads = value

                                        for image_upload in image_uploads:
                                            print("RelatedRecord  Id: " +
                                                  str(image_upload.get_id()))

                                            print("RelatedRecord  FileId: " +
                                                  image_upload.get_file_id())

                                            print(
                                                "RelatedRecord  SequenceNumber: " + image_upload.get_sequence_number())

                                            print("RelatedRecord  Size: " +
                                                  str(image_upload.get_size()))

                                            print("RelatedRecord  State: " +
                                                  str(image_upload.get_state()))

                                            print(
                                                "RelatedRecord  File_Name: " + image_upload.get_file_name())

                                            print(
                                                "RelatedRecord  PreviewId: " + image_upload.get_preview_id())

                                            print(
                                                "RelatedRecord  Description: " + str(image_upload.get_description()))

                                    elif isinstance(value[0], PricingDetails):
                                        pricing_details = value

                                        for pricing_detail in pricing_details:
                                            print(
                                                "Record PricingDetails ToRange: " + str(pricing_detail.get_to_range()))

                                            print(
                                                "Record PricingDetails Discount: " + str(pricing_detail.get_discount()))

                                            print(
                                                "Record PricingDetails ID: " + str(pricing_detail.get_id()))

                                            print("Record PricingDetails FromRange: " + str(
                                                pricing_detail.get_from_range()))

                                    elif isinstance(value[0], ZCRMRecord):
                                        record_list = value

                                        for each_record in record_list:
                                            for key, val in each_record.get_key_values().items():
                                                print(
                                                    str(key) + " : " + str(val))

                                    elif isinstance(value[0], LineTax):
                                        line_taxes = value

                                        for line_tax in line_taxes:
                                            print("Record LineTax Percentage: " + str(
                                                line_tax.get_percentage()))

                                            print(
                                                "Record LineTax Name: " + line_tax.get_name())

                                            print("Record LineTax Id: " +
                                                  str(line_tax.get_id()))

                                            print("Record LineTax Value: " +
                                                  str(line_tax.get_value()))

                                    elif isinstance(value[0], Comment):
                                        comments = value

                                        for comment in comments:
                                            print("Comment-ID: " +
                                                  str(comment.get_id()))

                                            print(
                                                "Comment-Content: " + str(comment.get_comment_content()))

                                            print("Comment-Commented_By: " +
                                                  str(comment.get_commented_by()))

                                            print("Comment-Commented Time: " +
                                                  str(comment.get_commented_time()))

                                    elif isinstance(value[0], Attachment):
                                        attachments = value

                                        for attachment in attachments:
                                            # Get the ID of each attachment
                                            print('Record Attachment ID : ' +
                                                  str(attachment.get_id()))

                                            # Get the owner User instance of each attachment
                                            owner = attachment.get_owner()

                                            # Check if owner is not None
                                            if owner is not None:
                                                # Get the Name of the Owner
                                                print(
                                                    "Record Attachment Owner - Name: " + owner.get_name())

                                                # Get the ID of the Owner
                                                print(
                                                    "Record Attachment Owner - ID: " + str(owner.get_id()))

                                                # Get the Email of the Owner
                                                print(
                                                    "Record Attachment Owner - Email: " + owner.get_email())

                                            # Get the modified time of each attachment
                                            print("Record Attachment Modified Time: " + str(
                                                attachment.get_modified_time()))

                                            # Get the name of the File
                                            print(
                                                "Record Attachment File Name: " + attachment.get_file_name())

                                            # Get the created time of each attachment
                                            print(
                                                "Record Attachment Created Time: " + str(attachment.get_created_time()))

                                            # Get the Attachment file size
                                            print(
                                                "Record Attachment File Size: " + str(attachment.get_size()))

                                            # Get the parentId Record instance of each attachment
                                            parent_id = attachment.get_parent_id()

                                            if parent_id is not None:
                                                # Get the parent record Name of each attachment
                                                print(
                                                    "Record Attachment parent record Name: ")
                                                print(
                                                    parent_id.get_key_value("name"))

                                                # Get the parent record ID of each attachment
                                                print(
                                                    "Record Attachment parent record ID: " + str(parent_id.get_id()))

                                            # Check if the attachment is Editable
                                            print(
                                                "Record Attachment is Editable: " + str(attachment.get_editable()))

                                            # Get the file ID of each attachment
                                            print(
                                                "Record Attachment File ID: " + str(attachment.get_file_id()))

                                            # Get the type of each attachment
                                            print(
                                                "Record Attachment File Type: " + str(attachment.get_type()))

                                            # Get the seModule of each attachment
                                            print(
                                                "Record Attachment seModule: " + str(attachment.get_se_module()))

                                            # Get the modifiedBy User instance of each attachment
                                            modified_by = attachment.get_modified_by()

                                            # Check if modifiedBy is not None
                                            if modified_by is not None:
                                                # Get the Name of the modifiedBy User
                                                print(
                                                    "Record Attachment Modified By - Name: " + modified_by.get_name())

                                                # Get the ID of the modifiedBy User
                                                print(
                                                    "Record Attachment Modified By - ID: " + str(modified_by.get_id()))

                                                # Get the Email of the modifiedBy User
                                                print(
                                                    "Record Attachment Modified By - Email: " + modified_by.get_email())

                                            # Get the state of each attachment
                                            print(
                                                "Record Attachment State: " + attachment.get_state())

                                            # Get the modifiedBy User instance of each attachment
                                            created_by = attachment.get_created_by()

                                            # Check if created_by is not None
                                            if created_by is not None:
                                                # Get the Name of the modifiedBy User
                                                print(
                                                    "Record Attachment Created By - Name: " + created_by.get_name())

                                                # Get the ID of the modifiedBy User
                                                print(
                                                    "Record Attachment Created By - ID: " + str(created_by.get_id()))

                                                # Get the Email of the modifiedBy User
                                                print(
                                                    "Record Attachment Created By - Email: " + created_by.get_email())

                                            # Get the linkUrl of each attachment
                                            print(
                                                "Record Attachment LinkUrl: " + str(attachment.get_link_url()))

                                    else:
                                        print(key_name)

                                        for each_value in value:
                                            print(str(each_value))

                            elif isinstance(value, User):
                                print("Record " + key_name +
                                      " User-ID: " + str(value.get_id()))

                                print("Record " + key_name +
                                      " User-Name: " + value.get_name())

                                print("Record " + key_name +
                                      " User-Email: " + value.get_email())

                            elif isinstance(value, Layout):
                                print(key_name + " ID: " + str(value.get_id()))

                                print(key_name + " Name: " + value.get_name())

                            elif isinstance(value, ZCRMRecord):
                                print(key_name + " Record ID: " +
                                      str(value.get_id()))

                                print(key_name + " Record Name: ")
                                print(value.get_key_value('name'))

                            elif isinstance(value, Choice):
                                print(key_name + " : " + value.get_value())

                            elif isinstance(value, RemindAt):
                                print(key_name + " : " + value.get_alarm())

                            elif isinstance(value, RecurringActivity):
                                print(key_name)

                                print("RRULE: " + value.get_rrule())

                            elif isinstance(value, Consent):
                                print("Record Consent ID: " +
                                      str(value.get_id()))

                                # Get the createdBy User instance of each Record
                                created_by = value.get_created_by()

                                # Check if created_by is not None
                                if created_by is not None:
                                    # Get the Name of the created_by User
                                    print(
                                        "Record Consent Created By - Name: " + created_by.get_name())

                                    # Get the ID of the created_by User
                                    print(
                                        "Record Consent Created By - ID: " + str(created_by.get_id()))

                                    # Get the Email of the created_by User
                                    print(
                                        "Record Consent Created By - Email: " + created_by.get_email())

                                # Get the CreatedTime of each Record
                                print("Record Consent CreatedTime: " +
                                      str(value.get_created_time()))

                                if value.get_modified_time() is not None:
                                    # Get the ModifiedTime of each Record
                                    print("Record Consent ModifiedTime: " +
                                          str(value.get_modified_time()))

                                # Get the Owner User instance of the Consent
                                owner = value.get_owner()

                                if owner is not None:
                                    # Get the Name of the Owner User
                                    print(
                                        "Record Consent Created By - Name: " + owner.get_name())

                                    # Get the ID of the Owner User
                                    print(
                                        "Record Consent Created By - ID: " + str(owner.get_id()))

                                    # Get the Email of the Owner User
                                    print(
                                        "Record Consent Created By - Email: " + owner.get_email())

                                print("Record Consent ContactThroughEmail: " +
                                      str(value.get_contact_through_email()))

                                print("Record Consent ContactThroughSocial: " +
                                      str(value.get_contact_through_social()))

                                print("Record Consent ContactThroughSurvey: " +
                                      str(value.get_contact_through_survey()))

                                print("Record Consent ContactThroughPhone: " +
                                      str(value.get_contact_through_phone()))

                                print("Record Consent MailSentTime: " +
                                      str(value.get_mail_sent_time()))

                                print("Record Consent ConsentDate: " +
                                      str(value.get_consent_date()))

                                print("Record Consent ConsentRemarks: " +
                                      value.get_consent_remarks())

                                print("Record Consent ConsentThrough: " +
                                      value.get_consent_through())

                                print("Record Consent DataProcessingBasis: " +
                                      value.get_data_processing_basis())

                                # To get custom values
                                print("Record Consent Lawful Reason: " +
                                      str(value.get_key_value("Lawful_Reason")))

                            elif isinstance(value, dict):
                                for key, val in value.items():
                                    print(key + " : " + str(val))

                            else:
                                print(key_name + " : " + str(value))

                    info = response_object.get_info()

                    if info is not None:
                        if info.get_per_page() is not None:
                            # Get the PerPage from Info
                            print('Record Info PerPage: ' +
                                  str(info.get_per_page()))

                        if info.get_page() is not None:
                            # Get the Page from Info
                            print('Record Info Page: ' + str(info.get_page()))

                        if info.get_count() is not None:
                            # Get the Count from Info
                            print('Record Info Count: ' +
                                  str(info.get_count()))

                        if info.get_more_records() is not None:
                            # Get the MoreRecords from Info
                            print('Record Info MoreRecords: ' +
                                  str(info.get_more_records()))

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
    def create_records(module_api_name):
        """
		This method is used to create records of a module and print the response.
		:param module_api_name: The API Name of the module to create records.
		"""

        """
		example
		module_api_name = 'Leads'
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Record instances
        records_list = []

        # Get instance of Record Class
        record = ZCRMRecord()

        # Get the instance of ApplyFeatureExecution Class
        apply_feature_execution = ApplyFeatureExecution()

        # set name to instance of ApplyFeatureExecution Class
        apply_feature_execution.set_name("layout_rules")

        # Add instance of ApplyFeatureExecution to apply_feature_list
        apply_feature_list = []

        apply_feature_list.append(apply_feature_execution)

        # set the data to BodyWrapper instance
        request.set_apply_feature_execution(apply_feature_list)

        # Value to Record's fields can be provided in any of the following ways

        """
		Call add_field_value method that takes two arguments
		Import the zcrmsdk.src.com.zoho.crm.api.record.field file
		1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field name from the displayed list.
		2 -> Value
		"""

        record.add_field_value(Field.Leads.last_name(), 'Python SDK')

        record.add_field_value(Field.Leads.first_name(), 'New')

        record.add_field_value(Field.Leads.company(), 'Zoho')

        record.add_field_value(Field.Leads.city(), 'City')

        """
		Call add_key_value method that takes two arguments
		1 -> A string that is the Field's API Name
		2 -> Value
		"""

        record.add_key_value('Custom_field', 'Value')

        record.add_key_value('Custom_field_2', 12)

        record.add_key_value('Date', date(2020, 4, 9))

        record.add_key_value('Discounted', 23.34)

        image_upload = ImageUpload()

        image_upload.set_encrypted_id(
            "ae9c7cefa418aec1d6a5cc2d9ab35c32d59ef634d7e170aa54e793c5184e4b87")

        record.add_key_value("Image_Upload", [image_upload])

        file_details = []

        file_detail = FileDetails()

        file_detail.set_file_id(
            'ae9c7cefa418aec1d6a5cc2d9ab35c3275c7759e756bf64b45f5ff128f1411ff')

        file_details.append(file_detail)

        file_detail = FileDetails()

        file_detail.set_file_id(
            'ae9c7cefa418aec1d6a5cc2d9ab35c32cf280bd47dfa3664980ea1303d75859c')

        file_details.append(file_detail)

        file_detail = FileDetails()

        file_detail.set_file_id(
            '479f0f5eebf0fb982f99e3832b35d23e29f67c2868ee4c789f22579895383c8')

        file_details.append(file_detail)

        record.add_key_value('File_Upload', file_details)

        record_owner = User()

        record_owner.set_email("abc@zoho.com")

        record.add_key_value("Owner", record_owner)

        # Used when GDPR is enabled
        data_consent = Consent()

        data_consent.set_consent_remarks("Approved.")

        data_consent.set_consent_through('Email')

        data_consent.set_contact_through_email(True)

        data_consent.set_contact_through_social(False)

        record.add_key_value('Data_Processing_Basis_Details', data_consent)

        # Products
        tax = Tax()

        tax.set_value("MyTax1134 - 15.0 %")

        record.add_key_value("Tax", [tax])

        record.add_key_value("Product_Name", "AutomatedSDK")

        """
		Following methods are being used only by Inventory modules
		"""
        deal_name = ZCRMRecord()

        deal_name.add_field_value(Field.Deals.id(), 347706112416012)

        record.add_field_value(Field.Sales_Orders.deal_name(), deal_name)

        contact_name = ZCRMRecord()

        contact_name.add_field_value(Field.Contacts.id(), 347706112263005)

        record.add_field_value(Field.Sales_Orders.contact_name(), contact_name)

        account_name = ZCRMRecord()

        # account_name.add_field_value(Field.Accounts.id(), 34096430692007)

        account_name.add_key_value("name", "automatedAccount")

        record.add_field_value(Field.Sales_Orders.account_name(), account_name)

        record.add_key_value("Discount", 10.5)

        inventory_line_item_list = []

        inventory_line_item = ZCRMRecord()

        line_item_product = LineItemProduct()

        line_item_product.set_id(347706112402032)

        # line_item_product.add_key_value("Products_External", "ProductExternal")

        inventory_line_item.add_key_value("Product_Name", line_item_product)

        inventory_line_item.add_key_value("Quantity", 3.0)

        inventory_line_item.add_key_value("Description", 'productDescription')

        inventory_line_item.add_key_value("ListPrice", 10.0)

        inventory_line_item.add_key_value("Discount", '5.90')

        product_line_taxes = []

        product_line_tax = LineTax()

        product_line_tax.set_name('MyTax1134')

        product_line_tax.set_percentage(12.1)

        product_line_taxes.append(product_line_tax)

        inventory_line_item.add_key_value("Line_Tax", product_line_taxes)

        inventory_line_item_list.append(inventory_line_item)

        record.add_key_value('Quoted_Items', inventory_line_item_list)

        record.add_field_value(Field.Quotes.subject(), "Python- testing")

        line_taxes = []

        line_tax = LineTax()

        line_tax.set_name('MyTax1134')

        line_tax.set_percentage(5.0)

        line_taxes.append(line_tax)

        record.add_key_value("$line_tax", line_taxes)

        vendor_name = ZCRMRecord()

        vendor_name.set_id(34770614996051)

        record.add_field_value(
            Field.Purchase_Orders.vendor_name(), vendor_name)

        """
		End Inventory
		"""

        """
		Following methods are being used only by Activity modules
		"""
        record.add_field_value(Field.Tasks.description(), "New Task")

        record.add_key_value('Currency', Choice('INR'))

        remind_at = RemindAt()

        remind_at.set_alarm(
            "FREQ=NONE;ACTION=POPUP;TRIGGER=DATE-TIME:2021-01-18T12:45:00+05:30")

        record.add_field_value(Field.Tasks.remind_at(), remind_at)

        record.add_field_value(Field.Tasks.subject(), "Python - testing")

        record.add_field_value(Field.Calls.reminder(), Choice("5 mins"))

        record.add_field_value(Field.Calls.call_type(), Choice("Outbound"))

        record.add_field_value(Field.Calls.call_start_time(),
                               datetime(2020, 12, 1, 1, 1, 1))

        who_id = ZCRMRecord()

        who_id.set_id(347706112263005)

        record.add_field_value(Field.Tasks.who_id(), who_id)

        record.add_field_value(Field.Tasks.status(),
                               Choice('Waiting for Input'))

        record.add_field_value(Field.Tasks.due_date(), date(2020, 10, 10))

        record.add_field_value(Field.Tasks.priority(), Choice('High'))

        what_id = ZCRMRecord()

        what_id.set_id(347706112263002)

        record.add_field_value(Field.Tasks.what_id(), what_id)

        record.add_key_value("$se_module", "Accounts")

        # Recurring Activity can be provided in any activity module

        recurring_activity = RecurringActivity()

        recurring_activity.set_rrule(
            'FREQ=DAILY;INTERVAL=10;UNTIL=2022-08-14;DTSTART=2022-07-03')

        record.add_field_value(
            Field.Events.recurring_activity(), recurring_activity)

        record.add_field_value(Field.Events.description(), "My Event")

        start_date_time = datetime.fromisoformat('2022-07-03T12:30:00+05:30')

        record.add_field_value(Field.Events.start_datetime(), start_date_time)

        participants_list = []

        participant = Participants()

        participant.set_participant('test@gmail.com')

        participant.set_type('email')

        participants_list.append(participant)

        participant = Participants()

        participant.set_participant('347706112263005')

        participant.set_type('contact')

        participants_list.append(participant)

        record.add_field_value(Field.Events.participants(), participants_list)

        record.add_key_value("$send_notification", True)

        record.add_field_value(
            Field.Events.event_title(), "New Automated Event")

        end_date_time = datetime(2022, 9, 3, 10, 10, 10)

        record.add_field_value(Field.Events.end_datetime(), end_date_time)

        remind_at_value = datetime(2022, 7, 3, 8, 10, 10)

        record.add_field_value(Field.Events.remind_at(), remind_at_value)

        record.add_field_value(Field.Events.check_in_status(), 'PLANNED')

        what_id = ZCRMRecord()

        what_id.set_id(347706112673010)

        record.add_field_value(Field.Events.what_id(), what_id)

        record.add_key_value("$se_module", "Leads")

        """
		End Activity
		"""

        """
		Following methods are being used only by Price_Books module
		"""
        pricing_details_list = []

        pricing_detail = PricingDetails()

        pricing_detail.set_from_range(1.0)

        pricing_detail.set_to_range(5.0)

        pricing_detail.set_discount(2.1)

        pricing_details_list.append(pricing_detail)

        pricing_detail = PricingDetails()

        pricing_detail.add_key_value('from_range', 6.0)

        pricing_detail.add_key_value('to_range', 11.0)

        pricing_detail.add_key_value('discount', 3.0)

        pricing_details_list.append(pricing_detail)

        record.add_field_value(
            Field.Price_Books.pricing_details(), pricing_details_list)

        record.add_key_value("Email", "abc@zoho.com")

        record.add_field_value(
            Field.Price_Books.description(), "My Price Book")

        record.add_field_value(
            Field.Price_Books.price_book_name(), 'book_name')

        record.add_field_value(
            Field.Price_Books.pricing_model(), Choice('Flat'))

        """
		End of Price_Books
		"""

        tags_list = []

        tag = Tag()

        tag.set_name("My Record")

        tags_list.append(tag)

        record.set_tag(tags_list)

        # Add Record instance to the list
        records_list.append(record)

        # Set the list to data in BodyWrapper instance
        request.set_data(records_list)

        trigger = ["approval", "workflow", "blueprint"]

        # Set the list containing the trigger operations to be run
        request.set_trigger(trigger)

        lar_id = '34096432157065'

        # Set the larId
        request.set_lar_id(lar_id)

        process = ["review_process"]

        # Set the array containing the process to be run
        request.set_process(process)

        header_instance = HeaderMap()

        # header_instance.add(CreateRecordsHeader.x_external, "Quotes.Quoted_Items.Product_Name.Products_External")

        # Call create_records method that takes module_api_name, BodyWrapper instance and header_instance as parameters
        response = record_operations.create_records(
            module_api_name, request, header_instance)

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
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

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
    def update_records(module_api_name):
        """
		This method is used to update the records of a module with ID and print the response.
		:param module_api_name: The API Name of the module to update records.
		"""

        """
		example
		module_api_name = 'Leads'
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Record instances
        records_list = []

        # Get instance of Record Class
        record1 = ZCRMRecord()

        # ID of the record to be updated
        record1.set_id(347706112685)

        # Get the instance of ApplyFeatureExecution Class
        apply_feature_execution = ApplyFeatureExecution()

        # set name to instance of ApplyFeatureExecution Class
        apply_feature_execution.set_name("layout_rules")

        # Add instance of ApplyFeatureExecution to apply_feature_list
        apply_feature_list = []

        apply_feature_list.append(apply_feature_execution)

        # set the data to BodyWrapper instance
        request.set_apply_feature_execution(apply_feature_list)

        # Value to Record's fields can be provided in any of the following ways

        """
		Call add_field_value method that takes two arguments
		Import the zcrmsdk.src.com.zoho.crm.api.record.field file
		1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field name from the displayed list.
		2 -> Value
		"""

        record1.add_field_value(Field.Leads.last_name(), 'Python SDK')

        record1.add_field_value(Field.Leads.company(), 'NNN')

        record1.add_field_value(Field.Leads.city(), 'Hola')

        """
		Call add_key_value method that takes two arguments
		1 -> A string that is the Field's API Name
		2 -> Value
		"""

        record1.add_key_value('Custom_field', 'Value')

        record1.add_key_value('Custom_field_2', 90)

        # Add Record instance to the list
        records_list.append(record1)

        # Get instance of Record Class
        record2 = ZCRMRecord()

        # ID of the record to be updated
        record2.set_id(347706112685)

        # Value to Record's fields can be provided in any of the following ways

        """
		Call add_field_value method that takes two arguments
		Import the zcrmsdk.src.com.zoho.crm.api.record.field file
		1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field name from the displayed list.
		2 -> Value
		"""

        record2.add_field_value(Field.Leads.last_name(), 'Edited Name')

        record2.add_field_value(Field.Leads.city(), 'Hola')

        """
		Call add_key_value method that takes two arguments
		1 -> A string that is the Field's API Name
		2 -> Value
		"""

        record2.add_key_value('Custom_field_2', 90)

        record2.add_key_value('Discounted', 19.8)

        # Used when GDPR is enabled
        data_consent = Consent()

        data_consent.set_consent_remarks("Approved.")

        data_consent.set_consent_through('Email')

        data_consent.set_contact_through_email(True)

        data_consent.set_contact_through_social(False)

        # record2.add_key_value('Data_Processing_Basis_Details', data_consent)

        """
		Following methods are being used only by Inventory modules
		"""
        deal_name = ZCRMRecord()

        deal_name.add_field_value(Field.Deals.id(), 347706112416012)

        record2.add_field_value(Field.Sales_Orders.deal_name(), deal_name)

        contact_name = ZCRMRecord()

        contact_name.add_field_value(Field.Contacts.id(), 347706112263005)

        record2.add_field_value(
            Field.Sales_Orders.contact_name(), contact_name)

        account_name = ZCRMRecord()

        # account_name.add_field_value(Field.Accounts.id(), 34096430692007)

        account_name.add_key_value("name", "automatedAccount")

        record2.add_field_value(
            Field.Sales_Orders.account_name(), account_name)

        record2.add_key_value("Discount", 10.5)

        inventory_line_item_list = []

        inventory_line_item = ZCRMRecord()

        line_item_product = LineItemProduct()

        line_item_product.set_id(347706112402032)

        # line_item_product.add_key_value("Products_External", "ProductExternal")

        inventory_line_item.add_key_value("Product_Name", line_item_product)

        inventory_line_item.add_key_value("Quantity", 3.0)

        inventory_line_item.add_key_value("Description", 'productDescription')

        inventory_line_item.add_key_value("ListPrice", 10.0)

        inventory_line_item.add_key_value("Discount", '5.90')

        product_line_taxes = []

        product_line_tax = LineTax()

        product_line_tax.set_name('MyTax1134')

        product_line_tax.set_percentage(12.1)

        product_line_taxes.append(product_line_tax)

        inventory_line_item.add_key_value("Line_Tax", product_line_taxes)

        inventory_line_item_list.append(inventory_line_item)

        record2.add_key_value('Quoted_Items', inventory_line_item_list)

        record2.add_field_value(Field.Quotes.subject(), "Python- testing")

        line_taxes = []

        line_tax = LineTax()

        line_tax.set_name('MyTax1134')

        line_tax.set_percentage(5.0)

        line_taxes.append(line_tax)

        record2.add_key_value("$line_tax", line_taxes)

        vendor_name = ZCRMRecord()

        vendor_name.set_id(34770614996051)

        # record2.add_field_value(Field.Purchase_Orders.vendor_name(), vendor_name)

        """
		End Inventory
		"""

        # Add Record instance to the list
        records_list.append(record2)

        # Set the list to data in BodyWrapper instance
        request.set_data(records_list)

        trigger = []

        trigger.append("approval")

        trigger.append("workflow")

        trigger.append("blueprint")

        # Set the list containing the trigger operations to be run
        request.set_trigger(trigger)

        header_instance = HeaderMap()

        header_instance.add(UpdateRecordsHeader.x_external,
                            "Quotes.Quoted_Items.Product_Name.Products_External")

        # Call update_records method that takes module_api_name, BodyWrapper instance and header_instance as parameter.
        response = record_operations.update_records(
            module_api_name, request, header_instance)

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
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

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
    def delete_records(module_api_name, record_ids):
        """
		This method is used to delete multiple records of a module and print the response.
		:param module_api_name: The API Name of the module to delete records.
		:param record_ids: The list of record IDs to be deleted
		"""

        """
		example
		module_api_name = "Contacts";
		record_ids = [34096430756050,
			34096430729017, 34096430729009]
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Delete Records operation
        param_instance.add(DeleteRecordsParam.wf_trigger, True)

        for record_id in record_ids:
            param_instance.add(DeleteRecordsParam.ids, record_id)

        header_instance = HeaderMap()

        # header_instance.add(DeleteRecordsHeader.x_external, "Leads.External")

        # Call deleteRecords method that takes param_instance and module_api_name as parameter.
        response = record_operations.delete_records(
            module_api_name, param_instance, header_instance)

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
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

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
    def upsert_records(module_api_name):
        """
		This method is used to Upsert records of a module and print the response.
		:param module_api_name: The API Name of the module to upsert records.
		"""

        """
		example
		module_api_name = 'Leads'
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List to hold Record instances
        records_list = []

        # Get instance of Record Class
        record_1 = ZCRMRecord()

        # Get the instance of ApplyFeatureExecution Class
        apply_feature_execution = ApplyFeatureExecution()

        # set name to instance of ApplyFeatureExecution Class
        apply_feature_execution.set_name("layout_rules")

        # Add instance of ApplyFeatureExecution to apply_feature_list
        apply_feature_list = []

        apply_feature_list.append(apply_feature_execution)

        # set the data to BodyWrapper instance
        request.set_apply_feature_execution(apply_feature_list)

        # Value to Record's fields can be provided in any of the following ways

        """
		Call add_field_value method that takes two arguments
		Import the zcrmsdk.src.com.zoho.crm.api.record.field file
		1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field name from the displayed list.
		2 -> Value
		"""

        record_1.add_field_value(Field.Leads.last_name(), 'Python SDK')

        record_1.add_field_value(Field.Leads.first_name(), 'New')

        record_1.add_field_value(Field.Leads.company(), 'Zoho')

        record_1.add_field_value(Field.Leads.city(), 'City')

        """
		Call add_key_value method that takes two arguments
		1 -> A string that is the Field's API Name
		2 -> Value
		"""

        record_1.add_key_value('Custom_field', 'Value')

        record_1.add_key_value('Custom_field_2', 12)

        # Add Record instance to the list
        records_list.append(record_1)

        # Get instance of Record Class
        record_2 = ZCRMRecord()

        # Value to Record's fields can be provided in any of the following ways

        """
		Call add_field_value method that takes two arguments
		Import the zcrmsdk.src.com.zoho.crm.api.record.field file
		1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field name from the displayed list.
		2 -> Value
		"""

        record_2.add_field_value(Field.Leads.last_name(), 'Boyle')

        record_2.add_field_value(Field.Leads.first_name(), 'Patricia')

        record_2.add_field_value(Field.Leads.company(), 'Law')

        record_2.add_field_value(Field.Leads.city(), 'Man')

        """
		Call add_key_value method that takes two arguments
		1 -> A string that is the Field's API Name
		2 -> Value
		"""

        record_2.add_key_value('Custom_field', 'Value')

        record_2.add_key_value('Custom_field_2', 12)

        # Add Record instance to the list
        records_list.append(record_2)

        # Set the list to data in BodyWrapper instance
        request.set_data(records_list)

        duplicate_check_fields = ["City", "Last_Name", "First_Name"]

        # Set the array containing duplicate check fields to BodyWrapper instance
        request.set_duplicate_check_fields(duplicate_check_fields)

        header_instance = HeaderMap()

        # header_instance.add(UpsertRecordsHeader.x_external, "Leads.External")

        # Call upsertRecords method that takes BodyWrapper instance and module_api_name as parameters.
        response = record_operations.upsert_records(
            module_api_name, request, header_instance)

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
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

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
    def get_deleted_records(module_api_name):
        """
		This method is used to get the deleted records of a module and print the response.
		:param module_api_name: The API Name of the module to get the deleted records.
		"""

        """
		example
		module_api_name = "Deals"
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Get Deleted Records operation
        param_instance.add(GetDeletedRecordsParam.page, 1)

        param_instance.add(GetDeletedRecordsParam.per_page, 200)

        # can be all/recycle/permanent
        param_instance.add(GetDeletedRecordsParam.type, 'permanent')

        # Get instance of HeaderMap Class
        header_instance = HeaderMap()

        # Possible headers for Get Deleted Records operation
        # header_instance.add(GetDeletedRecordsHeader.if_modified_since, datetime.fromisoformat('2020-01-15T10:35:32+05:30'))

        # Call getDeletedRecords method that takes param_instance, header_instance and module_api_name as parameter
        response = record_operations.get_deleted_records(
            module_api_name, param_instance, header_instance)

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

                # Check if expected DeletedRecordsWrapper instance is received.
                if isinstance(response_object, DeletedRecordsWrapper):
                    # Get the list of obtained DeletedRecord instances
                    deleted_records = response_object.get_data()

                    for deleted_record in deleted_records:
                        # Get the deletedBy User instance of each DeletedRecord
                        deleted_by = deleted_record.get_deleted_by()

                        # Check if deleted_by is not None
                        if deleted_by is not None:
                            # Get the Name of the deleted_by User
                            print("Record Deleted By - Name: " +
                                  deleted_by.get_name())

                            # Get the ID of the deleted_by User
                            print("Record Deleted By - ID: " +
                                  str(deleted_by.get_id()))

                        # Get the ID of each DeletedRecord
                        print("DeletedRecord ID: " +
                              str(deleted_record.get_id()))

                        # Get the DisplayName of each DeletedRecord
                        print("DeletedRecord DisplayName: " +
                              str(deleted_record.get_display_name()))

                        # Get the Type of each DeletedRecord
                        print("DeletedRecord Type: " +
                              str(deleted_record.get_type()))

                        # Get the DeletedTime of each DeletedRecord
                        print("DeletedRecord DeletedTime: " +
                              str(deleted_record.get_deleted_time()))

                        # Get the createdBy User instance of each DeletedRecord
                        created_by = deleted_record.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Record Created By - Name: " +
                                  created_by.get_name())

                            # Get the ID of the created_by User
                            print("Record Created By - ID: " +
                                  str(created_by.get_id()))

                    info = response_object.get_info()

                    if info is not None:
                        if info.get_per_page() is not None:
                            # Get the PerPage from Info
                            print('Record Info PerPage: ' +
                                  str(info.get_per_page()))

                        if info.get_page() is not None:
                            # Get the Page from Info
                            print('Record Info Page: ' + str(info.get_page()))

                        if info.get_count() is not None:
                            # Get the Count from Info
                            print('Record Info Count: ' +
                                  str(info.get_count()))

                        if info.get_more_records() is not None:
                            # Get the MoreRecords from Info
                            print('Record Info MoreRecords: ' +
                                  str(info.get_more_records()))

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
    def search_records(module_api_name):
        """
		This method is used to search records of a module and print the response.
		:param module_api_name: The API Name of the module to search records.
		"""

        """
		example
		module_api_name = "Price_Books"
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Search Records operation
        param_instance.add(SearchRecordsParam.email, 'user@zoho.com')

        param_instance.add(SearchRecordsParam.phone, '234567890')

        param_instance.add(SearchRecordsParam.word, 'First Name Last Name')

        param_instance.add(SearchRecordsParam.approved, 'both')

        param_instance.add(SearchRecordsParam.converted, 'both')

        param_instance.add(SearchRecordsParam.page, 1)

        param_instance.add(SearchRecordsParam.per_page, 20)

        # Encoding must be done for parentheses or comma
        param_instance.add(SearchRecordsParam.criteria,
                           '((Last_Name:starts_with:Last Name) and (Company:starts_with:fasf\\(123\\) K))')

        # param_instance.add(SearchRecordsParam.criteria, "(External:in:1232344323)")

        header_instance = HeaderMap()

        # header_instance.add(UpsertRecordsHeader.x_external, "Leads.External")

        # Call searchRecords method that takes module_api_name, param_instance and header_instance as parameter
        response = record_operations.search_records(
            module_api_name, param_instance, header_instance)

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

                # Check if expected ResponseWrapper instance is received.
                if isinstance(response_object, ResponseWrapper):

                    # Get the list of obtained Record instances
                    record_list = response_object.get_data()

                    for record in record_list:
                        # Get the ID of each Record
                        print("Record ID: " + str(record.get_id()))

                        # Get the createdBy User instance of each Record
                        created_by = record.get_created_by()

                        # Check if created_by is not None
                        if created_by is not None:
                            # Get the Name of the created_by User
                            print("Record Created By - Name: " +
                                  created_by.get_name())

                            # Get the ID of the created_by User
                            print("Record Created By - ID: " +
                                  str(created_by.get_id()))

                            # Get the Email of the created_by User
                            print("Record Created By - Email: " +
                                  created_by.get_email())

                        # Get the CreatedTime of each Record
                        print("Record CreatedTime: " +
                              str(record.get_created_time()))

                        if record.get_modified_time() is not None:
                            # Get the ModifiedTime of each Record
                            print("Record ModifiedTime: " +
                                  str(record.get_modified_time()))

                        # Get the modified_by User instance of each Record
                        modified_by = record.get_modified_by()

                        # Check if modified_by is not None
                        if modified_by is not None:
                            # Get the Name of the modified_by User
                            print("Record Modified By - Name: " +
                                  modified_by.get_name())

                            # Get the ID of the modified_by User
                            print("Record Modified By - ID: " +
                                  str(modified_by.get_id()))

                            # Get the Email of the modified_by User
                            print("Record Modified By - Email: " +
                                  modified_by.get_email())

                        # Get the list of obtained Tag instance of each Record
                        tags = record.get_tag()

                        if tags is not None:
                            for tag in tags:
                                # Get the Name of each Tag
                                print("Record Tag Name: " + tag.get_name())

                                # Get the Id of each Tag
                                print("Record Tag ID: " + str(tag.get_id()))

                        # To get particular field value
                        print("Record Field Value: " +
                              str(record.get_key_value('Last_Name')))

                        print('Record KeyValues: ')

                        key_values = record.get_key_values()

                        for key_name, value in key_values.items():

                            if isinstance(value, list):

                                if len(value) > 0:

                                    if isinstance(value[0], FileDetails):
                                        file_details = value

                                        for file_detail in file_details:
                                            # Get the Extn of each FileDetails
                                            print(
                                                "Record FileDetails Extn: " + file_detail.get_extn())

                                            # Get the IsPreviewAvailable of each FileDetails
                                            print("Record FileDetails IsPreviewAvailable: " + str(
                                                file_detail.get_is_preview_available()))

                                            # Get the DownloadUrl of each FileDetails
                                            print(
                                                "Record FileDetails DownloadUrl: " + file_detail.get_download_url())

                                            # Get the DeleteUrl of each FileDetails
                                            print(
                                                "Record FileDetails DeleteUrl: " + file_detail.get_delete_url())

                                            # Get the EntityId of each FileDetails
                                            print(
                                                "Record FileDetails EntityId: " + file_detail.get_entity_id())

                                            # Get the Mode of each FileDetails
                                            print(
                                                "Record FileDetails Mode: " + file_detail.get_mode())

                                            # Get the OriginalSizeByte of each FileDetails
                                            print(
                                                "Record FileDetails OriginalSizeByte: " + file_detail.get_original_size_byte())

                                            # Get the PreviewUrl of each FileDetails
                                            print(
                                                "Record FileDetails PreviewUrl: " + file_detail.get_preview_url())

                                            # Get the FileName of each FileDetails
                                            print(
                                                "Record FileDetails FileName: " + file_detail.get_file_name())

                                            # Get the FileId of each FileDetails
                                            print(
                                                "Record FileDetails FileId: " + file_detail.get_file_id())

                                            # Get the AttachmentId of each FileDetails
                                            print(
                                                "Record FileDetails AttachmentId: " + file_detail.get_attachment_id())

                                            # Get the FileSize of each FileDetails
                                            print(
                                                "Record FileDetails FileSize: " + file_detail.get_file_size())

                                            # Get the CreatorId of each FileDetails
                                            print(
                                                "Record FileDetails CreatorId: " + file_detail.get_creator_id())

                                            # Get the LinkDocs of each FileDetails
                                            print(
                                                "Record FileDetails LinkDocs: " + file_detail.get_link_docs())

                                    elif isinstance(value[0], Reminder):
                                        reminders = value

                                        for reminder in reminders:
                                            # Get the Reminder Period
                                            print("Reminder Period: " +
                                                  reminder.get_period())

                                            # Get the Reminder Unit
                                            print("Reminder Unit: " +
                                                  reminder.get_unit())

                                    elif isinstance(value[0], Choice):
                                        choice_list = value

                                        print(key_name)

                                        print('Values')

                                        for choice in choice_list:
                                            print(choice.get_value())

                                    elif isinstance(value[0], Participants):
                                        participants = value

                                        for participant in participants:
                                            print(
                                                "Record Participants Name: " + participant.get_name())

                                            print(
                                                "Record Participants Invited: " + str(participant.get_invited()))

                                            print(
                                                "Record Participants Type: " + participant.get_type())

                                            print(
                                                "Record Participants Participant: " + participant.get_participant())

                                            print(
                                                "Record Participants Status: " + participant.get_status())

                                    elif isinstance(value[0], ImageUpload):
                                        image_uploads = value

                                        for image_upload in image_uploads:
                                            print("Record  Id: " +
                                                  str(image_upload.get_id()))

                                            print("Record  FileId: " +
                                                  image_upload.get_file_id())

                                            print("Record  SequenceNumber: " +
                                                  image_upload.get_sequence_number())

                                            print("Record  Size: " +
                                                  str(image_upload.get_size()))

                                            print("Record  State: " +
                                                  str(image_upload.get_state()))

                                            print("Record  File_Name: " +
                                                  image_upload.get_file_name())

                                            print("Record  PreviewId: " +
                                                  image_upload.get_preview_id())

                                            print("Record  Description: " +
                                                  str(image_upload.get_description()))

                                    elif isinstance(value[0], Tax):
                                        tax = value[0]

                                        print("Record Tax Name: " +
                                              tax.get_name())

                                        print("Record Tax ID: " +
                                              str(tax.get_id()))

                                    elif isinstance(value[0], ImageUpload):
                                        image_uploads = value

                                        for image_upload in image_uploads:
                                            print("RelatedRecord  Id: " +
                                                  str(image_upload.get_id()))

                                            print("RelatedRecord  FileId: " +
                                                  image_upload.get_file_id())

                                            print(
                                                "RelatedRecord  SequenceNumber: " + image_upload.get_sequence_number())

                                            print("RelatedRecord  Size: " +
                                                  str(image_upload.get_size()))

                                            print("RelatedRecord  State: " +
                                                  str(image_upload.get_state()))

                                            print(
                                                "RelatedRecord  File_Name: " + image_upload.get_file_name())

                                            print(
                                                "RelatedRecord  PreviewId: " + image_upload.get_preview_id())

                                            print(
                                                "RelatedRecord  Description: " + str(image_upload.get_description()))

                                    elif isinstance(value[0], Tag):
                                        tags = value

                                        if tags is not None:
                                            for tag in tags:
                                                print(
                                                    "Record Tag Name: " + tag.get_name())

                                                print("Record Tag ID: " +
                                                      str(tag.get_id()))

                                    elif isinstance(value[0], PricingDetails):
                                        pricing_details = value

                                        for pricing_detail in pricing_details:
                                            print(
                                                "Record PricingDetails ToRange: " + str(pricing_detail.get_to_range()))

                                            print(
                                                "Record PricingDetails Discount: " + str(pricing_detail.get_discount()))

                                            print(
                                                "Record PricingDetails ID: " + str(pricing_detail.get_id()))

                                            print("Record PricingDetails FromRange: " + str(
                                                pricing_detail.get_from_range()))

                                    elif isinstance(value[0], ZCRMRecord):
                                        record_list = value

                                        for each_record in record_list:
                                            for key, val in each_record.get_key_values().items():
                                                print(
                                                    str(key) + " : " + str(val))

                                    elif isinstance(value[0], LineTax):
                                        line_taxes = value

                                        for line_tax in line_taxes:
                                            print("Record LineTax Percentage: " + str(
                                                line_tax.get_percentage()))

                                            print(
                                                "Record LineTax Name: " + line_tax.get_name())

                                            print("Record LineTax Id: " +
                                                  str(line_tax.get_id()))

                                            print("Record LineTax Value: " +
                                                  str(line_tax.get_value()))

                                    elif isinstance(value[0], Comment):
                                        comments = value

                                        for comment in comments:
                                            print("Comment-ID: " +
                                                  str(comment.get_id()))

                                            print("Comment-Content: " +
                                                  comment.get_comment_content())

                                            print("Comment-Commented_By: " +
                                                  comment.get_commented_by())

                                            print("Comment-Commented Time: " +
                                                  str(comment.get_commented_time()))

                                    else:
                                        print(key_name)

                                        for each_value in value:
                                            print(str(each_value))

                            elif isinstance(value, User):
                                print("Record " + key_name +
                                      " User-ID: " + str(value.get_id()))

                                print("Record " + key_name +
                                      " User-Name: " + value.get_name())

                                print("Record " + key_name +
                                      " User-Email: " + value.get_email())

                            elif isinstance(value, Layout):
                                print(key_name + " ID: " + str(value.get_id()))

                                print(key_name + " Name: " + value.get_name())

                            elif isinstance(value, ZCRMRecord):
                                print(key_name + " Record ID: " +
                                      str(value.get_id()))

                                print(key_name + " Record Name: " +
                                      value.get_key_value('name'))

                            elif isinstance(value, Choice):
                                print(key_name + " : " + value.get_value())

                            elif isinstance(value, RemindAt):
                                print(key_name + " : " + value.get_alarm())

                            elif isinstance(value, RecurringActivity):
                                print(key_name)

                                print("RRULE: " + value.get_rrule())

                            elif isinstance(value, Consent):
                                print("Record Consent ID: " +
                                      str(value.get_id()))

                                # Get the createdBy User instance of each Record
                                created_by = value.get_created_by()

                                # Check if created_by is not None
                                if created_by is not None:
                                    # Get the Name of the created_by User
                                    print(
                                        "Record Consent Created By - Name: " + created_by.get_name())

                                    # Get the ID of the created_by User
                                    print(
                                        "Record Consent Created By - ID: " + str(created_by.get_id()))

                                    # Get the Email of the created_by User
                                    print(
                                        "Record Consent Created By - Email: " + created_by.get_email())

                                # Get the CreatedTime of each Record
                                print("Record Consent CreatedTime: " +
                                      str(value.get_created_time()))

                                if value.get_modified_time() is not None:
                                    # Get the ModifiedTime of each Record
                                    print("Record Consent ModifiedTime: " +
                                          str(value.get_modified_time()))

                                # Get the Owner User instance of the Consent
                                owner = value.get_owner()

                                if owner is not None:
                                    # Get the Name of the Owner User
                                    print(
                                        "Record Consent Created By - Name: " + owner.get_name())

                                    # Get the ID of the Owner User
                                    print(
                                        "Record Consent Created By - ID: " + str(owner.get_id()))

                                    # Get the Email of the Owner User
                                    print(
                                        "Record Consent Created By - Email: " + owner.get_email())

                                print("Record Consent ContactThroughEmail: " +
                                      str(value.get_contact_through_email()))

                                print("Record Consent ContactThroughSocial: " +
                                      str(value.get_contact_through_social()))

                                print("Record Consent ContactThroughSurvey: " +
                                      str(value.get_contact_through_survey()))

                                print("Record Consent ContactThroughPhone: " +
                                      str(value.get_contact_through_phone()))

                                print("Record Consent MailSentTime: " +
                                      str(value.get_mail_sent_time()))

                                print("Record Consent ConsentDate: " +
                                      str(value.get_consent_date()))

                                print("Record Consent ConsentRemarks: " +
                                      value.get_consent_remarks())

                                print("Record Consent ConsentThrough: " +
                                      value.get_consent_through())

                                print("Record Consent DataProcessingBasis: " +
                                      value.get_data_processing_basis())

                                # To get custom values
                                print("Record Consent Lawful Reason: " +
                                      str(value.get_key_value("Lawful_Reason")))

                            elif isinstance(value, dict):
                                for key, val in value.items():
                                    print(key + " : " + str(val))

                            else:
                                print(key_name + " : " + str(value))

                    info = response_object.get_info()

                    if info is not None:
                        if info.get_per_page() is not None:
                            # Get the PerPage from Info
                            print('Record Info PerPage: ' +
                                  str(info.get_per_page()))

                        if info.get_page() is not None:
                            # Get the Page from Info
                            print('Record Info Page: ' + str(info.get_page()))

                        if info.get_count() is not None:
                            # Get the Count from Info
                            print('Record Info Count: ' +
                                  str(info.get_count()))

                        if info.get_more_records() is not None:
                            # Get the MoreRecords from Info
                            print('Record Info MoreRecords: ' +
                                  str(info.get_more_records()))

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
    def convert_lead(lead_id):
        """
		This method is used to Convert a Lead record and print the response.
		:param lead_id: The ID of the Lead to be converted.
		"""

        """
		example
		lead_id = 34096432034003
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of ConvertBodyWrapper Class that will contain the request body
        request = ConvertBodyWrapper()

        # List to hold LeadConverter instances
        data = []

        # Get instance of LeadConverter Class
        record = LeadConverter()

        record.set_overwrite(True)

        record.set_notify_lead_owner(True)

        record.set_notify_new_entity_owner(True)

        record.set_accounts('34096430692007')

        record.set_contacts('34096430836001')

        record.set_assign_to('34096430302031')

        deals = ZCRMRecord()

        """
		Call add_field_value method that takes two arguments
		Import the zcrmsdk.src.com.zoho.crm.api.record.field file
		1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field name from the displayed list.
		2 -> Value
		"""

        deals.add_field_value(Field.Deals.deal_name(), 'deal_name')

        deals.add_field_value(Field.Deals.description(), "deals description")

        deals.add_field_value(Field.Deals.closing_date(), date(2020, 10, 2))

        deals.add_field_value(Field.Deals.stage(), Choice("Closed Won"))

        deals.add_field_value(Field.Deals.amount(), 500.78)

        """
		Call add_key_value method that takes two arguments
		1 -> A string that is the Field's API Name
		2 -> Value
		"""

        deals.add_key_value('Custom_field', 'Value')

        tag_list = []

        tag = Tag()

        tag.set_name('Converted')

        tag_list.append(tag)

        deals.set_tag(tag_list)

        record.set_deals(deals)

        data.append(record)

        request.set_data(data)

        # Call convertLead method that takes ConvertBodyWrapper instance and lead_id as parameter
        response = record_operations.convert_lead(lead_id, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, ConvertActionWrapper):

                    # Get the list of obtained ActionResponse instances
                    action_response_list = response_object.get_data()

                    for action_response in action_response_list:

                        # Check if the request is successful
                        if isinstance(action_response, SuccessfulConvert):
                            # Get the Accounts ID of  Record
                            print("LeadConvert Accounts ID: " +
                                  action_response.get_accounts())

                            # Get the Contacts ID of  Record
                            print("LeadConvert Contacts ID: " +
                                  action_response.get_contacts())

                            # Get the Deals ID of  Record
                            print("LeadConvert Deals ID: " +
                                  action_response.get_deals())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

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
    def get_photo(module_api_name, record_id, destination_folder):
        """
		This method is used to download a photo associated with a record.
		:param module_api_name: The API Name of the record's module
		:param record_id: The ID of the record
		:param destination_folder: The absolute path of the destination folder to store the photo.
		"""

        """
		example
		module_api_name = "Contacts"
		record_id = 34096432034003
		destination_folder = "/Users/user-name/Documents"
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Call getPhoto method that takes module_api_name and record_id as parameters
        response = record_operations.get_photo(record_id, module_api_name)

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

                # Check if expected ResponseWrapper instance is received.
                if isinstance(response_object, FileBodyWrapper):

                    # Get StreamWrapper instance from the returned FileBodyWrapper instance
                    stream_wrapper = response_object.get_file()

                    # Construct the file name by joining the destinationFolder and the name from StreamWrapper instance
                    file_name = os.path.join(
                        destination_folder, stream_wrapper.get_name())

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

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def upload_photo(module_api_name, record_id, absolute_file_path):
        """
		This method is used to attach a photo to a record. You must include the file in the request
		:param module_api_name: The API Name of the record's module
		:param record_id: The ID of the record
		:param absolute_file_path: The absolute file path of the file to be uploaded
		"""

        """
		example
		module_api_name = "Contacts"
		record_id = 34096432034003
		absolute_file_path = "/Users/user_name/Desktop/image.png"
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of FileBodyWrapper class that will contain the request file
        request = FileBodyWrapper()

        """
		StreamWrapper can be initialized in any of the following ways

		* param 1 -> fileName
		* param 2 -> Read Stream.
		"""
        # stream_wrapper = StreamWrapper(stream=open(absolute_file_path, 'rb'))

        """
		* param 1 -> fileName
		* param 2 -> Read Stream
		* param 3 -> Absolute File Path of the file to be attached
		"""

        stream_wrapper = StreamWrapper(file_path=absolute_file_path)

        # Set file to the FileBodyWrapper instance
        request.set_file(stream_wrapper)

        # Call uploadPhoto method that takes FileBodyWrapper instance, module_api_name and record_id as parameter
        response = record_operations.upload_photo(
            record_id, module_api_name, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from responsse
            response_object = response.get_object()

            if response_object is not None:

                # Check if the request is successful
                if isinstance(response_object, SuccessResponse):
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
    def delete_photo(module_api_name, record_id):
        """
		This method is used to delete a photo from a record in a module.
		:param module_api_name: The API Name of the record's module
		:param record_id: The ID of the record to delete photo
		"""

        """
		example
		module_api_name = "Contacts"
		record_id = 34096432034003
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Call deletePhoto method that takes module_api_name and record_id as parameter
        response = record_operations.delete_photo(record_id, module_api_name)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from responsse
            response_object = response.get_object()

            if response_object is not None:

                # Check if the request is successful
                if isinstance(response_object, SuccessResponse):
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
    def mass_update_records(module_api_name):
        """
		This method is used to update the values of specific fields for multiple records and print the response.
		:param module_api_name: The API Name of the module to mass update records.
		"""

        """
		example
		module_api_name = "Contacts"
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of MassUpdateBodyWrapper Class that will contain the request body
        request = MassUpdateBodyWrapper()

        # List to hold Record instances
        records_list = []

        # Get instance of Record Class
        record = ZCRMRecord()

        record.add_field_value(Field.Leads.city(), 'HOO')

        # Add the record instance to list
        records_list.append(record)

        # Set the array to data in MassUpdateBodyWrapper instance
        request.set_data(records_list)

        # Set the cvid to MassUpdateBodyWrapper instance
        request.set_cvid('34096430087537')

        ids = [34096432049003, 34096432043003, 34096431881002]

        # Set the array of IDs to MassUpdateBodyWrapper instance
        request.set_ids(ids)

        # Set the value to over write
        request.set_over_write(True)

        # Get instance of Territory Class
        territory = MassUpdateTerritory()

        # Set ID to Territory
        territory.set_id(34096430505351)

        territory.set_include_child(True)

        request.set_territory(territory)

        # Call mass_update_records method that takes MassUpdateBodyWrapper instance, module_api_name as parameter.
        response = record_operations.mass_update_records(
            module_api_name, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from responsse
            response_object = response.get_object()

            if response_object is not None:

                # Check if expected ActionWrapper instance is received.
                if isinstance(response_object, MassUpdateActionWrapper):

                    # Get the list of obtained MassUpdate ActionResponse instances
                    action_response_list = response_object.get_data()

                    for action_response in action_response_list:
                        # Check if the request is successful
                        if isinstance(action_response, MassUpdateSuccessResponse):
                            # Get the Status
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

                        # Check if the request returned an exception
                        elif isinstance(action_response, APIException):
                            # Get the Status
                            print("Status: " +
                                  action_response.get_status().get_value())

                            # Get the Code
                            print("Code: " + action_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = action_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print("Message: " +
                                  action_response.get_message().get_value())

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
    def get_mass_update_status(module_api_name, job_id):
        """
		This method is used to get the status of the mass update job scheduled previously and print the response.
		:param module_api_name: The API Name of the module to obtain status of Mass Update.
		:param job_id: The ID of the job obtained from the response of Mass Update Records.
		"""

        """
		example
		module_api_name = "Leads"
		job_id = "34770615177002"
		"""

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        # Possible parameters for Get MassUpdate Status operation
        param_instance.add(GetMassUpdateStatusParam.job_id, job_id)

        # Call getMassUpdateStatus method that takes ParameterMap instance and module_api_name as parameter
        response = record_operations.get_mass_update_status(
            module_api_name, param_instance)

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

                # Check if expected MassUpdateResponseWrapper instance is received.
                if isinstance(response_object, MassUpdateResponseWrapper):

                    # Get the list of MassUpdate ActionResponse data
                    mass_update_responses = response_object.get_data()

                    for mass_update_response in mass_update_responses:

                        # Check if the request is successful
                        if isinstance(mass_update_response, MassUpdate):
                            # Get the Status of each MassUpdate
                            print("MassUpdate Status: " +
                                  mass_update_response.get_status().get_value())

                            # Get the FailedCount of each MassUpdate
                            print("MassUpdate FailedCount: " +
                                  str(mass_update_response.get_failed_count()))

                            # Get the UpdatedCount of each MassUpdate
                            print("MassUpdate UpdatedCount: " +
                                  str(mass_update_response.get_updated_count()))

                            # Get the NotUpdatedCount of each MassUpdate
                            print("MassUpdate NotUpdatedCount: " +
                                  str(mass_update_response.get_not_updated_count()))

                            # Get the TotalCount of each MassUpdate
                            print("MassUpdate TotalCount: " +
                                  str(mass_update_response.get_total_count()))

                        # Check if the request returned an exception
                        elif isinstance(mass_update_response, APIException):
                            # Get the Status
                            print(
                                "Status: " + mass_update_response.get_status().get_value())

                            # Get the Code
                            print(
                                "Code: " + mass_update_response.get_code().get_value())

                            print("Details")

                            # Get the details dict
                            details = mass_update_response.get_details()

                            for key, value in details.items():
                                print(key + ' : ' + str(value))

                            # Get the Message
                            print(
                                "Message: " + mass_update_response.get_message().get_value())

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
    def get_record_count():
        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of ParameterMap Class
        param_instance = ParameterMap()

        module_api_name = "Leads"

        param_instance = ParameterMap()

        param_instance.add(RecordCountParam.phone, "(990) -")

        response = record_operations.record_count(
            module_api_name, param_instance)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return

            # Get object from response
            count_handler = response.get_object()

            if count_handler is not None:
                if isinstance(count_handler, CountWrapper):
                    # Get the received CountWrapper instance
                    count_wrapper = count_handler

                    # Get the Count of Record
                    print("Record Count: " + str(count_wrapper.get_count()))
                # Check if the request returned an exception
                elif isinstance(count_handler, APIException):
                    # Get the Status
                    print("Status: " + mass_update_response.get_status().get_value())

                    # Get the Code
                    print("Code: " + mass_update_response.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = mass_update_response.get_details()

                    for key, value in details.items():
                        print(key + ' : ' + str(value))

                    # Get the Message
                    print("Message: " + mass_update_response.get_message().get_value())

    @staticmethod
    def assign_territories_to_multiple_records(module_api_name):
        # API Name of the module to assignTerritoriesToMultipleRecords
        module_api_name = "Leads"

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List of Record instances
        records = []

        # Get instance of Record Class
        record1 = ZCRMRecord()

        record1.set_id(347706112107002)

        territory = Territory()

        territory.set_id(34770613051397)

        record1.add_key_value("Territories", [territory])

        # Add Record instance to the list
        records.append(record1)

        # Set the list to Records in BodyWrapper instance
        request.set_data(records)

        # Call assign_territories_to_multiple_records method that takes module_api_name and  BodyWrapper instance as parameter.
        response = record_operations.assign_territories_to_multiple_records(module_api_name, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    # Get the list of obtained ActionResponse instances
                    action_responses = response_object.get_data()
                    for action_response in action_responses:
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
    def assign_territory_to_record(module_api_name, id):
        # API Name of the module to assignTerritoriesToMultipleRecords
        module_api_name = "Leads"

        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List of Record instances
        records = []
        # Get instance of Record Class
        record1 = ZCRMRecord()

        record1.set_id(347706112107002)

        territory = Territory()

        territory.set_id(34770613051397)

        record1.add_key_value("Territories", [territory])

        # Add Record instance to the list
        records.append(record1)

        # Set the list to Records in BodyWrapper instance
        request.set_data(records)

        # Call assign_territory_to_record method that takes module_api_name, id and  BodyWrapper instance as parameter.
        response = record_operations.assign_territory_to_record(module_api_name, id, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    # Get the list of obtained ActionResponse instances
                    action_responses = response_object.get_data()
                    for action_response in action_responses:
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

    def remove_territories_from_multiple_records(module_api_name):
        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List of Record instances
        records = []
        # Get instance of Record Class
        record1 = ZCRMRecord()

        record1.set_id(347706112107002)

        territory = Territory()

        territory.set_id(34770613051397)

        record1.add_key_value("Territories", [territory])

        # Add Record instance to the list
        records.append(record1)

        # Set the list to Records in BodyWrapper instance
        request.set_data(records)

        # Call remove_territories_from_multiple_records method that takes module_api_name and BodyWrapper instance as parameter
        response = record_operations.remove_territories_from_multiple_records(module_api_name, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    # Get the list of obtained ActionResponse instances
                    action_responses = response_object.get_data()
                    for action_response in action_responses:
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

    def remove_territories_from_record(module_api_name, id):
        # Get instance of RecordOperations Class
        record_operations = RecordOperations()

        # Get instance of BodyWrapper Class that will contain the request body
        request = BodyWrapper()

        # List of Record instances
        records = []
        # Get instance of Record Class
        record1 = ZCRMRecord()

        territory = Territory()

        territory.set_id(34770613051397)

        record1.add_key_value("Territories", [territory])

        # Add Record instance to the list
        records.append(record1)

        # Set the list to Records in BodyWrapper instance
        request.set_data(records)

        # Call remove_territories_from_record method that takes module_api_name, recordId and BodyWrapper instance as parameter
        response = record_operations.remove_territories_from_record(module_api_name, id, request)

        if response is not None:
            # Get the status code from response
            print('Status Code: ' + str(response.get_status_code()))

            # Get object from response
            response_object = response.get_object()

            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    # Get the list of obtained ActionResponse instances
                    action_responses = response_object.get_data()
                    for action_response in action_responses:
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
