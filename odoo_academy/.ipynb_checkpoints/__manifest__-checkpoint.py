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
     
     'depends': ['base'],
     
     'data': [
        'security/academy_security.xml',
         'security/ir.model.access.csv',
         'views/academy_menuitems.xml'
     ],
     
     'demo': [
        'demo/academy_demo.xml',
     ],
    #Add license to remove License Warning
    'license': 'OPL-1'
}