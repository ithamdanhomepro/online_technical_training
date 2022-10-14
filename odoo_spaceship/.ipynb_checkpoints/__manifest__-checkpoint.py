{
    'name': 'Odoo Spaceship',
    
    'summary': """Exploration app to manage Spaceship""",
    
    'description': """
        App Module to manage Spaceship Exploration To Moon
        -Spaceship
    """,
    
    'author': 'Issam',
    
    'website': 'http://www.odoo.com',
    
    'category': 'Exploration',
    'varsion': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/spaceship_security.xml',
        'security/ir.model.access.csv'
    
    ],
    
    'demo': [
       'demo/spaceship_demo.xml', 
    ],
    
    #Add license to remove License Warning
    'license': 'OPL-1'
}