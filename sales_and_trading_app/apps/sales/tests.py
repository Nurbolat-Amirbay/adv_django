from django.test import TestCase
from .models import SalesOrder, Invoice

class SalesOrderModelTest(TestCase):
    def setUp(self):
        self.order = SalesOrder.objects.create(
            customer_name="John Doe",
            total_amount=100.00,
            status="Pending"
        )

    def test_sales_order_creation(self):
        self.assertEqual(self.order.customer_name, "John Doe")
        self.assertEqual(self.order.total_amount, 100.00)
        self.assertEqual(self.order.status, "Pending")

class InvoiceModelTest(TestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(
            order=self.order,
            invoice_number="INV123456",
            amount_due=100.00
        )

    def test_invoice_creation(self):
        self.assertEqual(self.invoice.invoice_number, "INV123456")
        self.assertEqual(self.invoice.amount_due, 100.00)
        self.assertEqual(self.invoice.order, self.order)