// Copyright (c) 2023, Lalit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Train', {
	refersh: function(frm) {
		frappe.call({
	 	method:"val",
		doc:frm.doc,
		callback: function(r){
			frm.refresh_fields("available_tickets")
		}
	})	
}
});
