from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'), #esta es la ruta de la app libreria
    path('nosostros',views.nostros,name='nosotros')
]