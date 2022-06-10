# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductLithiumBattery(models.Model):
    _name = 'product.lithium.battery'
    _description = 'Lithium battery product'

    name = fields.Char("Battery model")
    brand = fields.Char("Brand")
    type = fields.Char("Type")
    li_qty = fields.Float("Lithium qty")
    battery_weight = fields.Float("Battery net weight")
    note = fields.Text()


