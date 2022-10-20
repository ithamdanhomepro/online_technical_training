
from odoo import models, fields, api
from datetime import date

class Mission(models.Model):
    
    _name = 'academy.mission'
    _description = 'Missions Info'
    
    spaceship_id = fields.Many2one(comodel_name='academy.spaceship',
                                   string='Spaceship',
                                   ondelete='cascade',
                                   required=True)
    
    #now create a related field to spaceship using the id to get the spaceship name (use related attribute)
    name = fields.Char(string='Title', related='spaceship_id.name')
    
    crewmember_ids = fields.Many2many(comodel_name='res.partner', string='Crea Members')
    
    launch_date = fields.Date(string='Launch Date')
    return_date = fields.Date(string='Return Date')
    
    fuel_amount = fields.Float(string='Amount of Fuel')
    engine_count = fields.Integer(string='Number of Engines')
    Safety_features = fields.Text(string='Safety Features')
    
    