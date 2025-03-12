# add_custom_field_to_bom.py
import frappe

def execute():
    frappe.reload_doctype("BOM")  # Reload BOM DocType schema
    create_custom_field()

def create_custom_field():
    custom_field = {
        "dt": "BOM",
        "label": "Is Service",
        "fieldname": "is_service_bom",
        "fieldtype": "Check",
        "insert_after": "transfer_material_against",  # Adjust placement
        "description": "Check if this BOM is for a service (non-stock item)."
    }
    frappe.get_doc({
        "doctype": "Custom Field",
        **custom_field
    }).insert(ignore_permissions=True)