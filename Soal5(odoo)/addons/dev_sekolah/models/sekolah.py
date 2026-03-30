from odoo import models, fields, api

class Sekolah(models.Model):
    _name = 'dev.sekolah'
    _description = 'Sekolah'

    name = fields.Char(required=True)
    alamat = fields.Text()

    kelas_ids = fields.One2many(
        'dev.sekolah.kelas',
        'sekolah_id',
        string='Daftar Kelas'
    )

    total_kelas = fields.Integer(
        string='Total Kelas',
        compute='_compute_total_kelas',
        store=True,
        readonly=True
    )

    @api.depends('kelas_ids')
    def _compute_total_kelas(self):
        for rec in self:
            rec.total_kelas = len(rec.kelas_ids)