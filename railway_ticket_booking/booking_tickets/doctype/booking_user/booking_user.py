# Copyright (c) 2023, Lalit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BookingUser(Document):
	def validate(self):
		if self.age <= 18:
			frappe.throw(f"You Dont Valid Only 18+ can aply Your age Is {self.age}")
