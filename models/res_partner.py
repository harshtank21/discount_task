from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    offer_discount = fields.Boolean(
        string="Offer Discount")
    special_discount = fields.Float(
        string="Special Discount (%)")

    def action_special_discount(self):
        print('hello')



