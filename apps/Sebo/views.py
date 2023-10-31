from django.shortcuts import render, redirect
from .models import *
from django.views.generic.list import ListView
from .forms import *
# Create your views here.

def listarDiscos(request):

    discos = Disco.objects.all()
    return render(request, 'base_lista_discos.html', {'discos': discos})

def detalheDisco(request, pk):

    disco = Disco.objects.get(pk=pk)
    return render(request, 'detalhe_disco.html', {'disco':disco})

def add_disco(request):

    if request.method == "GET":
        form = formDisco()

    else:
        form = formDisco(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_discos')
    
    return render(request, 'add_disco.html', {'form':form})

def edit_disco(request, pk):

    obj = Disco.objects.get(pk = pk)
    form = formDisco(request.POST, instance=obj)

    if request.method == "GET":
        initial_data = {field: getattr(obj, field) for field in obj.__dict__.keys() if field in formDisco.Meta.fields}
        form = formDisco(instance=obj, initial=initial_data)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect('listar_discos')

    return render(request, 'edit_disco.html', {'form':form})

def delet_disco(request, pk):

    obj = Disco.objects.get(pk=pk)

    if request.method == "POST":

        obj.delete()
        return redirect('listar_discos')
    
    return render(request, 'delet_disco.html')
