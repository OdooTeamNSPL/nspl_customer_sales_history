from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_order_count = fields.Integer(compute='_compute_sale_order_count', string="Sales Orders")

    def _compute_sale_order_count(self):
        for partner in self:
            partner.sale_order_count = self.env['sale.order'].search_count([('partner_id', '=', partner.id)])

    def action_open_customer_sales_history(self):
        self.ensure_one()
        partner = self.commercial_partner_id  # this will cover both company & contact
        return {
            'name': 'Sales History',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'target': 'current',
            'domain': [('partner_id', 'child_of', partner.id)],

        }

