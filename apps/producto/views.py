from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Producto, Categoria
from .forms import FormularioProducto

def index(request):
    obtenerP = Producto.objects.all()
    obtenerC = Categoria.objects.all()
    datos = {
        "productos": obtenerP,
        "categorias": obtenerC
    }
    return render(request, 'principal.html', datos)

def agregar(request):
    formularioP = FormularioProducto()
    if request.method == 'POST':
        formularioP = FormularioProducto(request.POST)
        if formularioP.is_valid():
            formularioP.save()
    context = {
        'formulario': formularioP,
        'titulo': 'Agregar Producto'
    }
    return render(request, 'producto.html', context) 

def eliminar(request, producto_id):
    productoAgregado = None
    try:
        productoAgregado = Producto.objects.get(id = producto_id)
        productoAgregado.delete()
    except:
        pass
    return redirect('index')        
# Create your views here.
