# -*- coding: utf-8 -*-
{
    'name': "Users Signature",

    'summary': """
        This module helps users to manage signature for the user.
    """,

    'description': """
        This module helps users to manage signature for the user.
    """,

    'author': "Agung Sepruloh",
    'website': "https://github.com/agungsepruloh",
    'maintainers': ['agungsepruloh'],
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_model_signature'],

    # always loaded
    'data': [
        'views/res_users_views.xml',
    ],

    # only loaded in demonstration mode
    'demo': [],

    'images': ['static/description/banner.gif'],
    'application': True,
}

