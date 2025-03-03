from django.shortcuts import render
from django.http import JsonResponse
from .models import SalesOrder, Invoice
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the sales index.")

def sales_order_list(request):
    sales_orders = SalesOrder.objects.all()
    return JsonResponse({'sales_orders': list(sales_orders.values())})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return JsonResponse({'invoices': list(invoices.values())})

def sales_index(request):
    return render(request, 'sales/index.html')