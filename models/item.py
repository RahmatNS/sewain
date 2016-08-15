from openerp import models,fields,api

class Item(models.Model):
    _name = 'sewain.item'

    nama = fields.Char(required=True)
    harga = fields.Integer(string="Harga sewa per jam", required=True)
    deskripsi = fields.Text(string="Keterangan")
    peminjaman_ids = fields.One2many(
        'sewain.peminjaman', 'item_id', string="Peminjaman")
    warna = fields.Integer()