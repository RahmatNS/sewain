from openerp import models,fields,api

class Transaksi(models.Model):
    _name = 'sewain.transaksi'
    user_id = fields.Many2one('res.users', string='Member', index=True,
        track_visibility='onchange', default=lambda self: self.env.user)

    peminjaman_ids = fields.One2many(
        'sewain.peminjaman', 'transaksi_id', string="Peminjaman")
    total_harga = fields.Integer(string="Total Harga")
    warna = fields.Integer()