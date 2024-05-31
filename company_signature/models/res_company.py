from odoo import fields, models


class ResCompany(models.Model):
    _name = 'res.company'
    _inherit = ['res.company', 'model.signature']
