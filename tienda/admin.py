from django.contrib import admin
from .models import Producto, Categoria


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    search_fields=("nombre",)
    
class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre", "categorias", "imagen", "precio", "stock", "disponibilidad")
    search_fields=("nombre",)
    readonly_fields=("created", "updated")

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
