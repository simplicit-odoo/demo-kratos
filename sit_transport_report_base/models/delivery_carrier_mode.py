# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DeliveryCarrierMode(models.Model):
    _name = 'delivery.carrier.mode'
    _description = "Delivery Carrier Mode"

    name = fields.Char('Name', required=True)
