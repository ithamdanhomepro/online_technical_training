from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Spaceship(models.Model):
    
    _name = 'academy.spaceship'
    _description = 'Spaceship Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    
    ship_length = fields.Float(string='Ship Length')
    ship_width = fields.Float(string='Ship Width')
    ship_height = fields.Float(string='Ship Height')
    
    fuel_type = fields.Text(string='Fuel Type', default='Nitrogen', readonly=True)
    
    ship_type = fields.Selection(string='Ship Type',
                                selection=[('rocket','Rocket'),
                                           ('capsule', 'Capsule')],
                                copy=False)
    
    no_passengers = fields.Integer(string='Number of Passengers', default=1)
    
    active = fields.Boolean(string='Active', default=True)
    