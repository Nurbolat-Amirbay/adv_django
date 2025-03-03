from django.urls import path
from . import views

urlpatterns = [
    path('', views.trading_index, name='trading_index'),
    path('orders/', views.order_list, name='order_list'),
    path('transactions/', views.transaction_list, name='transaction_list'),
]