from django.urls import path
from . import views




urlpatterns = [    
    
    path('', views.Tienda, name='tienda'),
    path('carro/', views.Carro, name='carro'),

    
]


