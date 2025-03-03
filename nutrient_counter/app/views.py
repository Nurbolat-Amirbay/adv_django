from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Consume
from .forms import FoodForm, ConsumeForm

def index(request):
    foods = Food.objects.all()
    if request.method == 'POST':
        consume_form = ConsumeForm(request.POST)
        if consume_form.is_valid():
            consume_form.save()
            return redirect('index')
    else:
        consume_form = ConsumeForm()
    
    return render(request, 'app/index.html', {'foods': foods, 'consume_form': consume_form})

def add_food(request):
    if request.method == 'POST':
        food_form = FoodForm(request.POST)
        if food_form.is_valid():
            food_form.save()
            return redirect('index')
    else:
        food_form = FoodForm()
    
    return render(request, 'app/add_food.html', {'food_form': food_form})

def delete_consume(request, consume_id):
    consume = get_object_or_404(Consume, id=consume_id)
    if request.method == 'POST':
        consume.delete()
        return redirect('index')
    
    return render(request, 'app/delete_food.html', {'consume': consume})

def visualize_food(request):
    consumed_foods = Consume.objects.all()
    return render(request, 'app/visualize_food.html', {'consumed_foods': consumed_foods})