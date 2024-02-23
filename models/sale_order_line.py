from odoo import models, fields, api


class SaleOrderLines(models.Model):
    _inherit = "sale.order.line"
    _description = "task"

    discount_amount = fields.Float(
        string='Discount Amount'
    )
    # discount = fields.Float(
    #     string="Discount (%)",
    #     compute='_compute_discount',
    #     digits='Discount',
    #     related='order_id.partner_id.special_discount',
    #     store=True, readonly=False, precompute=True)

    @api.onchange('price_subtotal')
    def _onchange_product_template_id(self):
        if not self.product_template_id.no_any_discount:
            if self.order_id.partner_id.offer_discount:
                self.discount = self.order_id.partner_id.special_discount
                self.discount_amount = ((self.price_unit * self.product_uom_qty) * self.discount) / 100
                # print(self._origin,'==================================[][[]]]]]][][[][[]]][[]][][[]][[][]]][[[][]]]]][][][][][][][][]]][][][[[][')
        else:
            self.discount = 0
    # @api.depends('price_unit', 'product_uom_qty', 'discount')
    # def _compute_discount(self):
    #     for rec in self:
    #         rec.discount_amount = ((rec.price_unit * rec.product_uom_qty) * rec
    #                                .discount) / 100


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "task"

    discount_amount_total = fields.Float('Discount Total')

    @api.depends('discount_amount')
    def _discount_amount_total(self):
        self.discount_amount_total = sum(list(rec.discount_amount for rec in self.order_line))
