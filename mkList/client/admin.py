from django.contrib import admin

from .models import *

@admin.register(Cliente)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'dv', 'direccion', 'comuna', 'ciudad', 'fono']