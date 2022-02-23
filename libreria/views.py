from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def libros(request):  # con esta funcion devolvemos la lista de todos los libros
    libros = Libro.objects.all()  # asi obtenemos todos los libros
    print(libros)
    return render(request, 'libros/index.html', {'libros': libros})


def crear(request):  # esta funcion es para crear un libro
    formulario = LibroForm(request.POST or None)
    return render(request, 'libros/crear.html',{'formulario':formulario})


def editar(request):
    return render(request, 'libros/editar.html')
