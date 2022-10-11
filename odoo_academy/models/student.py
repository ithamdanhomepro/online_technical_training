# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    
    _name = 'academy.student'
    _description = 'Student Info'

    name =fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')