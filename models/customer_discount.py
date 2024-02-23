from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CustomerDiscount(models.TransientModel):
    _name = "customer.discount"

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer'
    )
    amount = fields.Float(
        string='Amount (%)'
    )

    @api.constrains('partner_id')
    def _check_record(self):
        partner_record = self.search([('partner_id.id', '=', self.partner_id.id), ('id', '!=', self.id)])
        if partner_record:
            raise ValidationError('Already exists this customer')
