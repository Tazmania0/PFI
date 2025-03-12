import json
import frappe
import os

def execute():
    app_path = frappe.get_app_path('pfi')

    # Load Cutting Matrix Table
    with open(os.path.join(app_path, 'manufacturing', 'cutting_matrix_table', 'cutting_matrix_table.json')) as f:
        doc = json.load(f)
        if not frappe.db.exists("DocType", doc.get("name")):
            frappe.get_doc(doc).insert(ignore_permissions=True)
            print(f"Created {doc.get('name')}")

    # Load Size Table
    with open(os.path.join(app_path, 'manufacturing', 'size_table', 'size_table.json')) as f:
        doc = json.load(f)
        if not frappe.db.exists("DocType", doc.get("name")):
            frappe.get_doc(doc).insert(ignore_permissions=True)
            print(f"Created {doc.get('name')}")


