from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged('post_install', '-at_install')
class TestModelSignature(TransactionCase):
    def test_signature_field_exists_on_abstract_model(self):
        field = self.env['model.signature']._fields['digitized_signature']

        self.assertEqual(field.type, 'binary')
        self.assertEqual(field.string, 'Signature')
