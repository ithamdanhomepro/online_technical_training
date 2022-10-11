# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    
    _name = 'academy.task'
    _description = 'Task Info'
    
    name =fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')