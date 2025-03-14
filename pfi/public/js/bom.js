// pfi/public/js/bom.js
frappe.ui.form.on('BOM', {
    refresh: function(frm) {
        // Initialize visibility of "Is Service" and Items table
        frm.toggle_display('is_service_bom', frm.doc.with_operations);
        frm.toggle_display('items', !frm.doc.is_service_bom);
        
        // Clear Items table if "Is Service" is checked
        if (frm.doc.is_service_bom) {
            frm.clear_table('items');
            frm.refresh_field('items');
        }
    },
    with_operations: function(frm) {
        // Toggle "Is Service" visibility and reset if needed
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
	
    // Override client-side mandatory check
    before_save: function(frm) {
        if (frm.doc.is_service_bom) {
            // Bypass items check for service BOMs
            frm.doc.items = [];
            frm.refresh_field('items');
        }
    },

    // UI Handling
    refresh: function(frm) {
        frm.toggle_display('is_service_bom', frm.doc.with_operations);
        frm.toggle_display(['items', 'scrap_items'], !frm.doc.is_service_bom);
        
        if (frm.doc.is_service_bom) {
            frm.clear_table('items');
            frm.clear_table('scrap_items');
            frm.refresh_field('items');
            frm.refresh_field('scrap_items');
        }
    },

    with_operations: function(frm) {
        frm.toggle_display('is_service_bom', frm.doc.with_operations);
        if (!frm.doc.with_operations && frm.doc.is_service_bom) {
            frm.set_value('is_service_bom', 0);
        }
    },

   
});