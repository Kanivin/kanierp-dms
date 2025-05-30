# Copyright (c) 2025, Kanivin Pvt. Ltd. and contributors
# For license information, please see license.txt


# import frappe
from frappe.model.document import Document


class ProcessStatementOfAccountsCustomer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		billing_email: DF.Data | None
		customer: DF.Link
		customer_name: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		primary_email: DF.ReadOnly | None
	# end: auto-generated types

	pass
