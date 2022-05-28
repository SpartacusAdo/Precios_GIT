from urllib.parse import uses_fragment
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages

from client.models import *

def cliente(request):   # Vista recibe id customer
                                  # Desde el DashBoard href="{% url 'customer' c.id %}">Ver</a></td>
    #clientes = request.user.cliente   
    clientes = Cliente.objects.all()       
    context = {'clientes': clientes}
    return render(request, 'appClient/listCliente.html', context)

def nada(request):   # Vista recibe id customer
                                  # Desde el DashBoard href="{% url 'customer' c.id %}">Ver</a></td>
    #clientes = request.user.cliente   
    clientes = Cliente.objects.all()       
    context = {'clientes': clientes}
    return render(request, 'appClient/nada.html', context)

def crea_cliente(request):
        data = {'form':ClienteAdminForm, 'step':True, 'titulo':False}
        if request.method == 'POST': 
            form = ClienteAdminForm(request.POST,)
            print('Validoooooooooooo', form.data)
            form.usuario = request.user
            if form.is_valid():
                print('OOOOOOOKKKKKKK')
                form.save()
                messages.success(request, 'Cliente creado correctamente')
                return redirect(to='appClient:cliente')
            else:
                print('ErroooooooooooorrrssXXXXXXXXXXXXXX')
                form = ClienteAdminForm()
                
        return render(request, 'appClient/modCliente.html', data)

def mod_cliente(request, id):
    iCliente=get_object_or_404(Cliente, pk=id)
    data = {'form' : ClienteForm(instance=iCliente), 'step':True, 'titulo':True}
    if request.method == 'POST':
        form = ClienteForm(data=request.POST, instance=iCliente)
        print('Antes de validar')
        if form.is_valid():
            print('Valido')
            form.save() 
            messages.success(request, 'Cliente modificado correctamente')
            return redirect(to='appClient:cliente')
        
        data["form"] = form
        
    return render(request, 'appClient/modCliente.html', data)

def mod_datos(request, user):
    
    try:
        print('Tryyyyyyy')
        iCliente=Cliente.objects.get(usuario=user)
       
        data = {'form' : ClienteForm(instance=iCliente), 'step':True, 'titulo':True}
        if request.method == 'POST':
            form = ClienteForm(data=request.POST, instance=iCliente, )
        
            if form.is_valid():
            
                form.save() 
                messages.success(request, 'Cliente modificado correctamente')
                return redirect(to='client:gallery')
        
            data["form"] = form
    except:
        
        print('Except')
        data = {'form':ClienteNuevoForm, 'step':False, 'titulo':False}
        
        if request.method == 'POST':
            
            form = ClienteNuevoForm(request.POST,)
            print('Validoooooooooooo', form.data)
            

            form.usuario =  request.user
            
            if form.is_valid():
                print('OOOOOOOKKKKKKK', user)
                #form.save()
                

                post = form.save(commit=False)
                post.usuario = request.user
                post.save()
                messages.success(request, 'Cliente creado correctamente')
                return redirect(to='client:gallery')
            else:
                print('ErroooooooooooorrrssXXXXXXXXXXXXXX', user)
                form = ClienteNuevoForm()
                
    return render(request, 'appClient/modCliente.html', data)

def del_cliente(request, iuser):
    ibulbo=get_object_or_404(Cliente, usuario=uses_fragment)
    ibulbo.delete()
    messages.success(request, 'Cliente eliminado')

    return redirect(to='product:list_bulbo')
