# pfi/custom_scripts/bom_events.py
import frappe
from frappe import _

def validate_bom(doc, method):
    # Skip validation for service BOMs
    if doc.is_service_bom:
        doc.items = []  # Clear items table
        doc.flags.ignore_mandatory = True  # Bypass mandatory checks

    # Validate Operations if "With Operations" is checked
    if doc.with_operations and not doc.operations:
        frappe.throw(_("Operations are required when 'With Operations' is checked."))