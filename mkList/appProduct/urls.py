from django.urls import path
from . import views

app_name = 'appProduct'             # Con este nombre es invocado en URL del core proyecto
urlpatterns =[
     #path('<slug:category_slug>/<product_slug>/', views.product,  name='product'),
     path('add_categoria/',        views.add_categoria,      name='add_categoria'),
     path('list_categoria/',       views.list_categoria,     name='list_categoria'),
     path('mod_categoria/<id>/',   views.mod_categoria,      name='mod_categoria'),
     path('del_categoria/<id>/',   views.del_categoria,      name='del_categoria'),
     path('add_colores/', views.add_colores,      name='add_colores'),
     path('list_colores/', views.list_colores,    name='list_colores'),
     path('mod_colores/<id>/', views.mod_colores, name='mod_colores'),
     path('del_colores/<id>/', views.del_colores, name='del_colores'),
     path('add_bulbo/', views.add_bulbo,      name='add_bulbo'),
     path('list_bulbo/', views.list_bulbo,    name='list_bulbo'),
     path('mod_bulbo/<id>/', views.mod_bulbo, name='mod_bulbo'),
     path('del_bulbo/<id>/', views.del_bulbo, name='del_bulbo'),
     path('<slug:category_slug>/', views.category,           name='category'),
]  