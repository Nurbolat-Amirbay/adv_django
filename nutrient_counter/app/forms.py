from django import forms
from .models import Food, Consume

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'carbs', 'proteins', 'fats', 'calories']

class ConsumeForm(forms.ModelForm):
    class Meta:
        model = Consume
        fields = ['food', 'user']