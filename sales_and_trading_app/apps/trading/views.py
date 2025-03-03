from django.shortcuts import render
from django.http import JsonResponse
from .models import Order, Transaction

def order_list(request):
    orders = Order.objects.all()
    return JsonResponse({'orders': list(orders.values())})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return JsonResponse({'transactions': list(transactions.values())})

def trading_index(request):
    return render(request, 'trading/index.html')