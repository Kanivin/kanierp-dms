// Copyright (c) 2025, Kanivin Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Customer-wise Item Price"] = {
	filters: [
		{
			label: __("Customer"),
			fieldname: "customer",
			fieldtype: "Link",
			options: "Customer",
			reqd: 1,
		},
		{
			label: __("Item"),
			fieldname: "item",
			fieldtype: "Link",
			options: "Item",
			get_query: () => {
				return {
					query: "kanierp.controllers.queries.item_query",
					filters: { is_sales_item: 1 },
				};
			},
		},
	],
};
