# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockQuantPackage(models.Model):
    _inherit = 'stock.quant.package'

    total_lithium_weight = fields.Float('Total lithium weight', compute='_compute_total_lithium_weight')

    def _compute_total_lithium_weight(self): #TODO test
        for package in self:
            total = 0.0
            for quant in package.quant_ids:
                # At the package level, total must be displayed in kg
                total += (quant.product_tmpl_id.total_battery_weight * quant.quantity) / 1000
            package.total_lithium_weight = total