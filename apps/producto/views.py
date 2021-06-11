from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
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

def modificar_producto(request, producto_id): 
    producto = get_object_or_404(Producto, id=producto_id)
    data = {
        'titulo': 'Editar Producto',
        'formulario': FormularioProducto(instance=producto)
    }
    if request.method == 'POST':
        formulario = FormularioProducto(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="index")
        data["formulario"] = formulario    
    
    return render(request, 'modificar.html', data)