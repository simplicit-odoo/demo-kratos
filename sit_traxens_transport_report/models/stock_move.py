# -*- coding: utf-8 -*-

from odoo import models, fields


class StockMove(models.Model):
    _inherit = 'stock.move'

    ship_pi_reference = fields.Char('Invoice N°', related='picking_id.ship_pi_reference', store=True, readonly=True)
    ship_pl_reference = fields.Char('BL N°', related='picking_id.ship_pl_reference', store=True, readonly=True)

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    ship_pi_reference = fields.Char('Invoice N°', related='picking_id.ship_pi_reference', store=True, readonly=True)
    ship_pl_reference = fields.Char('BL N°', related='picking_id.ship_pl_reference', store=True, readonly=True)
