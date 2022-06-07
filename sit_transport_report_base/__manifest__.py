# -*- coding: utf-8 -*-
{
    'name': "SIT - Transport report base",

    'summary': """This module adds information (new fields on products, transfers, stock moves) necessary to generate transport documents from transfers.""",

    'description': """
        This module adds information necessary to generate transport documents from transfers:
            - contacts on transfers (departure and destination address, importer, exporter)
            - information on products used for customs: country of origin, price,...
            - packaging information
            - various text fields to add manual notes
            - delivery mode on carriers
            - ...
    """,

    'author': "SimplicIT",
    'website': "https://www.simplicit.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'delivery', 'sit_stock_incoterm'],

    # always loaded
    'data': [
        'views/stock_picking_views.xml',
        'views/res_partner_views.xml',
        'views/res_partner_category_views.xml',
        'views/product_template_views.xml',
        'views/delivery_carrier_views.xml',
        'views/delivery_mode_views.xml',
        'security/ir.model.access.csv',
    ],
}
