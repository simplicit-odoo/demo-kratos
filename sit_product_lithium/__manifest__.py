# -*- coding: utf-8 -*-
{
    'name': "SIT - Product lithium",

    'summary': """
        This module allows to add lithium information in products.""",

    'description': """
        This module allows to add lithium information in products:
            - create and configure models of lithium batteries
            - add batteries to a product
            - computes the total quantity of lithium contained in the product
            - computes the total quantity of lithium contained in packages
    """,

    'author': "SimplicIT",
    'website': "https://www.simplicit.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_lithium_battery_views.xml',
        'views/product_template_views.xml',
        'views/stock_quant_package_views.xml',
    ],
}
