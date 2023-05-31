// Copyright (c) 2023, Lalit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ticket Booking Page', {	
	onload: function(frm) {
		cur_frm.disable_save();
		frm.set_value('booking_user','')
		frm.set_value('password','')
		// frm.set_value('check_user','')
		frm.set_value('user_validate','')
		frm.set_value('from_station','')
		frm.set_value('to_station','')
		frm.set_value('journey_date','')
		frm.clear_table('train')
		frm.set_value('traveller_full_nmae','')
		frm.set_value('age','')
		frm.set_value('gender','')
		frm.clear_table('data')
		frm.set_value('fare','')
		frm.set_value('gst','')
		frm.set_value('total_fare','')
		

		// frm.clear_fields('booking_user')
		// frm.refresh_fields('booking_user')
        
    },
	train_avalable: function(frm) {
		// var journeyDate = new Date(doc.getElementById(frm.doc.journey_date).Date);
		// if(!frm.doc.train){
		// 	frappe.throw("Thses Root Train Was Not Available")
		// }
		var journeyDate = frappe.datetime.str_to_user(frm.doc.journey_date);
		var currentDate = new Date();
		var formattedDate = moment(currentDate).format("DD-MM-YYYY");
		
		if(!frm.doc.journey_date){
			frappe.throw("Plese Select The Date")
		}
		if(journeyDate <= formattedDate) {
			frappe.throw("Please select a future date")
		}
		if(frm.doc.user_validate === "No" || !frm.doc.user_validate) {
			frappe.throw("Soryy You Don't Valid User")
		}
		
		// console.log(journeyDate)
		// console.log(formattedDate)

		
		frappe.call({
			method:"fetch_data",
			// method:"vali",	
			doc:frm.doc,		
			callback: function(r){
				// console.log(r)
				
				frm.refresh_fields("train")
				// frm.doc.save();
				// frm.clear_table('train')	
				
				// frm.refresh_fields('train')
			}
		}	
		 )		
	},
	// onload: function(frm){
	// 	frappe.call({
	// 		method:"refer",
	// 		doc:frm.doc,
	// 	})
	// },
	
	add_data: function(frm){
		if(!frm.doc.train){
			frappe.throw("Plese check train")
		}
		if(!frm.doc.traveller_full_nmae,!frm.doc.age,!frm.doc.gender)
			frappe.throw("Plese Fil The User Fields....")
		frappe.call({
			method:"child",
			doc:frm.doc,
			callback: function(r){
				frm.refresh_fields('data')
				
				
				frm.set_value('traveller_full_nmae','')
				frm.set_value('age','')
				frm.set_value('gender','')
				
			}
		})
	},
	check_amount: function(frm){	
			
		frappe.call({
			method:"before",
			doc:frm.doc,
			
			callback: function(r){
				// frm.set_value('data',)
				// frm.clear_table('data')
				frm.refresh_fields('data')
				// frm.doc.save();	
				
				
				
			}
		})
	},
	
	book_ticket: function(frm){
		//
		frappe.warn('Are you sure you want to proceed?')
		if (!frm.doc.booking_user,!frm.doc.password,!frm.doc.user_validate,!frm.doc.from_station,!frm.doc.to_station,
			!frm.doc.journey_date,!frm.doc.train,!frm.doc.traveller_full_nmae,!frm.doc.age,!frm.doc.gender,!frm.doc.data,!frm.doc.fare,!frm.doc.total_fare) {
			frappe.throw("Please Fillup These All Fields");
		}
		else{
			// frappe.msgprint("Data Is Stored")
			// frm.refresh_fields('data')
			// frm.set_value('booking_user','')
			// frm.set_value('password','')
			// // frm.set_value('check_user','')
			// frm.set_value('user_validate','')
			// frm.set_value('from_station','')
			// frm.set_value('to_station','')
			// frm.set_value('journey_date','')
			// frm.clear_table('train')
			// frm.set_value('traveller_full_nmae','')
			// frm.set_value('age','')
			// frm.set_value('gender','')
			// frm.clear_table('data')
			// frm.set_value('fare','')
			// frm.set_value('gst','')
			// frm.set_value('total_fare','')
			// frm.set_value('book_ticket','')
			frappe.call({
				method:"push_data",
				doc:frm.doc,
				callback: function(r){
					
				}
				
			})
			
		}
		
	
		
	}

		})
	// },

	

	// onclick: function(frm){
		
		

	// }
// });
frappe.ui.form.on('Ticket Booking Page', {
	check_user: function(frm) {
			frappe.call({
				method:"user",	
				doc:frm.doc,		
				callback: function(r){
					// console.log(r)
					// if(r.message == "Yes"){
					// 	frappe.set_value("Yes")
					frm.refresh_fields("check_user")
					
					}
					
				}
			// },
			 )		
		}
	});

frappe.ui.form.on('Train Details_child',{
	check_box: function(frm, cdt, cdn) {
		var child_table = locals[cdt][cdn];
		
		
		if (child_table.check_box) {
			
			$.each(frm.doc.train || [], function(i, row) {
				if (row.name != child_table.name && row.check_box) {
					frappe.model.set_value(row.doctype, row.name, 'check_box', false);
					
				}
			});
		}
		
	}
});


	
