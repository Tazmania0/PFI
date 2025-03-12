import frappe

def execute():
    # Check if the custom field exists
    if not frappe.db.exists('Custom Field', 'BOM-is_service'):
        frappe.get_doc({
            'doctype': 'Custom Field',
            'dt': 'BOM',
            'fieldname': 'is_service_bom',
            'label': 'Is Service',
            'fieldtype': 'Check',
            'insert_after': 'description',
            'default': 0
        }).insert(ignore_permissions=True)
        print("Custom Field 'is_service' added to BOM")