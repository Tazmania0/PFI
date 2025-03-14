from frappe import _

app_name = "pfi"
app_title = "PFI"
app_publisher = "PFI"

app_description = "Custom ERPNext App for Garment Manufacturing and Job Card Customization"
#app_icon = "octicon octicon-file-directory"
app_color = "gray"
app_email = "your@email.com"

app_license = "MIT"

app_version = "1.0.0"



def override_bom_class():
    from erpnext.manufacturing.doctype.bom.bom import BOM as OriginalBOM
    from pfi.custom_scripts.bom_service_check import CustomBOM

    # Monkey-patch the BOM class
    OriginalBOM.__bases__ = (CustomBOM,)

# Run the override on app initialization
app_initialized = {
    "after_migrate": override_bom_class
}



doc_events = {
#    "Work Order": {
#        "before_submit": "pfi.custom_scripts.work_order_custom.before_submit_work_order"
#    },
#    "Work Order": {
#
#        "validate": "pfi.work_order_custom.validate_work_order"
#
#    },
#    "Work Order": {
#        "before_save": "pfi.custom_scripts.work_order_validate.before_save"
#    } 
}
doc_events = {
#    "BOM": {
#        "before_validate": "pfi.custom_scripts.bom_events.validate_bom"
    }
}

# hooks.py
override_doctype_class = {
    "BOM": "pfi.custom_scripts.bom_service_check.CustomBOM"
}

include_js = {
    "public/js/pfi.js"
}

# Include JS for Work Order and Job Card (client-side logic)

doctype_js = {
#    "Work Order": "public/js/work_order_custom.js",
#    "Cutting Matrix Table": "doctype/manufacturing/cutting_matrix_table/cutting_matrix_table.js",
#    "Size Table": "doctype/manufacturing/size_table/size_table.js",
    "BOM": "public/js/bom.js"

#    "Job Card": "public/js/job_card_custom.js"

}

after_migrate = [
    "pfi.patches.v1_0_0.add_custom_field_to_bom.execute"
]