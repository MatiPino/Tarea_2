from django import forms
from django.forms import widgets
from .models import Producto

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre_producto',
            'precio_producto',
            'codigo_barra',
            'categoria'
        ]
        widgets = {
            'nombre_producto': forms.TextInput(attrs={
                'class': 'nombre_p form-control bg-secondary text-light',
                'placeholder': 'Nombre del producto'
            }),
            'precio_producto': forms.TextInput(attrs={
                'class': 'precio form-control bg-secondary text-light',
                'type': 'number',
                'placeholder': 'Ingresa el precio del proucto'
            }),
            'codigo_barra': forms.TextInput(attrs={
                'class': 'codigo form-control bg-secondary text-light',
                'type': 'text',
                'placeholder': 'Ingresar codigo de barra'
            }),
        }