# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_incoterm_id = fields.Many2one("account.incoterms", string="Incoterm")
