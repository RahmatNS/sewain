from openerp import models,fields,api

class Transaksi(models.Model):
    _name = 'sewain.transaksi'
    user_id = fields.Many2one('res.users',
        ondelete='set null', string="Member", index=True)

    peminjaman_ids = fields.One2many(
        'sewain.peminjaman', 'transaksi_id', string="Peminjaman")
    total_harga = fields.Integer(string="Total Harga", store=True,
        compute='_get_total_harga', inverse='_set_total_harga')
    
    @api.depends('peminjaman_ids.sub_total', 'peminjaman_ids')
    def _get_total_harga(self):
        for r in self:
            r.total_harga += r.peminjaman_ids.sub_total

    warna = fields.Integer()