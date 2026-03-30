from odoo import models, fields, api

class Kelas(models.Model):
    _name = 'dev.sekolah.kelas'
    _description = 'Kelas'

    name = fields.Char(required=True)
    sekolah_id = fields.Many2one('dev.sekolah', string='Sekolah', ondelete='cascade')
    
    wali_kelas_id = fields.Many2one(
        'res.partner',
        string='Wali Kelas',
        domain=[('is_guru', '=', True)],
    )

    total_kelas_sekolah = fields.Integer(
        related='sekolah_id.total_kelas',
        store=True,
        string='Total Kelas Sekolah'
    )

    kelas_summary = fields.Char(compute="_compute_summary")

    @api.depends('name', 'sekolah_id', 'sekolah_id.total_kelas')
    def _compute_summary(self):
        for rec in self:
            sekolah_name = rec.sekolah_id.name if rec.sekolah_id else '-'
            total_kelas = rec.sekolah_id.total_kelas if rec.sekolah_id else 0
            rec.kelas_summary = f"{rec.name} | Sekolah: {sekolah_name} | Total Kelas: {total_kelas}"