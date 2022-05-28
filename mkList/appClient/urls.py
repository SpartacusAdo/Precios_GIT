from django.urls import path

from . import views

app_name = 'appClient'                                      # Con este nombre es invocado en URL del core proyecto
urlpatterns = [

    path('cliente/', views.cliente, name='cliente'),                   # List
    path('nada/', views.nada, name='nada'),
    path('mod_cliente/<id>/', views.mod_cliente, name='mod_cliente'),  # modifica desde lista pasa id user al cliente
    path('crea_cliente/', views.crea_cliente, name='crea_cliente'),    # Crea desde lista
    path('mod_datos/<user>/', views.mod_datos, name='mod_datos'),      # crea modifica desde login pasa el user al cliente
    ]