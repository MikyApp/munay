from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def Contacto(request):
    if request.method=="POST":
        asunto = "Tienda munay"
        nombre=request.POST["nombres"]
        apellido=request.POST["apellidos"]
        email=request.POST["email"]
        telefono=request.POST["telefono"] 
        mensaje=request.POST["mensaje"]       
        enviar_mensaje="\nNombres: "+nombre+"\nApellidos: "+apellido+"\nEmail: "+email+ "\nTelefono: "+telefono+"\nMensaje: "+mensaje

        if not nombre or not apellido or not email or not telefono or not mensaje:
            alert_message = "Por favor, completa todos los campos del formulario."
            return render(request, 'contacto/contactos.html', {'message': alert_message})
        

        email_from=settings.EMAIL_HOST_USER
        recipient_list=["miguelpaucar987@gmail"]
        send_mail(asunto, enviar_mensaje, email_from, recipient_list )
        return render(request, 'contacto/contactos.html', {"men":nombre})
    
    return render(request, 'contacto/contactos.html')