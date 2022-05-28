from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Color
from .forms import *
from django.contrib import messages     # Me permite enviar messages 


#--------------------------------------------------------------------------------------------------------------------
def category(request, category_slug):
    print (category_slug)
    categoria = get_object_or_404(Categoria, slug=category_slug)
    return render(request,  'client/gallery_category.html', {'categoria': categoria})

def add_categoria(request):
    data = {'form':CategoriaForm}

    if request.method == 'POST':
        form = CategoriaForm(data=request.POST,)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria ingresada correctamente')
        else:
            data["form"] = form

    return render(request, 'appProduct/categorias/add.html', data)
    
def list_categoria(request):
    categorias=Categoria.objects.all()
    data = {'categorias' : categorias}
    return render(request, 'appProduct/categorias/list.html', data)

def mod_categoria(request, id):
    icategoria=get_object_or_404(Categoria, id=id)
    data = {'form' : CategoriaForm(instance=icategoria)}
    if request.method == 'POST':
        form = CategoriaForm(data=request.POST, instance=icategoria, )
        if form.is_valid():
            form.save() 
            messages.success(request, 'Categoria modificada correctamente')
            return redirect(to='appProduct:list_categoria')
        data["form"] = form

    return render(request, 'appProduct/categorias/mod.html', data)

def del_categoria(request, id):
    icategoria=get_object_or_404(Categoria, id=id)
    icategoria.delete()
    messages.success(request, 'Categoria eliminada')

    return redirect(to='appProduct:list_categoria')

#--------------------------------------------------------------------------------------------------------------------

def add_colores(request):
    data = {'form':ColorForm}

    if request.method == 'POST':
        form = ColorForm(data=request.POST,)
        if form.is_valid():
            form.save()
            messages.success(request, 'Color ingresado correctamente')
        else:
            data["form"] = form

    return render(request, 'appProduct/colores/add.html', data)
    
def list_colores(request):
    colores=Color.objects.all()
    data = {'colores' : colores}
    return render(request, 'appProduct/colores/list.html', data)

def mod_colores(request, id):
    icolor=get_object_or_404(Color, id=id)
    data = {'form' : ColorForm(instance=icolor)}
    if request.method == 'POST':
        form = ColorForm(data=request.POST, instance=icolor, )
        if form.is_valid():
            form.save() 
            messages.success(request, 'Color modificado correctamente')
            return redirect(to='appProduct:list_colores')
        data["form"] = form

    return render(request, 'appProduct/colores/mod.html', data)

def del_colores(request, id):
    icolor=get_object_or_404(Color, id=id)
    icolor.delete()
    messages.success(request, 'Color eliminado')

    return redirect(to='appProduct:list_colores')


#-----------------------------------------------------------------

def add_bulbo(request):
    if request.method == 'POST':
        form = BulboForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bulbo ingresado correctamente')
            return redirect(to='appProduct:list_bulbo')
    else:
        form = BulboForm()

    return render(request, 'appProduct/mnt_bulbo/add_bulbo.html', {'form': form})




def list_bulbo(request):
    bulbos=Bulbo.objects.all()
    data = {'bulbos' : bulbos}
    return render(request, 'appProduct/mnt_bulbo/list_bulbo.html', data)

def mod_bulbo(request, id):
    ibulbo=get_object_or_404(Bulbo, id=id)
    data = {'form' : BulboForm(instance=ibulbo)}
    if request.method == 'POST':
        form = BulboForm(request.POST, request.FILES, instance=ibulbo, )
        if form.is_valid():
            form.save() 
            messages.success(request, 'Bulbo modificado correctamente')
            return redirect(to='appProduct:list_bulbo')
        
        data["form"] = form

    return render(request, 'appProduct/mnt_bulbo/mod_bulbo.html', data)

def del_bulbo(request, id):
    ibulbo=get_object_or_404(Bulbo, id=id)
    ibulbo.delete()
    messages.success(request, 'Bulbo eliminado')

    return redirect(to='appProduct:list_bulbo')