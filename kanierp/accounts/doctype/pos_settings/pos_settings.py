# Copyright (c) 2025, Kanivin Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class POSSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from kanierp.accounts.doctype.pos_field.pos_field import POSField
		from kanierp.accounts.doctype.pos_search_fields.pos_search_fields import POSSearchFields

		invoice_fields: DF.Table[POSField]
		pos_search_fields: DF.Table[POSSearchFields]
	# end: auto-generated types

	def validate(self):
		pass
