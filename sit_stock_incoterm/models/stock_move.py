# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _assign_picking_post_process(self, new=False):
        '''
        On est obligé d'utiliser cette méthode pour initialiser le picking (au lieu de le faire
        dans le create du picking) car le champ picking.group_id est un champ related: il n'apparaît 
        pas dans les vals de la méthode create du picking
        '''
        super(StockMove, self)._assign_picking_post_process(new=new)
        if new:
            for picking in self.mapped('picking_id'):
                if picking.group_id and picking.group_id.sale_id and picking.group_id.sale_id.incoterm:
                    picking.sale_incoterm_id = picking.group_id.sale_id.incoterm.id
