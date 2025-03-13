# pfi/custom_scripts/bom_service_check.py
# pfi/custom_scripts/bom_service_check.py
from frappe import _
from erpnext.manufacturing.doctype.bom.bom import BOM

class CustomBOM(BOM):
    def validate(self):
        # Clear Items table and skip validation if "Is Service" is checked
        if self.is_service_bom:
            self.items = []
            return  # Skip standard validation
        
        # Validate Operations if "With Operations" is checked
        if self.with_operations and not self.operations:
            frappe.throw(_("Operations are required when 'With Operations' is checked."))
        
        # Run standard validation for non-service BOMs
        super().validate()
        
# Override the default BOM class
def override_bom_doc():
    return CustomBOM