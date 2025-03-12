// bom.js
frappe.ui.form.on('BOM', {
    refresh: function(frm) {
        frm.toggle_reqd('items', !frm.doc.is_service_bom);
        frm.toggle_display(['items', 'operations'], !frm.doc.is_service_bom);
    },
    is_service_bom: function(frm) {
        frm.toggle_reqd('items', !frm.doc.is_service_bom);
        frm.toggle_display(['items', 'operations'], !frm.doc.is_service_bom);
        
        // Clear items table if "Is Service" is checked
        if (frm.doc.is_service_bom) {
            frm.clear_table('items');
            frm.refresh_field('items');
        }
    }
});