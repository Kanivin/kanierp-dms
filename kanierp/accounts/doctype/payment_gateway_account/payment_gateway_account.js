// Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.ui.form.on("Payment Gateway Account", {
	refresh(frm) {
		kanierp.utils.check_payments_app();
		if (!frm.doc.__islocal) {
			frm.set_df_property("payment_gateway", "read_only", 1);
		}
	},
});
