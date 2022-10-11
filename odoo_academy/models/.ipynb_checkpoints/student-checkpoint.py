# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(model.Model):
    
    _name: 'academy.student'
    _order = "id desc"