from django.urls import path
from .views import Contacto




urlpatterns = [    
    
    path('', Contacto, name='contactos')
]


