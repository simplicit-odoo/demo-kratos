# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    origin_country_id = fields.Many2one('res.country', 'Origin country')
    value_for_customs = fields.Monetary('Value for customs', currency_field='currency_id')
