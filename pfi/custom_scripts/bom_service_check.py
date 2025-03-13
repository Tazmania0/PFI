# pfi/custom_scripts/bom_service_check.py
from frappe import _
from erpnext.manufacturing.doctype.bom.bom import BOM

class CustomBOM(BOM):
    def validate(self):
      frappe.log_error("CustomBOM validate called", "DEBUG")
      
      if self.is_service_bom:
            # Bypass all validation for service BOMs
            self.items = []
            self.flags.ignore_mandatory = True
            return

        # Run standard validation for non-service BOMs
        super().validate()

        # Validate Operations if "With Operations" is checked
        if self.with_operations and not self.operations:
            frappe.throw(_("Operations are required when 'With Operations' is checked."))

  