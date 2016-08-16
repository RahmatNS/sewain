from openerp import models,fields,api
from datetime import timedelta

class Peminjaman(models.Model):
    _name = 'sewain.peminjaman'

    item_id = fields.Many2one('sewain.item',
        ondelete='set null', string="Kode Item", index=True)
    item_name = fields.Char(string="Nama",store=False, compute='_get_item_name')
    kuantitas = fields.Integer(string="Jumlah item", required=True,default=1)
    waktu_mulai = fields.Date(default=fields.Date.today)
    durasi = fields.Float(digits=(6, 2), help="Duration in days")
    waktu_selesai = fields.Date(string="Waktu Selesai", store=True,
        compute='_get_waktu_selesai', inverse='_set_waktu_selesai')
    harga_dasar = fields.Integer(string="Harga Dasar",store=True,compute="_get_harga_dasar")
    sub_total = fields.Integer(string="Sub Total", store=True,
        compute='_get_sub_total', inverse='_set_sub_total')
    warna = fields.Integer()
    transaksi_id = fields.Many2one('sewain.transaksi',
        ondelete='set null', string="Member", index=True)

    state = fields.Selection([
        ('draft', "Draft"),
        ('confirmed', "Confirmed"),
        ('done', "Done"),
    ], default='draft')

    @api.depends('item_id.nama','item_id')
    def _get_item_name(self):
        for r in self:
            r.item_name = r.item_id.nama

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_confirm(self):
        self.state = 'confirmed'

    @api.multi
    def action_done(self):
        self.state = 'done'
        
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

    @api.depends('item_id.harga','item_id')
    def _get_harga_dasar(self):
        for r in self:
            r.harga_dasar = r.item_id.harga

    @api.depends('harga_dasar', 'durasi','kuantitas')
    def _get_sub_total(self):
        for r in self:
            r.sub_total = r.harga_dasar * r.durasi * r.kuantitas


    @api.multi
    def confirm(self, context):
        for r in self:
            print "+++++++++++++++++++++++++="
            r.state = "draft"
            print r.state