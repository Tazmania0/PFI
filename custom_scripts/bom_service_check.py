import frappe

def validate_bom(doc, method):
    if doc.get("is_service"):
        if doc.items:
            frappe.throw("Service BOM cannot include raw materials.")
