# Copyright (c) 2023, Lalit and addtributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import datetime
# from frappe import PasswordField
# from frappe.utils.password import check_password
# from frappe.utils.password import get_password_hash

class TicketBookingPage(Document):	
	@frappe.whitelist()
	def user(self):
		
		# sales_order = frappe.get_doc('Train', self.train_name)
		
		# password = frappe.db.PasswordField("Booking User","password")
		# p=self.train_name
		# print("##################################3",p.train_name)
		# print(password)

	# def validate(self):
		password1 = frappe.get_doc('Booking User',{'name':self.booking_user}).get_password("password")
		# print("########33",password1)
		if password1 == self.password:
			# print("@@@@@@@@@@@@@@@@@@@",self.user_validate)
			self.user_validate="Yes"
			# print("##################3",self.user_validate)
			frappe.msgprint("valid user")
		else:
			self.user_validate="No"
			frappe.throw("You Dont Valid User")
		# return get_password_hash(password) == hashed_password
		# print(password)

		# j=frappe.get_all('Train','train_name')
		# print(j)
	@frappe.whitelist()
	def fetch_data(self):
		if self.from_station == self.to_station:		
			frappe.throw("You Dont select Same station")
		elif self.from_station == "" or self.to_station == "":
			frappe.throw("Plese select The station..")

		invoices = frappe.db.get_all('Train',{'from_station':self.from_station,'to_station':self.to_station},['train_name','train_type','from_station','to_station','distance','start_time',
		'end_time','total_journey_time','available_tickets','rate_per_ticket'])
		if invoices:
			pass
		else:		
			frappe.throw("These Root Train Not Available..")
		
	
		
		
		self.train=[]
		for i in invoices:			
				self.append('train',{
					'train_type':i.train_type,
					'train_name':i.train_name,
					'from_station':i.from_station,
					'to_station':i.to_station,
					'distance':i.distance,
					'start_time':i.start_time,
					'end_time':i.end_time,
					'total_journey_time':i.total_journey_time,
					'available_tickets':i.available_tickets,
					'rate_per_ticket':i.rate_per_ticket
				})
				if i.check_box == 1:
					i.available_tickets=i.available_tickets-(len(self.data))
					frappe.db.update()
					frappe.save()
				
	@frappe.whitelist()
	def child(self):	
		self.append('data',{ #these was field name
			'traveller_name':self.traveller_full_nmae,
			'age':self.age,
			'gender':self.gender
		}
		)
		data=self.data
		
		for details in data:
			traveler_name = details.get("traveller_name")
			age = details.get("age")
			gender = details.get("gender")
			p=[traveler_name,age,gender]

		p=(len(data))
	@frappe.whitelist()
	def before(self):
		# print("##############")
		
		for i in self.train:
			if i.check_box == 1:

				r=(i.rate_per_ticket*(len(self.data)))
				self.fare=r
				self.gst='12%'
				e=self.fare*.12
				self.total_fare=e+self.fare
	@frappe.whitelist()
	def push_data(self):
		
		add = frappe.new_doc("Booking Details")
		add.prnno = random.randint(1111111111,9999999999)
		add.journey_date = self.journey_date
		for td in self.train:
			if td.check_box == 1:
				add.train = td.train_name
				add.from_station = td.from_station
				add.to_station = td.to_station
				add.distance = td.distance
				add.start_time = td.start_time
				add.end_time = td.end_time
				add.available = td.available_tickets
				add.rate_per_ticket = td.rate_per_ticket
				add.ticketes_quntity=len(self.data)
				m=td.available_tickets-len(self.data)
				l=frappe.get_doc("Train",{"from_station":self.from_station,"to_station":self.to_station,"train_name":td.train_name})
				# print("##########0#",l)
				l.set("available_tickets",m)
				l.save(ignore_permissions=True)
				add.book_ticket=l.set("available_tickets",m)

			# if len(self.data) >= 0:
				# add.traveller_name = td.traveller_full_nmae
				# add.age = td.age
				# add.gender = td.gender
				# # l.available_tic kets=m
				
		for dt in self.data:
			add.append("traveler_details",{
				"traveller_name":dt.traveller_name,
				"age":dt.age,
				"gender":dt.gender
			})
			# add.traveller_name = 
			# add.age = 
			# add.gender = dt.gender 

		add.fare = self.fare 
		
		add.gst = self.gst
		add.total_fare = self.total_fare
		add.save(ignore_permissions=True)
	# @frappe.whitelist()
	# def vali(self):
	# 	today = datetime.date.today()
	# 	if self.journey_date <= today:
	# 		frappe.throw("Please select Current Date")
			