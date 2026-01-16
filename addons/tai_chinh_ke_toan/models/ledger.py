from odoo import models, fields, api

class Ledger(models.Model):
    _name = "tai_chinh_ke_toan.ledger"
    _description = "Sổ cái kế toán"

    date = fields.Date(string='Date', required=True)
    journal_entry_id = fields.Many2one('tai_chinh_ke_toan.journal_entry', string='Journal Entry')
    account_id = fields.Many2one('account.account', string='Account', required=True)
    debit = fields.Float(string='Debit')
    credit = fields.Float(string='Credit')
    balance = fields.Float(string='Balance', compute='_compute_balance', store=True)

    @api.depends('debit', 'credit', 'account_id', 'date')
    def _compute_balance(self):
        for record in self:
            # Get all ledger entries for the same account, ordered by date
            ledger_entries = self.env['tai_chinh_ke_toan.ledger'].search([
                ('account_id', '=', record.account_id.id)
            ], order='date asc, id asc')
            running_balance = 0.0
            for entry in ledger_entries:
                running_balance += entry.debit - entry.credit
                if entry.id == record.id:
                    record.balance = running_balance
                    break
