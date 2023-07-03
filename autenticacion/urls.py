from django.urls import path
from .views import VRegistro, cerrar_sesion, Registro, logear




urlpatterns = [    
    
    path('', VRegistro.as_view(), name='autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('', Registro, name='registro'),
    path('logear', logear, name='logear'),
]


