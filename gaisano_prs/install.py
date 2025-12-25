import frappe
from frappe.permissions import add_permission, update_permission_property

def after_install():
    create_roles()
    add_permissions_to_roles()

def create_roles():
    roles = ["Inventory Manager"]
    for role in roles:
        try:
            frappe.get_doc("Role", role)
        except:
            frappe.get_doc({
                "doctype": "Role",
                "role_name": role,
                "desk_access": 1
            }).insert()

        else:
            continue
def add_permissions_to_roles():
    roles = ["Inventory Manager"]
    doctypes = ["Purchase Requisition", "Requisition Item", "Project", "Branch", "Department","Requisitioner"]
    #Add generic permissions to roles
    for role in roles:
        if not frappe.db.exists("Role", role):
            continue
        ptype = ["read", "write", "report"] #ptype with permissions = 1
        ptype_0 = ["create", "delete", "submit", "cancel", "amend"] #ptype with permissions = 0
        for dt in doctypes:
            # this adds read permission to the role
            add_permission(dt, role)
            for p in ptype:
                # now we update the above role to have all permissions from the ptype
                update_permission_property(dt, role, 0, p, 1)
            for p0 in ptype_0:
                # now we update the above role to have all permissions from the ptype
                update_permission_property(dt, role, 0, p0, 0)
    
    roles=[]