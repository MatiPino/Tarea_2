from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/', views.agregar , name='agregar'),
    path('eliminar/<producto_id>', views.eliminar, name='eliminarP'),
    path('modificar-producto/<producto_id>', views.modificar_producto, name="modificar_producto"),
]