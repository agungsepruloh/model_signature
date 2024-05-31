from odoo import fields, models


class ModelSignature(models.AbstractModel):
    _name = 'model.signature'
    _description = 'Model Signature'

    digitized_signature = fields.Binary('Signature')
