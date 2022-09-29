from django.db import models
from django.conf import settings
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True) #Unique determina que nuestra ruta será la unica
    def __str__(self):
        return self.nombre #Cuando llamo al objeto este me devolverá el atributo Nombre de cada clase

class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Unidades'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    description = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits = 10)
    unidades = models.CharField(max_length=2, choices=ProductUnits.choices, default=ProductUnits.UNITS)
    disponible = models.BooleanField(blank = True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre #Cuando llamo al objeto este me devolverá el atributo Nombre de cada clase en la consola de admin de DJANGO

class EstadoOrden(models.TextChoices):
    PAGADO = 'pagado', 'Ya pagó'
    DEBE = 'debe', 'No pagó'

class Orden(models.Model):
    total = models.IntegerField(default=0)
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inventario_orden_vendedor')
    fecha = models.DateField()
    estado =  models.CharField(max_length=10, choices=EstadoOrden.choices, default=EstadoOrden.DEBE)

class OrdenProducto (models.Model):
    orden  =  models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto =  models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad =  models.DecimalField(decimal_places=2, max_digits = 10)