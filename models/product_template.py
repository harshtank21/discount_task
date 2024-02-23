from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    no_any_discount = fields.Boolean(
        string='No any discount'
    )