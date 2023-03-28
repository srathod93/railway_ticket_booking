# Copyright (c) 2023, Lalit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ReportAnalysis(Document):
	# @frappe.whitelist()
	def validate(self):
		d=frappe.db.get_all('Booking Details',['prnno','journey_date','from_station','to_station','train',
				    'traveller_full_name','gender','age','ticketes_quntity','fare','gst','total_fare','available_ticketes'])
		print("#########",d)
		for i in d:
			self.journey_date=i.journey_date
			self.total_tickets=i.ticketes_quntity
			print("#########################3",i.journey_date)