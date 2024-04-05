from odoo.odoo import fields, models, api


class TrainingCourse(models.Model):
    _name = 'training_center.course'
    _description = 'training_center.course'

    name = fields.Char(string='course title')
    level = fields.Selection(
        [
            ('basic', "Basic"),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('expert', "Expert"),
        ])
    active = fields.Binary(default=True)
    instructor_id = fields.Many2many(comodel_name='training_center.instructor', string='Instructor', )
    start_date = fields.Date()
    price = fields.Monetary(string='price')
    currency_id = fields.One2many('res.currency', string='Currency')
    manager_remark = fields.Text()
    status = fields.Selection([
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ])
    training_center_id = fields.Many2one('training_center.training_center', )


class TrainingInstructor(models.Model):
    _inherit = 'res.partner'
    course_ids = fields.One2many('training_center.course', 'instructor_id', 'courses')


class TrainingCenter(models.Model):
    _name = 'training_center.training_center'
    _description = 'Training Center -> Training Center'

    name = fields.Char('Training center name: ')
    course_ids = fields.One2many('training_center.course', 'training_center_id', 'course')