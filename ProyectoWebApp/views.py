from django.shortcuts import render
from django.db import connection
from carro.carro import Carro

# Create your views here.

def Inicio(request):
    carro = Carro(request)
    try:
        # Intenta realizar una consulta a la base de datos
        # Si hay un problema de conexión, se lanzará una excepción
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tienda_producto")
            rows = cursor.fetchall()
        return render(request, 'ProyectoWebApp/inicio.html')

    except Exception as error:
        # Captura la excepción y muestra un mensaje de error personalizado
        error_message = "Lo sentimos, estamos experimentando problemas técnicos en este momento. Por favor, intenta nuevamente más tarde."
        return render(request, 'ProyectoWebApp/error.html', {"error":error_message, "e":error})
