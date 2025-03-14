# pfi/custom_scripts/bom_service_check.py

from frappe import _
from erpnext.manufacturing.doctype.bom.bom import BOM as OriginalBOM
class CustomBOM(OriginalBOM):
    def validate_materials(self):
        """Override to skip raw material validation for service BOMs"""
        # Debug message 
        frappe.msgprint("Skipping raw material validation for Service BOM")
        
        if self.is_service_bom:
            return  # Skip validation for service BOMs
            
        # Run original validation for non-service BOMs
        super().validate_materials()

    def calculate_rm_cost(self, save=False):
        """Override to exclude raw material cost calculation for service BOMs"""
        if self.is_service_bom:
            # Clear raw material costs for service BOMs
            self.raw_material_cost = 0
            self.base_raw_material_cost = 0
            return
            
        # Run original calculation for non-service BOMs
        super().calculate_rm_cost(save)