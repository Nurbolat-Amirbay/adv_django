from django.db import models

class SalesOrder(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_number} - {self.customer_name}"

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    invoice_date = models.DateTimeField(auto_now_add=True)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.invoice_number} for Order {self.sales_order.order_number}"