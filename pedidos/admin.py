from django.contrib import admin
from .models import Pedido, LineaPedido
# Register your models here.


class PedidoAdmin(admin.ModelAdmin):
    list_display=("user",)



    
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(LineaPedido)
