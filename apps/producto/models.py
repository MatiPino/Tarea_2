from django.db import models
from apps.categoria.models import Categoria

# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField('Nombre del producto', max_length=50, blank=False, null= False)
    precio_producto = models.SmallIntegerField('Precio del producto', blank=False, null=False)
    codigo_barra = models.CharField('Codigo de barra', blank=False, null=False, max_length=150)

    # Uno a Uno
    # on_delete CASCADE = Me llevo a mi y a todos conmigo
    # on_delete RESTRICT = Protege el borrado si hay relaciones usadas
    # on_delete SET_NULL = Toda la dependencia a Nulos
    # on_delete SET_DEFAULT = Al borrar aplica el valor que esta en la clausula default

    # categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE)

    # Uno a Muchos
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE ,null=True)

    # Muchos a Muchos
    # categoria_muchos_muchos = models.ManyToManyField(Categoria)

