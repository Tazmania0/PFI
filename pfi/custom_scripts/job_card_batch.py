import frappe
from pfi.custom_scripts.cutting_matrix import process_cutting_matrix

@frappe.whitelist()
def generate_job_cards(work_order_doc):
    job_card_batches = []

    cutting_matrix = work_order_doc.get("cutting_matrix_table", [])
    size_table = work_order_doc.get("size_table", [])

    if cutting_matrix:
        for entry in cutting_matrix:
            color = entry.get("color")
            size = entry.get("size")
            batch_size = entry.get("batch_size")

            if batch_size <= 0:
                frappe.throw(f"Batch size must be positive for {color} / {size}")

            # Planned qty comes from size_table
            planned_qty_entry = next((s for s in size_table if s['color'] == color), None)
            if not planned_qty_entry:
                frappe.throw(f"No planned quantity found for {color}")

            planned_qty = planned_qty_entry.get("size", 0) # 'size' holds planned quantity now
            if planned_qty <= 0:
                frappe.throw(f"Planned quantity must be positive for {color}")

            num_batches = -(-planned_qty // batch_size)
            for i in range(num_batches):
                qty = min(batch_size, planned_qty - (i * batch_size))
                job_card_batches.append({
                    "color": color,
                    "size": size,
                    "quantity": qty
                })

    elif size_table:
        batch_size_default = work_order_doc.get("batch_size") or 1
        for entry in size_table:
            color = entry.get("color")
            planned_qty = entry.get("size") # 'size' is the planned quantity here

            num_batches = -(-planned_qty // batch_size_default)
            for i in range(num_batches):
                qty = min(batch_size_default, planned_qty - (i * batch_size_default))
                job_card_batches.append({
                    "color": color,
                    "quantity": qty
                })

    else:
        default_qty = work_order_doc.get("qty") or 1
        batch_size = work_order_doc.get("batch_size") or 1
        num_batches = -(-default_qty // batch_size)
        for i in range(num_batches):
            qty = min(batch_size, default_qty - (i * batch_size))
            job_card_batches.append({
                "quantity": qty
            })

    # Create job cards
    for batch in job_card_batches:
        jc = frappe.new_doc("Job Card")
        jc.work_order = work_order_doc.name
        jc.color = batch.get("color")
        jc.size = batch.get("size")
        jc.qty = batch.get("quantity")
        jc.insert()
        frappe.msgprint(f"Job Card created for {batch.get('color')} / {batch.get('size')} x {batch.get('quantity')}")


