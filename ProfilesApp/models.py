from django.contrib.auth.models import User
from django.db import models

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
