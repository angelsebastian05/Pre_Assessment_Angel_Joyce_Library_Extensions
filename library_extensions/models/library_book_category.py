from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Lib Book Category'
    #Name Field
    name = fields.Char(required=True, unique=True)