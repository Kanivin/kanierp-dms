# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# See license.txt

import frappe
from frappe.tests.utils import KanivinTestCase
from frappe.utils import add_days, today

from kanierp.maintenance.doctype.maintenance_schedule.test_maintenance_schedule import (
	make_serial_item_with_serial,
)


class TestStockLedgerReeport(KanivinTestCase):
	def setUp(self) -> None:
		make_serial_item_with_serial("_Test Stock Report Serial Item")
		self.filters = frappe._dict(
			company="_Test Company",
			from_date=today(),
			to_date=add_days(today(), 30),
			item_code="_Test Stock Report Serial Item",
		)

	def tearDown(self) -> None:
		frappe.db.rollback()
