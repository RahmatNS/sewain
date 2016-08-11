from openerp import models,fields,api

class Item(models.Model):
    _name = 'sewain.item'

    nama = fields.Char(required=True)
    harga = fields.Integer(string="Harga sekali sewa", required=True)
    jumlah = fields.Integer(string="Jumlah item", required=True,default=1)
    deskripsi = fields.Text(string="Keterangan")
    warna = fields.Integer()