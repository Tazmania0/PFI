# pfi/custom_scripts/bom_service_check.py
from frappe import _
from erpnext.manufacturing.doctype.bom.bom import BOM

class CustomBOM(BOM):
    def validate(self):
        # Clear Items table if "Is Service" is checked
        if self.is_service_bom:
            self.items = []
        
        # Validate Operations if "With Operations" is checked (applies to all BOMs)
        if self.with_operations and not self.operations:
            frappe.throw(_("Operations are required when 'With Operations' is checked."))
        
        # Run standard validation for non-service BOMs (checks Items)
        if not self.is_service_bom:
            super().validate()