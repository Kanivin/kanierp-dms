frappe.treeview_settings["Warehouse"] = {
	get_tree_nodes: "kanierp.stock.doctype.warehouse.warehouse.get_children",
	add_tree_node: "kanierp.stock.doctype.warehouse.warehouse.add_node",
	get_tree_root: false,
	root_label: "Warehouses",
	filters: [
		{
			fieldname: "company",
			fieldtype: "Select",
			options: kanierp.utils.get_tree_options("company"),
			label: __("Company"),
			default: kanierp.utils.get_tree_default("company"),
		},
	],
	fields: [
		{ fieldtype: "Data", fieldname: "warehouse_name", label: __("New Warehouse Name"), reqd: true },
		{
			fieldtype: "Check",
			fieldname: "is_group",
			label: __("Is Group"),
			description: __("Child nodes can be only created under 'Group' type nodes"),
		},
	],
	ignore_fields: ["parent_warehouse"],
};
