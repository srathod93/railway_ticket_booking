// Copyright (c) 2023, Lalit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Booking User', {
	validate: function(frm) {
		frm.set_value("full_name",frm.doc.user_name +" "+ frm.doc.last_name)

	}
});
