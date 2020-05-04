# -*- coding: utf-8 -*-
{
    'name': "Performa Commercial Invoice report",

    'summary': """
        Performa Commercial Invoice report  
            """,

    'description': """
         Performa Commercial Invoice report
         1-Custom Performa Invoice Format.
         2-Custom Commercial Invoice Format     
            """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'reports/performa_commercial_report.xml',
        'reports/performa_invoice_template.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
