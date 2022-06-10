# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    transport_supplier_id = fields.Many2one('res.partner', string="Contact Transporteur")
