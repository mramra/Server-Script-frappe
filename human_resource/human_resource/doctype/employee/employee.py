# Copyright (c) 2023, Human Resource and contributors
# For license information, please see license.txt
# import frappe
from frappe import msgprint
from frappe.model.document import Document
import frappe.utils
class Employee(Document):
	def validate(self):
		if self.first_name and self.middle_name and self.last_name:
			self.full_name = self.first_name + " " + self.middle_name + " " + self.last_name
		else:
			frappe.throw("ادخال اسم موظف كامل")

		if self.date_of_birth:
			dob = self.date_of_birth
			now = frappe.utils.nowdate()
			diff = frappe.utils.date_diff(now, dob) // 365
			self.age = int(diff)
		else:
			frappe.throw("ادخال تاريخ الميلاد")

		if (self.status == "Active" and self.age >= 60):
			frappe.throw(" عمر موظف اكبر من 60")

		if len(self.mobile) != 10:
			frappe.throw("رقم موبايل غير كامل")

		if self.mobile.startswith("059"):
			pass
		else:
			frappe.throw("رقم موبايل يجب ان يبداء 059")

		self.count_employee_education=0
		for x in self.employee_education:
			self.count_employee_education =self.count_employee_education+1

		if self.count_employee_education < 2:
			frappe.throw("الشهادات يجب ان تكون شهادتين")



