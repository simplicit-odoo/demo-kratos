# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductLithiumQuantity(models.Model):
    _name = 'product.lithium.quantity'
    _description = 'Product lithium Quantity'

    product_template_id = fields.Many2one('product.template', 'Product')
    lithium_battery_id = fields.Many2one('product.lithium.battery', 'Lithium battery')
    qty = fields.Integer('Quantity')


