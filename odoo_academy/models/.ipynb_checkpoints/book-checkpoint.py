# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    
    _name = 'academy.book'
    _description = 'Book Info'
    
    name =fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')