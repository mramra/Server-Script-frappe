# Copyright (c) 2023, Human Resource and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
class LeaveApplication(Document):
    def validate(self):
        doc = frappe.db.get_value('leave Allocation', {'employee': self.employee},['employee', 'leave_type','total_leaves_allocated'])
        if self.leave_type==doc[1]:
            self.leave_balance=doc[2]

        diff = frappe.utils.date_diff(self.to_date, self.from_date)
        year=diff//365
        month = (diff - (year * 365)) // 30
        day = ((diff - (year * 365)) - (month * 30))
        self.total_leave_days=day

        if  self.total_leave_days <= int(doc[2]):
            frappe.db.set_value('leave Allocation', doc, {'total_leaves_allocated': int(doc[2])-day})
        else:
            frappe.throw("رصيد اجازات غير متاح")
