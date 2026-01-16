from odoo import models, fields, api

class FinanceEntry(models.Model):
    _name = 'tai_chinh_ke_toan.entry'
    _description = 'Bút toán Thu Chi'
    _order = 'date desc'

    name = fields.Char(
        string='Số chứng từ',
        required=True,
        copy=False,
        default='New'
    )

    date = fields.Date(
        string='Ngày',
        default=fields.Date.context_today,
        required=True
    )

    entry_type = fields.Selection([
        ('thu', 'Thu'),
        ('chi', 'Chi'),
    ], string='Loại', required=True)

    amount = fields.Float(string='Số tiền', required=True)

    description = fields.Text(string='Diễn giải')

    state = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
    ], default='draft', string='Trạng thái')

    @api.model
    def create(self, vals):
        if vals.get('name') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'tai_chinh_ke_toan.entry'
            ) or 'New'
        return super().create(vals)

    def action_confirm(self):
        self.state = 'confirmed'
