# Copyright (c) 2025, Kanivin Pvt. Ltd. and Contributors
# See license.txt

import unittest

import frappe


class TestIssuePriority(unittest.TestCase):
	def test_priorities(self):
		make_priorities()
		priorities = frappe.get_list("Issue Priority")

		for priority in priorities:
			self.assertIn(priority.name, ["Low", "Medium", "High"])


def make_priorities():
	insert_priority("Low")
	insert_priority("Medium")
	insert_priority("High")


def insert_priority(name):
	if not frappe.db.exists("Issue Priority", name):
		frappe.get_doc({"doctype": "Issue Priority", "name": name}).insert(ignore_permissions=True)
