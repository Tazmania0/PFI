# pfi/custom_scripts/bom_service_check.py
from frappe import _
from erpnext.manufacturing.doctype.bom.bom import BOM

class CustomBOM(BOM):
    def validate(self):
        frappe.log_error("CustomBOM validate called", "DEBUG")
        if self.is_service_bom:
            # Force clear items and bypass validation
            self.items = []
            self.flags.ignore_mandatory = True  # Bypass mandatory checks
            return  # Skip all parent validation

        # For non-service BOMs, validate normally
        super().validate()

        # Additional check for operations
        if self.with_operations and not self.operations:
            frappe.throw(_("Operations are required when 'With Operations' is checked."))