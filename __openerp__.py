# -*- coding: utf-8 -*-
{
    'name': "Sewain App",

    'summary': """Easy app to rent item""",

    'description': """
        This module will help you to:
            - Rent item online
    """,

    'author': "Rahmat NS",
    'website': "http://www.rahmatnasution.xyz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'security/security.xml',
        # 'templates.xml',
        'view/sewain.xml',
        'view/peminjaman.xml',
        'view/transaksi.xml',
        'wizard/pinjam_wizard.xml',
        'wizard/checkout_wizard.xml',
        'report/reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
# rahmath322ue
# maksimal trip 30,000
