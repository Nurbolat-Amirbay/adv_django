from django.test import TestCase
from .models import Order, Transaction

class OrderModelTest(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            # Add necessary fields for Order model
        )

    def test_order_creation(self):
        self.assertIsInstance(self.order, Order)
        self.assertEqual(str(self.order), 'Expected string representation')

class TransactionModelTest(TestCase):
    def setUp(self):
        self.transaction = Transaction.objects.create(
            # Add necessary fields for Transaction model
        )

    def test_transaction_creation(self):
        self.assertIsInstance(self.transaction, Transaction)
        self.assertEqual(str(self.transaction), 'Expected string representation')