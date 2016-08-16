from openerp import models,fields,api
class Checkout_wizard(models.TransientModel):
    _name = 'sewain.checkout_wizard'
    def _get_peminjaman_id(self):
        active_ids = self._context.get('active_ids')
        if active_ids:
            return [(6, 0, active_ids)]
        return False

    peminjaman_ids = fields.Many2many('sewain.peminjaman', 'peminjaman_wizard_rel', 'peminjaman_id', 'wizard_id', string="Peminjaman",default=_get_peminjaman_id)
    total_harga = fields.Integer(string="Total Harga", store=True,
        compute='_get_total_harga')
    
    @api.depends('peminjaman_ids.sub_total', 'peminjaman_ids')
    def _get_total_harga(self):
        for r in self:
            for s in r.peminjaman_ids:
                r.total_harga += s.sub_total

    @api.multi
    def checkout(self):
        transaksi_class = self.env['sewain.transaksi']
        print self.peminjaman_ids
        print self.total_harga
        transaksi_class.create({
            'peminjaman_ids': self.peminjaman_ids,
            'total_harga': self.total_harga
        })