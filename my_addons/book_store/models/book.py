from odoo.odoo import models, fields


class Book(models.Model):
    _name = "bookstore.book"
    _description = "Book Store"

    image = fields.Image(string='cover', attachment=True)
    id = fields.Char(string='book_id')
    name = fields.Char(string="name", required=True)
    catalog_id = fields.Many2one(comodel_name='bookstore.catalog', string='category', required=True)
    author = fields.Char(string='author', required=True)
    price = fields.Float(string='price', required=True)
    pages = fields.Integer(string='pages')
    count = fields.Integer(string='qty')
    published_date = fields.Date(string='publish date')
    description = fields.Text(string="description")


class Catalog(models.Model):
    _name = "bookstore.catalog"
    _description = "Catalog"

    name = fields.Char(string='catalog', required=True)
    book_ids = fields.One2many(comodel_name='bookstore.book', inverse_name='catalog_id', string='Book')
