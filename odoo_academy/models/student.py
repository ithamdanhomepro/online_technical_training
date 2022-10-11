# _*_ coding: utf-8 _*_

from odoo import models, fields, api

class Student(model.Model):
    
    _name: 'academy.student'
    _order = "id desc"