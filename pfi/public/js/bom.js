// bom.js
frappe.ui.form.on('BOM', {
    refresh: function(frm) {
        frm.toggle_display(['operations'], !frm.doc.is_service_bom);
    },
    _is_service: function(frm) {
        frm.toggle_display(['operations'], !frm.doc._is_service_bom);
    }
});