# -*- coding: utf-8 -*-
{
    'name': "Company Signature",

    'summary': """
        This module helps users to manage signature for the company.
    """,

    'description': """
        This module helps users to manage signature for the company.
    """,

    'author': "Agung Sepruloh",
    'website': "https://github.com/agungsepruloh",
    'maintainers': ['agungsepruloh'],
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_model_signature'],

    # always loaded
    'data': [
        'views/res_company_views.xml',
    ],

    # only loaded in demonstration mode
    'demo': [],

    'images': ['static/description/banner.gif'],
    'application': True,
}

