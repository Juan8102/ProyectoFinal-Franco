from django.contrib.auth.models import User
from django.db import models

class Noticia(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    titulo=models.CharField(max_length=200)
    subtitulo=models.CharField(max_length=300)
    cuerpo=models.CharField(max_length=24000, null=True)
    autor=models.CharField(max_length=100)
    fecha=models.DateField()

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.fecha}"

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
