// pfi/public/js/bom.js
frappe.ui.form.on('BOM', {
    refresh: function(frm) {
        // Toggle visibility of "Is Service" based on "With Operations"
        frm.toggle_display('is_service_bom', frm.doc.with_operations);
        
        // Toggle Items visibility and clear if "Is Service" is checked
        frm.toggle_display('items', !frm.doc.is_service_bom);
        if (frm.doc.is_service_bom) {
            frm.clear_table('items');
            frm.refresh_field('items');
        }
        
        // Toggle Operations requirement
        frm.toggle_reqd('operations', frm.doc.with_operations);
    },
    with_operations: function(frm) {
        // Update "Is Service" visibility and reset if needed
        frm.toggle_display('is_service_bom', frm.doc.with_operations);
        if (!frm.doc.with_operations && frm.doc.is_service_bom) {
            frm.set_value('is_service_bom', 0);
        }
    },
    is_service_bom: function(frm) {
        // Clear Items table and hide it
        frm.toggle_display('items', !frm.doc.is_service_bom);
        if (frm.doc.is_service_bom) {
            frm.clear_table('items');
            frm.refresh_field('items');
        }
    }
});