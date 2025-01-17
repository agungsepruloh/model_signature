# -*- coding: utf-8 -*-
{
    'name': "Employee Signature",

    'summary': """
        This module helps users to manage signature for the employee.
    """,

    'description': """
        This module helps users to manage signature for the employee.
    """,

    'author': "Agung Sepruloh",
    'website': "https://github.com/agungsepruloh",
    'maintainers': ['agungsepruloh'],
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources/Employees',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'base_model_signature'],

    # always loaded
    'data': [
        'views/hr_employee_views.xml',
    ],

    # only loaded in demonstration mode
    'demo': [],

    'images': ['static/description/banner.gif'],
    'application': True,
}

