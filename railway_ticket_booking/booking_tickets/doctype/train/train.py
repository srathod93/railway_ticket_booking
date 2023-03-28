# Copyright (c) 2023, Lalit and contributors
# For license information, please see license.txt
# from datetime import datetime

import frappe
from frappe.model.document import Document
from frappe.utils import  get_time
from datetime import datetime

class Train(Document):
	def validate(self):
		if self.from_station == self.to_station:
			frappe.throw("You Dont select Same station")

		
		# self.save()
		# self.rate_per_ticket.save()
		# self.available_tickets.save()
	@frappe.whitelist()
	def val(self):
		# ded=frappe.get_all('Ticket Booking Page',,['data'])
		# print("###################3",ded)

		# i=(self.end_time)
		# o=(self.start_time)
		# print(i - o)
		# if self.from_station == "Surat" and self.to_station == "Ahemdabad":
		# start_time = frappe.db.get_value('Train', 'start_time')
		# end_time = frappe.db.get_value('Train', 'end_time')
		# start_time_obj = datetime.strptime(str(start_time), '%Y-%m-%d %H:%M:%S')
		# end_time_obj = datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S')
		# time_difference = end_time_obj - start_time_obj
		# print("########################################",time_difference)
		# a=get_time(self.start_time)
		# b=get_time(self.end_time)
		# print("##############",int(a-b))
		self.rate_per_ticket=self.distance *13
		self.available_tickets=self.number_of_boggy * self.occupency_perboggy
		self.total_citing_capacity=self.number_of_boggy * self.occupency_perboggy

		# print("########",self.rate_per_ticket,self.available_tickets)
		from_time_obj = datetime.strptime(self.start_time, '%H:%M:%S')
		end_time_obj = datetime.strptime(self.end_time, '%H:%M:%S')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
		time_difference = end_time_obj - from_time_obj

# print the time difference in minutes
		p=(time_difference.seconds // 60)
		j=p//60
		# print("###################################",j,"Houres")
		if j <= 1:
			# print("############################",p,"Minutes")
			self.total_journey_time=(f"{p} Minutes")
			# frappe.db.set_value("Train",self.total_journey_time,"total_journey_time",p)
		else:
			# print("###################################",j,"Houres")
			self.total_journey_time=(f"{j} Houres")
			# frappe.db.set_value("Train",'j')
	
	

		