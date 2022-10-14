from odoo import models, fields, api

class Spaceship(models.Model):
    
    _name = 'academy.spaceship'
    _description = 'Spaceship Info'
    
    name = fields.Char(string='Title', required=True)
    deswription = fields.Text(string='Description')
    