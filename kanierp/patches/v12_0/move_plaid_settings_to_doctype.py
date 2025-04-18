# Copyright (c) 2025, Kanivin and Contributors
# License: GNU General Public License v3. See license.txt


import frappe


def execute():
	frappe.reload_doc("kanierp_integrations", "doctype", "plaid_settings")
	plaid_settings = frappe.get_single("Plaid Settings")
	if plaid_settings.enabled:
		if not (frappe.conf.plaid_client_id and frappe.conf.plaid_env and frappe.conf.plaid_secret):
			plaid_settings.enabled = 0
		else:
			plaid_settings.update(
				{
					"plaid_client_id": frappe.conf.plaid_client_id,
					"plaid_env": frappe.conf.plaid_env,
					"plaid_secret": frappe.conf.plaid_secret,
				}
			)
		plaid_settings.flags.ignore_mandatory = True
		plaid_settings.save()
