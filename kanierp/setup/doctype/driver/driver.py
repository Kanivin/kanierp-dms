# Copyright (c) 2025, Kanivin Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class Driver(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from kanierp.setup.doctype.driving_license_category.driving_license_category import (
			DrivingLicenseCategory,
		)

		address: DF.Link | None
		cell_number: DF.Data | None
		driving_license_category: DF.Table[DrivingLicenseCategory]
		employee: DF.Link | None
		expiry_date: DF.Date | None
		full_name: DF.Data
		issuing_date: DF.Date | None
		license_number: DF.Data | None
		naming_series: DF.Literal["HR-DRI-.YYYY.-"]
		status: DF.Literal["Active", "Suspended", "Left"]
		transporter: DF.Link | None
	# end: auto-generated types

	pass
