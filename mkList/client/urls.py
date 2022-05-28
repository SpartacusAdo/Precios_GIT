from django.urls import path
from . import views

app_name = 'client'                    # Con este nombre es invocado en URL del core proyecto
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),  # Viene el ID del customer

    path('gallery/', views.gallery, name='gallery'),

    ]