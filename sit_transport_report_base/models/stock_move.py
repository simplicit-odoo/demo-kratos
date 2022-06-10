# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    picking_currency_id = fields.Many2one('res.currency', related='picking_id.currency_id')
    price_unit = fields.Monetary("Price unit", currency_field='picking_currency_id')
    price_subtotal = fields.Monetary("Subtotal", currency_field='picking_currency_id', compute='_compute_price_subtotal')
    hs_code = fields.Char(string='HS code', related='product_id.product_tmpl_id.hs_code')
    origin_country_id = fields.Many2one('res.country', string="Origin country")

    @api.depends('price_unit', 'quantity_done')
    def _compute_price_subtotal(self):
        for move in self:
            if move.state in ['cancel', 'done'] :
                move.price_subtotal = move.price_unit * move.quantity_done
            else:
                # Besoin de pouvoir imprimer avec un total != 0 même avant validation
                move.price_subtotal = move.price_unit * move.product_uom_qty

    @api.model
    def create(self, vals):
        move = super(StockMove, self).create(vals)

        if move.product_id and move.product_id.product_tmpl_id:
            if move.product_id.product_tmpl_id.origin_country_id:
                move.origin_country_id = move.product_id.product_tmpl_id.origin_country_id.id
            move.price_unit = move.product_id.product_tmpl_id.value_for_customs

        return move
    

