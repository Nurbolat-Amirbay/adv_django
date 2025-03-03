from django.test import TestCase
from .models import Food, Consume

class FoodModelTest(TestCase):
    def setUp(self):
        self.food = Food.objects.create(
            name='Apple',
            carbs=25,
            proteins=0.5,
            fats=0.3,
            calories=95
        )

    def test_food_creation(self):
        self.assertEqual(self.food.name, 'Apple')
        self.assertEqual(self.food.carbs, 25)
        self.assertEqual(self.food.proteins, 0.5)
        self.assertEqual(self.food.fats, 0.3)
        self.assertEqual(self.food.calories, 95)

class ConsumeModelTest(TestCase):
    def setUp(self):
        self.food = Food.objects.create(
            name='Banana',
            carbs=27,
            proteins=1.3,
            fats=0.3,
            calories=105
        )
        self.consume = Consume.objects.create(
            food=self.food,
            quantity=2
        )

    def test_consume_creation(self):
        self.assertEqual(self.consume.food, self.food)
        self.assertEqual(self.consume.quantity, 2)