from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout   # Importamos esto para LOGIN
from django.contrib import messages                           # Usado para mensajes de error en este caso LOGIN
from .forms import CreateUserForm                             # Para register usamos el CreateUserForm 
from django.contrib.auth.models import Group                  # Para save the group for user register new
from django.contrib.auth.decorators import login_required     # Sistema de autentication o  Django para validar login efectivo

from .models import *                                         # Import all models
from appProduct.models import *

def loginPage(request):
    
        if request.method == 'POST':
            username = request.POST.get('username')      # Rescatado del template
            password = request.POST.get('password')      # Rescatado del template
            user = authenticate(request, username=username, password=password)  # Para login
            if user is not None:
                login(request, user)      # Login
                return redirect('client:gallery')   # Al home
            else:
                messages.info(request, 'El usuario y/o la password es/estan incorrecto/a/s')

        context={}
        return render(request, 'client/login.html', context)
        
def registerPage(request):
    
    form = CreateUserForm()                        # Este reemplaza al form UseCreationForm que es mas basico
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()                     # Guardar el form en user
            username = form.cleaned_data.get('username')     # Guardar el username
            
            group = Group.objects.get(name='customer')        # Get group customer from group admin panel
            user.groups.add(group)                            # Add the group to user

            messages.success(request, 'Usuario creado correctamente ' + username)   # Mensaje de usuario guardado

            return redirect('login')

    context={'form': form}
    return render(request, 'client/register.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('client:login')

def customer(request, pk_test):   # Vista recibe id customer
                                  # Desde el DashBoard href="{% url 'customer' c.id %}">Ver</a></td>         
    context = {}
    return render(request, 'client/customer.html', context)

def gallery(request):
    bulbos = Bulbo.objects.all()
    context = {'bulbos':bulbos}
    return render(request, 'client/gallery.html', context)