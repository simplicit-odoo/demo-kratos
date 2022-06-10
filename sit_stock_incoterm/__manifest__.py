# -*- coding: utf-8 -*-
{
    'name': "SIT - Stock Incoterm",

    'summary': """
        Adds incoterm information on transfers.""",

    'description': """
        Adds incoterm information on transfers.
        Installs the OCA module sale_partner_incoterm.
        In the context of a sale, the transfer will retrieve the incoterm information from the sale order. 
    """,

    'author': "SimplicIT",
    'website': "https://www.simplicit.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_partner_incoterm', 'stock'],

    # always loaded
    'data': [
        'views/stock_picking_views.xml',
    ],
}
