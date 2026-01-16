from odoo import models, fields, api
from odoo.exceptions import ValidationError

class JournalLine(models.Model):
    _name = "tai_chinh_ke_toan.journal_line"
    _description = "Dòng bút toán"

    journal_entry_id = fields.Many2one('tai_chinh_ke_toan.journal_entry', string='Journal Entry')
    account_id = fields.Many2one('account.account', string='Account', required=True)
    debit = fields.Float(string='Debit')
    credit = fields.Float(string='Credit')
    name = fields.Char(string='Description')

class JournalEntry(models.Model):
    _name = "tai_chinh_ke_toan.journal_entry"
    _description = "Bút toán kế toán"

    name = fields.Char(string='Reference')
    date = fields.Date(string='Date', required=True)
    entry_id = fields.Many2one('tai_chinh_ke_toan.entry', string='Depreciation Entry')
    line_ids = fields.One2many('tai_chinh_ke_toan.journal_line', 'journal_entry_id', string='Journal Lines')

    @api.constrains('line_ids')
    def _check_balance(self):
        for record in self:
            total_debit = sum(line.debit for line in record.line_ids)
            total_credit = sum(line.credit for line in record.line_ids)
            if abs(total_debit - total_credit) > 0.01:
                raise ValidationError('Total debit must equal total credit.')
