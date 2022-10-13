# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Course Info'
    
    name =fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Level',
                            selection=[('beginner', 'Beginner'),
                                        ('intermediate', 'Intermediate'),
                                        ('advanced', 'Advanced')],
                            copy=False)
        
    active = fields.Boolean(string='Active', default=True)
    
    base_price = fields.Float(string='Base Price', default=0.00)
    
    additional_fee = fields.Float(string='Additional Fee', default=10.00)
    
    total_price = fields.Float(string='Total Price', readonly=True)
    
    #add methods
    @api.onchange('base_price', 'addtional_fee')
    def _onchange_total_price(self):
        
        if self.base_price < 0.00:
            raise UserError('Base Price can not be set as Negative.')
            
        self.total_price = self.base_price + self.additional_fee
        
    @api.constraints('attional_fee')
    def _check_additional_fee(self):
        for record in self:
            if record.addional_fee < 10.00:
                raise VaalidationError('Addtional Fees cannot be less than 10.00: %s' % record.additional_fee)
    