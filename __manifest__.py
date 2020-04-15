# -*- coding: utf-8 -*-
{
    'name': "pdf_agregacion",

    'summary': """ Agregacion de un campo al modelo de los empleados
        """,

    'description': """
        Este modulo nos permitira poder visualizar un campo nuevo donde se almacenara el CV del empleado
    """,

    'author': "Licorera del sur",
    'website': "http://www.licoreradelsur.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Generic Modules/Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],
    'images': ['static/description/logo licorera .png'],

    # always loaded
    'data': [
        # 'security/ir.mrodel.access.csv',
        'views/Employee_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}