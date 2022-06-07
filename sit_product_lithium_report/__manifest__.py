# -*- coding: utf-8 -*-
{
    'name': "SIT - Product lithium report",

    'summary': """
        Based on module 'SIT - Product lithium', this module allows to print Lithium Labels documents from a transfer.""",

    'description': """
        Based on module 'SIT - Product lithium', this module allows to print Lithium Labels documents from a transfer, in order 
        to display how much lithium is contained in each package moved by the transfer.
        Prints a PDF as below:
          - one page for each package (stock_picking.package_ids)
          - on each page is displayed:
                - the origin and destination address
                - the total lithium quantity in the package
    """,

    'author': "SimplicIT",
    'website': "https://www.simplicit.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sit_product_lithium', 'sit_transport_report_base'],

    # always loaded
    'data': [
        'views/report_lithium_per_package.xml',
        'report/picking_report.xml',
    ],
}
