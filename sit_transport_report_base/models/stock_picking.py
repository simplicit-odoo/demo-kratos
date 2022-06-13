# -*- coding: utf-8 -*-

import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _get_default_currency(self):
        return self.env.user.company_id.currency_id

    destination_partner_id = fields.Many2one('res.partner', 'Destination address')
    departure_partner_id = fields.Many2one('res.partner', 'Departure address')
    importer_partner_id = fields.Many2one('res.partner', 'Importer partner')
    exporter_partner_id = fields.Many2one('res.partner', 'Exporter partner')
    destination_note = fields.Text('Destination notes')
    departure_note = fields.Text('Departure notes')
    importer_note = fields.Text('Importer notes')
    exporter_note = fields.Text('Exporter notes')
    origin_depot_id = fields.Many2one('stock.location', 'Departure location', readonly=True)
    dest_depot_id = fields.Many2one('stock.location', 'Destination location', readonly=True)
    customer_id = fields.Many2one('res.partner', 'Customer', related='destination_partner_id.parent_id', readonly=True)
    vendor_id = fields.Many2one('res.users', 'Vendor', related='group_id.sale_id.user_id')
    transport_note = fields.Text("Transport note", help="Add a note that will be displayed on the transport document")
    currency_id = fields.Many2one('res.currency', string='Currency', default=_get_default_currency)
    amount_total = fields.Monetary('Amount total', compute='_compute_amount_total', store=False, currency_field='currency_id')
    show_transport = fields.Boolean("Show transport fields")
    packing_details = fields.Text("Packing details")
    delivery_mode_id = fields.Many2one('delivery.carrier.mode', string="Delivery mode")
    transport_supplier_id = fields.Many2one('res.partner', string="Contact Transporteur", related='carrier_id.transport_supplier_id')
    incoterm_city = fields.Char()

    @api.depends('move_lines.price_subtotal')
    def _compute_amount_total(self):
        for picking in self:
            total = 0.0
            for move in picking.move_lines:
                total += move.price_subtotal
            picking.amount_total = total


    def _get_partner_warehouse(self, location):
        if not location:
            return False
        warehouse = location.warehouse_id
        if not warehouse:
            return False
        return warehouse.partner_id.id

    def action_compute_packing_details(self):
        self.ensure_one()
        packages = self.package_ids
        packaging_types = set([package.packaging_id for package in packages])

        packing_info = []
        for packaging in packaging_types:
            if packaging:
                pp = packages.filtered(lambda p: p.packaging_id == packaging)
                # For now we make the assumption all packages of the same packaging type have the same weight
                packing_info.append(
                    "{package_count} {packaging_name}:\n\t- Dimensions per package: {L}*{l}*{h} {uom_l}\n\t- Net Weight per package: {net_w} {uom_w}\n\t- Gross weight per package: {gross_w} {uom_w}".format(
                        package_count = len(pp),
                        packaging_name = packaging.name,
                        L = packaging.packaging_length,
                        l = packaging.width,
                        h = packaging.height,
                        uom_l = packaging.length_uom_name,
                        net_w = round(pp[0].weight, 2),
                        gross_w = round(pp[0].shipping_weight, 2),
                        uom_w = pp[0].weight_uom_name
                    )
                )
            else:
                packing_info.append(
                    "{package_count} OTHER PACKAGE(S)".format(
                        package_count = len(packages.filtered(lambda p: not p.packaging_id)),
                    )
                )

        packing_info.append("TOTAL Net weight: {net_weight} {uom}\nTOTAL Gross weight: {gross_weight} {uom}".format(
            net_weight = self.weight,
            gross_weight = self.shipping_weight,
            uom = packages.mapped('weight_uom_name')[0]
        ))
        self.packing_details = "\n".join(packing_info)


    @api.model
    def create(self, vals):
        picking = super(StockPicking, self).create(vals)

        if picking.picking_type_code == 'outgoing':
            picking.departure_partner_id = self._get_partner_warehouse(picking.location_id)
            picking.destination_partner_id = picking.partner_id.id
            picking.origin_depot_id = picking.location_id.id
            picking.dest_depot_id = picking.partner_id.property_stock_customer.id
        elif picking.picking_type_code == 'incoming':
            picking.departure_partner_id = picking.partner_id.id
            picking.destination_partner_id = self._get_partner_warehouse(picking.location_dest_id)
            picking.origin_depot_id = picking.departure_partner_id.property_stock_customer.id
            picking.dest_depot_id = picking.location_dest_id.id
        else:
            picking.departure_partner_id = self._get_partner_warehouse(picking.location_id)
            picking.destination_partner_id = self._get_partner_warehouse(picking.location_dest_id)
            picking.origin_depot_id = picking.location_id.id
            picking.dest_depot_id = picking.location_dest_id.id
        
        if picking.destination_partner_id:
            picking.importer_partner_id = picking.destination_partner_id.importer_partner_id
            picking.exporter_partner_id = picking.destination_partner_id.exporter_partner_id
            picking.currency_id = picking.destination_partner_id.currency_id.id

        return picking
