# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    
    _name = 'academy.spaceship'
    _description = 'Spaceship Info'
    
    spaceship_length = fields.Integer('Spaceship Length')
    spaceship_width = fields.Integer('Spaceship Width')
    spaceship_height = fields.Integer('Spaceship Height')
    
    fuel_type = fields.Char(string='Fuel Type')
    ship_type = fields.Selection(string='Ship Type',
                            selection=[('small', 'Small'),
                                        ('medium', 'Medium'),
                                        ('huge', 'Huge')])
    
    no_passengers = fields.Integer(string='No of Passengers', default=100)
    ship_status = fields.Boolean(string='Active', default=True, tracking=True)
    
    