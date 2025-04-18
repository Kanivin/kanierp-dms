# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# License: MIT. See LICENSE


import frappe


def execute():
	navbar_settings = frappe.get_single("Navbar Settings")
	for item in navbar_settings.help_dropdown:
		if item.is_standard and item.route == "https://kanierp.com/docs/user/manual":
			item.route = "https://docs.kanierp.com/docs/v14/user/manual/en/introduction"

	navbar_settings.save()
