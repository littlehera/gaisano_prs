// Copyright (c) 2025, hvillanueva and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Purchase Requisition", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Requisition Item", "inv_onhand", function(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    if (row.inv_onhand < row.order_qty) {
        row.final_order = row.order_qty - row.inv_onhand;
        frappe.model.set_value(cdt, cdn, "final_order", row.final_order);
        frm.refresh_field("items");
    }
    else{
        row.final_order = 0;
        frappe.model.set_value(cdt, cdn, "final_order", row.final_order);
        frm.refresh_field("items");
    }
});

frappe.ui.form.on("Requisition Item", "order_qty", function(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    if (row.inv_onhand < row.order_qty) {
        row.final_order = row.order_qty - row.inv_onhand;
        frappe.model.set_value(cdt, cdn, "final_order", row.final_order);
        frm.refresh_field("items");
    }
    else{
        row.final_order = 0;
        frappe.model.set_value(cdt, cdn, "final_order", row.final_order);
        frm.refresh_field("items");
    }
});