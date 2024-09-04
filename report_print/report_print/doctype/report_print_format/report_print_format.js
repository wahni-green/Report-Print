// Copyright (c) 2024, Code Venturers and contributors
// For license information, please see license.txt

frappe.ui.form.on('Report Print Format', {
	refresh: function(frm) {
		if (!frm.doc.default){
			frm.add_custom_button(__("Set as Default"), function () {
				frm.call({
					doc: frm.doc,
					method: "make_default",
					callback: function () {
						frm.refresh();
					},
				});
			});
		}
	}
});
