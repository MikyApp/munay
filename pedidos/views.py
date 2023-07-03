from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages
# from flask import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from pedidos.models import LineaPedido, Pedido
from django.utils.html import strip_tags

# Create your views here.

@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido =list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

            producto_id = key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido

        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(        
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario = request.user.username,
        emailusuario = request.user.email
    )


    messages.success(request, "El pedido se ha creado correctamente")

    return redirect("../tienda")


def enviar_mail(**kwargs): 
    asunto ="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario"),

    })

    mensaje_texto = strip_tags(mensaje)
    from_email="miguelpaucar987@gmail.com"
    #to=kwargs.get("emailusuario")
    to="mpaucarporras@gmail.com"
    send_mail(asunto, mensaje_texto, from_email, [to],html_message=mensaje)