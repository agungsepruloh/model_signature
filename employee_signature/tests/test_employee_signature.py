import base64

from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged('post_install', '-at_install')
class TestEmployeeSignature(TransactionCase):
    def test_employee_signature_is_stored(self):
        signature = base64.b64encode(b'employee-signature')
        employee = self.env['hr.employee'].create({
            'name': 'Signature Employee',
            'digitized_signature': signature,
        })

        self.assertEqual(employee.digitized_signature, signature)
