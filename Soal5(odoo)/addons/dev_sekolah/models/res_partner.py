# models/res_partner.py
from odoo import models, fields

class ResPartnerGuru(models.Model):
    _inherit = 'res.partner'

    is_guru = fields.Boolean(string='Guru', default=False)
    bidang_studi = fields.Selection([
        ('matematika', 'Matematika'),
        ('ipa', 'IPA'),
        ('ips', 'IPS'),
        ('bahasa_indonesia', 'Bahasa Indonesia'),
        ('bahasa_inggris', 'Bahasa Inggris'),
        ('lainnya', 'Lainnya'),
    ], string='Bidang Studi')