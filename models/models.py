from openerp import models,fields,api
from datetime import timedelta

class Item(models.Model):
    _name = 'sewain.item'

    nama = fields.Char(required=True)
    harga = fields.Integer(string="Harga sewa per jam", required=True)
    jumlah = fields.Integer(string="Jumlah item tersedia", required=True,default=1)
    deskripsi = fields.Text(string="Keterangan")
    peminjaman_ids = fields.One2many(
        'sewain.peminjaman', 'item_id', string="Peminjaman")
    warna = fields.Integer()

class Peminjaman(models.Model):
    _name = 'sewain.peminjaman'

    item_id = fields.Many2one('sewain.item',
        ondelete='set null', string="Item", index=True)
    kuantitas = fields.Integer(string="Jumlah item", required=True,default=1)
    waktu_mulai = fields.Date(default=fields.Date.today)
    durasi = fields.Float(digits=(6, 2), help="Duration in days")
    waktu_selesai = fields.Date(string="Waktu Selesai", store=True,
        compute='_get_waktu_selesai', inverse='_set_waktu_selesai')
    sub_total = fields.Integer(string="Sub Total", store=True,
        compute='_get_sub_total', inverse='_set_sub_total')
    warna = fields.Integer()
    transaksi_id = fields.Many2one('sewain.transaksi',
        ondelete='set null', string="Member", index=True)

    @api.depends('waktu_mulai', 'durasi')
    def _get_waktu_selesai(self):
        for r in self:
            if not (r.waktu_selesai and r.durasi):
                r.waktu_selesai = r.waktu_mulai
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            start = fields.Datetime.from_string(r.waktu_mulai)
            duration = timedelta(days=r.durasi, seconds=-1)
            r.waktu_selesai = start + duration
    @api.depends('item_id.harga', 'durasi','item_id')
    def _get_sub_total(self):
        for r in self:
            r.sub_total = r.item_id.harga * r.durasi

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