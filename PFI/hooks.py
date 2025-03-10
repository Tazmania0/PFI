from frappe import _

doc_events = {
    "Work Order": {
        "before_submit": "PFI.custom_scripts.work_order_custom.before_submit_work_order"
    },
    "BOM": {
        "validate": "PFI.custom_scripts.bom_service_check.validate_bom"
    }
    "Work Order": {
        "before_save": "PFI.work_order_validate.before_save"
    } 
}
fixtures = ["Custom Field", "Print Format"]

app_include_js = "/assets/PFI/js/work_order.js"
app_include_css = "/assets/PFI/css/work_order.css"