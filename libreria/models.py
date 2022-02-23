from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to= 'imagenes/',verbose_name='Imagen', null=True)
    descripcion = models.TextField( verbose_name= 'Descripcion',null=True)

    def __str__(self): #esto es para poder ver el titulo y la descripcion en el panel administrativo
        fila = "Titulo:" + self.titulo + "=" + "Descripcion:" + self.descripcion
        return fila

    def delete(self,using=None, Keep_parents=False): #esta funcion es para borrar la imagen del libro
        self.imagen.storage.delete(self.imagen.name)
        super().delete()