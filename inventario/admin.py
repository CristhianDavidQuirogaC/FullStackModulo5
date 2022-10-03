from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Producto
from .models import Orden
from .models import OrdenProducto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "unidades") 
    ordering = ["precio"] #ordena la lista por precio de menor a mayor
    search_fields = ["nombre"] # hace una busqueda por nombres
    list_filter = ("disponible", "precio")

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Orden)
admin.site.register(OrdenProducto)


