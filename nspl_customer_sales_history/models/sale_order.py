from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_open_customer_sales_history(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Customer Sales History',
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'domain': [('partner_id', '=', self.partner_id.id)],
            'context': {'search_default_group_by_date_order': 1},
        }
