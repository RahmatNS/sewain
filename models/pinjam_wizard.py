from openerp import models,fields,api
class Pinjam_wizard(models.TransientModel):
    _name = 'sewain.pinjam_wizard'

    def _get_item_id(self):
        active_ids = self._context.get('active_ids')[0]
        if active_ids:
            return active_ids
        return False
                

    item_id = fields.Many2one('sewain.item',string="Item",required=True,default=_get_item_id)
    item_name = fields.Char(string="Nama", related="item_id.nama", readonly=True)
    kuantitas = fields.Integer(string="Jumlah item", required=True,default=1)
    waktu_mulai = fields.Date(default=fields.Date.today)
    durasi = fields.Float(digits=(6, 2), help="Duration in days",default=1)

    @api.multi
    def sewa_item(self):
        peminjaman_class = self.env['sewain.peminjaman']
        peminjaman_id = peminjaman_class.create({
            'item_id': self.item_id.id,
            'item_name': self.item_name,
            'kuantitas': self.kuantitas,
            'waktu_mulai': self.waktu_mulai,
            'durasi': self.durasi
        })
        transaksi_class = self.env['sewain.transaksi']
        transaksi_class.create({
            'peminjaman_ids': [(4, peminjaman_id.id)]
            })