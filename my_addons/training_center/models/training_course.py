from odoo import fields, models


class Course(models.Model):
    _name = 'training.course'
    _description = 'Training Course'

    name = fields.Char("Course Title", required=True)
    desc = fields.Html("Description")
