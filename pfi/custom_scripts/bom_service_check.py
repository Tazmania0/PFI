# pfi/custom_scripts/bom_service_check.py
from frappe import _
from erpnext.manufacturing.doctype.bom.bom import BOM

class CustomBOM(BOM):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        frappe.log_error("CustomBOM initialized", "Debug")  # Debug line

class CustomBOM(BOM):
    def validate(self):
        frappe.log_error("CustomBOM validate called", "DEBUG")
        frappe.throw("Custom Validation Active!")  # Test line
        # Skip validation entirely for service BOMs
        if self.is_service_bom:
            self.items = []
            self.flags.ignore_mandatory = True  # Bypass mandatory checks
            self.flags.ignore_validate = True  # Skip ERPNext's validate method
            return

        # For non-service BOMs, run standard validation
        super().validate()

        # Validate Operations if "With Operations" is checked
        if self.with_operations and not self.operations:
            frappe.throw(_("Operations are required when 'With Operations' is checked."))