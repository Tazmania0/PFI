// pfi/public/js/bom.js
frappe.ui.form.on('BOM', {
    refresh: function(frm) {
        // Initialize visibility
        frm.toggle_display('is_service_bom', frm.doc.with_operations);
        frm.toggle_display('items', !frm.doc.is_service_bom);
        
        // Clear items if service BOM
        if (frm.doc.is_service_bom) {
            frm.clear_table('items');
            frm.refresh_field('items');
        }
    },
    with_operations: function(frm) {
        // Toggle "Is Service" visibility
        frm.toggle_display('is_service_bom', frm.doc.with_operations);
        if (!frm.doc.with_operations && frm.doc.is_service_bom) {
            frm.set_value('is_service_bom', 0);
        }
    },
    is_service_bom: function(frm) {
        // Clear and hide items
        frm.toggle_display('items', !frm.doc.is_service_bom);
        if (frm.doc.is_service_bom) {
            frm.clear_table('items');
            frm.refresh_field('items');
        }
    }
});