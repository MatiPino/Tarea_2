from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Categoria
from .forms import FormularioCategoria

def index(request):

    formularioC = FormularioCategoria()
    if request.method == 'POST':
        formularioC = FormularioCategoria(request.POST)
        if formularioC.is_valid():
            formularioC.save()
    context = {'formulario': formularioC,
               'titulo': 'Agregar Categoria'}

    return render(request, 'producto.html', context)        

# Create your views here.
