from django.urls import path
from ProyectoWebApp import views
from django.conf import settings

from django.conf import Settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', views.Inicio, name='inicio'),    
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
