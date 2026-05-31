import base64

from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged('post_install', '-at_install')
class TestUsersSignature(TransactionCase):
    def test_user_signature_is_stored(self):
        signature = base64.b64encode(b'user-signature')
        user = self.env['res.users'].create({
            'name': 'Signature User',
            'login': 'signature_user',
            'email': 'signature_user@example.com',
            'digitized_signature': signature,
        })

        self.assertEqual(user.digitized_signature, signature)
