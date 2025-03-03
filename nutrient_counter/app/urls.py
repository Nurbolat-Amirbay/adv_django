from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_food/', views.add_food, name='add_food'),
    path('delete/<int:id>/', views.delete_consume, name='delete'),
    path('visualize_food/', views.visualize_food, name='visualize_food'),
]