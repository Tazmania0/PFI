# pfi/custom_scripts/bom_service_check.py
from erpnext.manufacturing.doctype.bom.bom import BOM

class CustomBOM(BOM):
    def validate(self):
        # Skip validation for Items if "Is Service" is checked
        if self.get("is_service_bom"):
            self.items = []  # Clear items table
            self.with_operations = 0  # Optional: Disable operations if needed
            self.operating_cost = 0
            return  # Skip ERPNext's standard validation
        super().validate()  # Run original validation for non-service BOMs

# Override the default BOM class
def override_bom_doc():
    return CustomBOM