try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
	from zcrmsdk.src.com.zoho.crm.api.record.record import Record
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .record import Record


class InventoryLineItems(Record):
	def __init__(self):
		"""Creates an instance of InventoryLineItems"""
		super().__init__()


	def get_product_name(self):
		"""
		The method to get the product_name

		Returns:
			LineItemProduct: An instance of LineItemProduct
		"""

		return self.get_key_value('Product_Name')

	def set_product_name(self, product_name):
		"""
		The method to set the value to product_name

		Parameters:
			product_name (LineItemProduct) : An instance of LineItemProduct
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.record.line_item_product import LineItemProduct
		except Exception:
			from .line_item_product import LineItemProduct

		if product_name is not None and not isinstance(product_name, LineItemProduct):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: product_name EXPECTED TYPE: LineItemProduct', None, None)
		
		self.add_key_value('Product_Name', product_name)

	def get_parent_id(self):
		"""
		The method to get the parent_id

		Returns:
			Record: An instance of Record
		"""

		return self.get_key_value('parent_id')

	def set_parent_id(self, parent_id):
		"""
		The method to set the value to parent_id

		Parameters:
			parent_id (Record) : An instance of Record
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.record.record import Record
		except Exception:
			from .record import Record

		if parent_id is not None and not isinstance(parent_id, Record):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent_id EXPECTED TYPE: Record', None, None)
		
		self.add_key_value('parent_id', parent_id)

	def get_quantity(self):
		"""
		The method to get the quantity

		Returns:
			float: A float representing the quantity
		"""

		return self.get_key_value('Quantity')

	def set_quantity(self, quantity):
		"""
		The method to set the value to quantity

		Parameters:
			quantity (float) : A float representing the quantity
		"""

		if quantity is not None and not isinstance(quantity, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: quantity EXPECTED TYPE: float', None, None)
		
		self.add_key_value('Quantity', quantity)

	def get_discount(self):
		"""
		The method to get the discount

		Returns:
			string: A string representing the discount
		"""

		return self.get_key_value('Discount')

	def set_discount(self, discount):
		"""
		The method to set the value to discount

		Parameters:
			discount (string) : A string representing the discount
		"""

		if discount is not None and not isinstance(discount, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: discount EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Discount', discount)

	def get_total_after_discount(self):
		"""
		The method to get the total_after_discount

		Returns:
			float: A float representing the total_after_discount
		"""

		return self.get_key_value('Total_After_Discount')

	def set_total_after_discount(self, total_after_discount):
		"""
		The method to set the value to total_after_discount

		Parameters:
			total_after_discount (float) : A float representing the total_after_discount
		"""

		if total_after_discount is not None and not isinstance(total_after_discount, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: total_after_discount EXPECTED TYPE: float', None, None)
		
		self.add_key_value('Total_After_Discount', total_after_discount)

	def get_net_total(self):
		"""
		The method to get the net_total

		Returns:
			float: A float representing the net_total
		"""

		return self.get_key_value('Net_Total')

	def set_net_total(self, net_total):
		"""
		The method to set the value to net_total

		Parameters:
			net_total (float) : A float representing the net_total
		"""

		if net_total is not None and not isinstance(net_total, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: net_total EXPECTED TYPE: float', None, None)
		
		self.add_key_value('Net_Total', net_total)

	def get_price_book_name(self):
		"""
		The method to get the price_book_name

		Returns:
			float: A float representing the price_book_name
		"""

		return self.get_key_value('Price_Book_Name')

	def set_price_book_name(self, price_book_name):
		"""
		The method to set the value to price_book_name

		Parameters:
			price_book_name (float) : A float representing the price_book_name
		"""

		if price_book_name is not None and not isinstance(price_book_name, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: price_book_name EXPECTED TYPE: float', None, None)
		
		self.add_key_value('Price_Book_Name', price_book_name)

	def get_tax(self):
		"""
		The method to get the tax

		Returns:
			float: A float representing the tax
		"""

		return self.get_key_value('Tax')

	def set_tax(self, tax):
		"""
		The method to set the value to tax

		Parameters:
			tax (float) : A float representing the tax
		"""

		if tax is not None and not isinstance(tax, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tax EXPECTED TYPE: float', None, None)
		
		self.add_key_value('Tax', tax)

	def get_list_price(self):
		"""
		The method to get the list_price

		Returns:
			float: A float representing the list_price
		"""

		return self.get_key_value('List_Price')

	def set_list_price(self, list_price):
		"""
		The method to set the value to list_price

		Parameters:
			list_price (float) : A float representing the list_price
		"""

		if list_price is not None and not isinstance(list_price, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: list_price EXPECTED TYPE: float', None, None)
		
		self.add_key_value('List_Price', list_price)

	def get_unit_price(self):
		"""
		The method to get the unit_price

		Returns:
			float: A float representing the unit_price
		"""

		return self.get_key_value('unit_price')

	def set_unit_price(self, unit_price):
		"""
		The method to set the value to unit_price

		Parameters:
			unit_price (float) : A float representing the unit_price
		"""

		if unit_price is not None and not isinstance(unit_price, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: unit_price EXPECTED TYPE: float', None, None)
		
		self.add_key_value('unit_price', unit_price)

	def get_quantity_in_stock(self):
		"""
		The method to get the quantity_in_stock

		Returns:
			float: A float representing the quantity_in_stock
		"""

		return self.get_key_value('quantity_in_stock')

	def set_quantity_in_stock(self, quantity_in_stock):
		"""
		The method to set the value to quantity_in_stock

		Parameters:
			quantity_in_stock (float) : A float representing the quantity_in_stock
		"""

		if quantity_in_stock is not None and not isinstance(quantity_in_stock, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: quantity_in_stock EXPECTED TYPE: float', None, None)
		
		self.add_key_value('quantity_in_stock', quantity_in_stock)

	def get_total(self):
		"""
		The method to get the total

		Returns:
			float: A float representing the total
		"""

		return self.get_key_value('Total')

	def set_total(self, total):
		"""
		The method to set the value to total

		Parameters:
			total (float) : A float representing the total
		"""

		if total is not None and not isinstance(total, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: total EXPECTED TYPE: float', None, None)
		
		self.add_key_value('Total', total)

	def get_description(self):
		"""
		The method to get the description

		Returns:
			string: A string representing the description
		"""

		return self.get_key_value('Description')

	def set_description(self, description):
		"""
		The method to set the value to description

		Parameters:
			description (string) : A string representing the description
		"""

		if description is not None and not isinstance(description, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: description EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Description', description)

	def get_line_tax(self):
		"""
		The method to get the line_tax

		Returns:
			list: An instance of list
		"""

		return self.get_key_value('Line_Tax')

	def set_line_tax(self, line_tax):
		"""
		The method to set the value to line_tax

		Parameters:
			line_tax (list) : An instance of list
		"""

		if line_tax is not None and not isinstance(line_tax, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: line_tax EXPECTED TYPE: list', None, None)
		
		self.add_key_value('Line_Tax', line_tax)
