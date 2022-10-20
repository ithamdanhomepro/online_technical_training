# -*- coding: utf-8 -*-
    
{
    'name': 'Odoo Academy',
     
    'summary': """Academy app to manage Training""",
     
    'description': """
         Academy Module to manage Training:
         - Courses
         - Sessions
         - Attendees
    """,
     
    'author': 'Odoo',
    
     'website': 'http://www.odoo.dom',
     
     'category': 'Training',
     'version' : '0.2',
     
     'depends': ['sale_management'],
     
     'data': [
        'security/academy_security.xml',
         'security/ir.model.access.csv',
         'views/academy_menuitems.xml',
         'views/course_views.xml',
         'views/session_views.xml',
         'views/sale_views_inherit.xml',
         'views/product_views_inherit.xml',
         'wizards/sale_wizard_view.xml',
         'reports/session_report_templates.xml',
     ],
     
     'demo': [
        'demo/academy_demo.xml',
     ],
    #Add license to remove License Warning
    'license': 'OPL-1'
}