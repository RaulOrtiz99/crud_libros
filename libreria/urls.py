from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'), #esta es la ruta de la app libreria
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros',views.libros,name='libros'),
    path('libros/crear',views.crear,name='crear'),
    path('libros/editar',views.editar,name='editar'),
]