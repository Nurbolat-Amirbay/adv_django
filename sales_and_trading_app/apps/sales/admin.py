from django.contrib import admin
from .models import SalesOrder, Invoice

admin.site.register(SalesOrder)
admin.site.register(Invoice)