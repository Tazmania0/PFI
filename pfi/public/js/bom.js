// pfi/public/js/bom.js
frappe.ui.form.on('BOM', {
    onload: function(frm) {
        // Initial setup: Hide "is_service_bom" if "With Operations" is unchecked
        frm.toggle_display('_is_service', frm.doc.with_operations);
    },
    refresh: function(frm) {
        // Toggle Items visibility/requirement
        frm.toggle_display('items', !frm.doc.is_service_bom);
        frm.toggle_reqd('items', !frm.doc.is_service_bom);
        
        // Toggle Operations requirement
        frm.toggle_reqd('operations', frm.doc.with_operations);
    },
    with_operations: function(frm) {
        // Show/hide "is_service_bom" based on "With Operations"
        frm.toggle_display('is_service_bom', frm.doc.with_operations);
        
        // Uncheck "_is_service" if "With Operations" is unchecked
        if (!frm.doc.with_operations && frm.doc.is_service_bom) {
            frm.set_value('is_service_bom', 0);
        }
    },
    _is_service: function(frm) {
        // Clear Items table and toggle visibility
        frm.toggle_display('items', !frm.doc.is_service_bom);
        frm.toggle_reqd('items', !frm.doc.is_service_bom);
        if (frm.doc.is_service_bom) {
            frm.clear_table('items');
            frm.refresh_field('items');
        }
    }
});