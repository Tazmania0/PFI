from frappe import _

app_name = "PFI"
app_title = "ERPNext Customizations"
app_publisher = "Your Company Name"
app_description = "Customizations for ERPNext tailored to garment manufacturing, job cards, and BOM workflows."
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "your.email@company.com"
app_license = "MIT"
app_version = "1.0.0"

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