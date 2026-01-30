# Copyright (c) 2025, hvillanueva and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PurchaseRequisition(Document):
	def validate(self):
		items = self.items
		for item in items:
			calculated_order = item.order_qty - item.inv_onhand if item.order_qty >= item.inv_onhand else 0
			if item.final_order != calculated_order:
				item.final_order_changed = 1
				frappe.msgprint(f"Final Order for item {item.item_description} does not match calculated order.")
			else:
				item.final_order_changed = 0
	pass
