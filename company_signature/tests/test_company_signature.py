import base64

from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged('post_install', '-at_install')
class TestCompanySignature(TransactionCase):
    def test_company_signature_is_stored(self):
        signature = base64.b64encode(b'company-signature')

        self.env.company.digitized_signature = signature

        self.assertEqual(self.env.company.digitized_signature, signature)
