
from odoo import models, fields, api

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session Info'
    
    #TODO add relational field in session that relates to course
    #if course_id in course model is delted, then session is deleted as well
    #required True means every session must have an associated course
    course_id = fields.Many2one(comodel_name='academy.course',
                                string='Course',
                                ondelete='cascade',
                                required=True)
    
    #now create a related field to course using the id to get the course name (use related attribute)
    name = fields.Char(string='Title', related='course_id.name')
    
    #add an instructor (Many2one) and Students (Manytomany) to session.
    #Odoo has res.Partner in the base model that Odoo automatically installs
    instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor')
    
    student_ids = fields.Many2many(comodel_name='res.partner', string='Students')
    
    