# -*- coding: utf-8 -*-
{
    'name': "SIT - Traxens transport report",

    'summary': """
        Based on 'SIT - Transport report base', this module allows to print a transport document from transfers.""",

    'description': """
        Based on 'SIT - Transport report base', this module allows to print a transport document from transfers.
    """,

    'author': "SimplicIT",
    'website': "https://www.simplicit.pro",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'sit_transport_report_base',
        'sit_product_lithium',
        'sit_stock_incoterm',
    ],

    # always loaded
    'data': [
        'views/stock_picking_views.xml',
        'views/stock_move_views.xml',
        'views/report_ship_pi.xml',
        'views/report_ship_pl.xml',
        'report/picking_report.xml',
    ],
}
