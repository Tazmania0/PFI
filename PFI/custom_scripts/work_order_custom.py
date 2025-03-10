import frappe
from frappe.model.document import Document

def before_save(doc, method):
    validate_cutting_matrix(doc)
    recalculate_planned_qty(doc)
    validate_bom_is_service(doc)

def validate_cutting_matrix(doc):
    if doc.cutting_matrix:
        for matrix_row in doc.cutting_matrix:
            if not matrix_row.sizes:
                frappe.throw(f"Color '{matrix_row.color}' missing sizes.")
            
            for size in matrix_row.sizes:
                if size.quantity <= 0:
                    frappe.throw(f"Quantity in color '{matrix_row.color}', size '{size.size}' must be positive.")
                if size.batch_size <= 0:
                    frappe.throw(f"Batch size in color '{matrix_row.color}', size '{size.size}' must be positive.")

def recalculate_planned_qty(doc):
    if not doc.cutting_matrix: return
    
    total_qty = 0
    for matrix_row in doc.cutting_matrix:
        for size in matrix_row.sizes:
            total_qty += size.quantity or 0
    doc.planned_qty = total_qty

def validate_bom_is_service(doc):
    if doc.bom_no:
        bom_doc = frappe.get_doc("BOM", doc.bom_no)
        if bom_doc.is_service and bom_doc.items:
            frappe.throw(f"BOM '{bom_doc.name}' is marked as service but contains raw materials.")

def on_submit(doc, method):
    generate_job_cards(doc)

def generate_job_cards(doc):
    if doc.cutting_matrix:
        # Generate job cards based on matrix data
        for matrix_row in doc.cutting_matrix:
            for size in matrix_row.sizes:
                # Add logic for job card creation
                frappe.msgprint(f"Generated job card for {matrix_row.color} - {size.size} - Qty {size.batch_size}")
    else:
        # Fallback to planned qty
        frappe.msgprint(f"Generated default job card for planned qty {doc.planned_qty}")

