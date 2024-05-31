from odoo import fields, models


class ResUsers(models.Model):
    _name = 'res.users'
    _inherit = ['res.users', 'model.signature']
