# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


import frappe


def execute():
	for report in ["Delayed Order Item Summary", "Delayed Order Summary"]:
		if frappe.db.exists("Report", report):
			frappe.delete_doc("Report", report)
