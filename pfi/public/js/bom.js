frappe.ui.form.on('BOM', {
    refresh: function(frm) {
        // Toggle Items table visibility/mandatory based on "_is_service"
        frm.toggle_reqd('items', !frm.doc.is_service_bom);
        frm.toggle_display('items', !frm.doc.is_service_bom);
        
        // Clear Items table if "Is Service" is checked
        if (frm.doc.is_service_bom) {
            frm.clear_table('items');
            frm.refresh_field('items');
        }
    },
    is_service_bom: function(frm) {
        // Update on checkbox change
        frm.toggle_reqd('items', !frm.doc.is_service_bom);
        frm.toggle_display('items', !frm.doc.is_service_bom);
        
        if (frm.doc.is_service_bom) {
            frm.clear_table('items');
            frm.refresh_field('items');
        }
    }
});