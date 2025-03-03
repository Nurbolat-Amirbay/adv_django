from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()

    def __str__(self):
        return self.name

class Consume(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    date_consumed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} consumed {self.food.name} on {self.date_consumed}"