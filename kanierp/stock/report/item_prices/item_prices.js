// Copyright (c) 2025, Kanivin Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Item Prices"] = {
	filters: [
		{
			fieldname: "items",
			label: __("Items Filter"),
			fieldtype: "Select",
			options: "Enabled Items only\nDisabled Items only\nAll Items",
			default: "Enabled Items only",
		},
	],
};
