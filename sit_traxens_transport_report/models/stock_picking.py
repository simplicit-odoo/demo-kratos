# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    ship_pi_reference = fields.Char('Invoice N°')
    ship_pl_reference = fields.Char('BL N°')
    ship_pi_note = fields.Text()
    ship_pl_note = fields.Text()

    def _set_document_reference(self):
        for record in self:
            if record.picking_type_code != 'incoming':
                try:
                    record.ship_pi_reference = "FAPRO" + record.create_date.strftime('%y%m%d') + record.name.split('/')[-1]
                    record.ship_pl_reference = "BLPRO" + record.create_date.strftime('%y%m%d') + record.name.split('/')[-1]
                except:
                    record.ship_pi_reference = False
                    record.ship_pl_reference = False
    @api.model
    def create(self, vals):
        picking = super(StockPicking, self).create(vals)
        if picking.picking_type_code != 'incoming':
            picking._set_document_reference()
        return picking

    def action_view_serial_number_moves(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("stock.stock_move_line_action")
        action['domain'] = [('picking_id', '=', self.id), ('lot_id', '!=', False)]
        action['context'] = {'search_default_done': 0, 'search_default_groupby_product_id': 0, 'create': 0}
        return action
