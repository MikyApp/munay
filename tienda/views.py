from django.shortcuts import render
from .models import Producto
# Create your views here.
def Tienda(request):

    productos = Producto.objects.all()
    # modificado
    if request.method == 'POST':
        dato = request.POST.get('prod')
        productos = Producto.objects.filter(nombre__icontains=dato)
    # modificado
        return render(request, 'tienda/tienda.html', {"productos":productos, "query":dato})
    # modificado
    else:
        return render(request, 'tienda/tienda.html', {"productos":productos})


def Carro(request):
    return render(request, 'tienda/widget.html')


