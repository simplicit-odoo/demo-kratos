# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    lithium_qty_ids = fields.One2many('product.lithium.quantity','product_template_id', 'Lithium qty')
    total_li_qty = fields.Float('Total Li qty', store=True, compute='_compute_total_li_qty')
    total_battery_weight = fields.Float('Total net weight', store=True, compute='_compute_total_battery_weight',
        help="This weight will be used to compute total qty on picking and to generate lithium document")
    hazardous_classification = fields.Text('Hazardous classification')


    @api.depends('lithium_qty_ids.lithium_battery_id.li_qty') #TODO verifier
    def _compute_total_li_qty(self):
        for product in self:
            total = 0.0
            for line in product.lithium_qty_ids:
                total += line.qty * line.lithium_battery_id.li_qty
            product.total_li_qty = total


    @api.depends('lithium_qty_ids.lithium_battery_id.battery_weight') #TODO verifier
    def _compute_total_battery_weight(self):
        for product in self:
            total = 0.0
            for line in product.lithium_qty_ids:
                total += line.qty * line.lithium_battery_id.battery_weight
            product.total_battery_weight = total
