# Copyright (c) 2024, Code Venturers and contributors
# For license information, please see license.txt

import frappe
from frappe import _, bold
from frappe.utils.jinja import validate_template

from frappe.model.document import Document


class ReportPrintFormat(Document):
	def validate(self):
		pass
		# if self.html:
		# 	validate_template(self.html)

	@frappe.whitelist()
	def make_default(self):
		if self.disabled:
			frappe.throw(_("The document {} is disabled..".format(bold(self.name))))
		
		if default_print := frappe.db.get_value(
			"Report Print Format", {"report": self.report, "default": 1}, "name"
		):
			report_print_doc = frappe.get_doc("Report Print Format", default_print)
			report_print_doc.db_set("default", 0)
		self.db_set("default", 1)

		frappe.msgprint(
			_("{0} is now default print format for {1} report").format(
				frappe.bold(self.name), frappe.bold(self.report)
			)
		)
