# pfi/custom_scripts/bom_service_check.py
from frappe import _
from erpnext.manufacturing.doctype.bom.bom import BOM

class CustomBOM(BOM):
    def validate(self):
        # Skip all validation for service BOMs
        if self.is_service_bom:
            self.flags.ignore_mandatory = True  # Bypass mandatory checks
            self.items = []  # Force clear items
            return  # Skip rest of validation

        # For non-service BOMs, validate Operations if "With Operations" is checked
        if self.with_operations and not self.operations:
            frappe.throw(_("Operations are required when 'With Operations' is checked."))

        # Run standard validation for non-service BOMs
        super().validate()