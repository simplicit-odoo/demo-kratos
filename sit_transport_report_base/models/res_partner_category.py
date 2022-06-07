# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnerCategory(models.Model):
    _inherit = 'res.partner.category'

    is_contact_displayed = fields.Boolean("Display contact on transport document", help="Display or not the delivery contact on SHIP_PI and SHIP_PL")
