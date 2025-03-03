from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    asset = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_type = models.CharField(max_length=10, choices=[('buy', 'Buy'), ('sell', 'Sell')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_type.capitalize()} Order {self.order_id} for {self.quantity} of {self.asset}"

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    executed_price = models.DecimalField(max_digits=10, decimal_places=2)
    executed_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} for Order {self.order.order_id}"