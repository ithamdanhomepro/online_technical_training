{
    'name': 'Space Mission',
    'version': '0.6',
    'summary': 'Odoo Application to control its Space Mission',
    'description': """
        Space Mission Application to Manage Space Control:
            -
            -
            -
        """,
    'license': 'OPL-1',
    'author': 'fsrs-odoo',
    'website': 'www.odoo.com',
    'category': 'Tech Training',
    
    'depends': ['project'],
    'data': [
        'security/spaceship_security.xml',
        'security/ir.model.access.csv',
        'views/space_mission_menuitems.xml',
        'views/spaceship_view.xml',
        'views/mission_view.xml',
        'views/project_views_inherit.xml',
        'wizard/project_wizard.xml',
    ],
    'demo': ['demo/spaceship_demo.xml',],
    
    'assets': {},
    
    'installable': True,
    'application': True,
    'auto_install': False,
    
}
