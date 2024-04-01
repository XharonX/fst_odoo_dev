from odoo import models, fields


class Book(models.Model):
    _name = "book.store"
    _description = "Book Store"

    id = fields.Char(string='book_id')
    name = fields.Char(string="name")
    author = fields.Char(string='author')
    price = fields.Float(string='price')
    pages = fields.Integer(string='pages')
    count = fields.Integer(string='qty')
    published_date = fields.Date(string='publish date')
    description = fields.Text(string="description")


