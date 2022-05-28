from django.contrib import admin
from appProduct.models import Categoria, Color, Bulbo

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['color',]

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria',]

@admin.register(Bulbo)
class BulboAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'bulbo', 'creado_en', 'modificado_en', ]
    
