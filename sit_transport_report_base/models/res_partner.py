# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    exporter_partner_id = fields.Many2one('res.partner', 'Exporter partner', domain="[('id','child_of',parent_id)]")
    importer_partner_id = fields.Many2one('res.partner', 'Importer partner', domain="[('id','child_of',parent_id)]")
    is_displayed_on_report = fields.Boolean(compute='_compute_is_displayed_on_report', store=True)

    @api.depends('category_id', 'category_id.is_contact_displayed')
    def _compute_is_displayed_on_report(self):
        for partner in self:
            res = False
            for tag in partner.category_id:
                if tag.is_contact_displayed:
                    res = True
                    break
            partner.is_displayed_on_report = res
