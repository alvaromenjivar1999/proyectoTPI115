from django.db import models
from cuenta.models import Cuenta
# Create your models here.


class Video(models.Model):
    nombre = models.CharField(max_length=120)
    fechaPublicacion = models.DateField()
    categoria = models.CharField(max_length=30)
    palabraClave = models.CharField(max_length=30)
    usuario = models.ForeignKey("cuenta.Cuenta", on_delete=models.SET_NULL, null=True)
    recurso = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre
    

class Favoritos(models.Model):
    usuario = models.ForeignKey("cuenta.Cuenta", on_delete=models.SET_NULL, null=True)
    videos = models.ManyToManyField(Video)

    def __str__(self):
        return str(self.usuario)


class VerMasTarde(models.Model):
    usuario = models.ForeignKey("cuenta.Cuenta", on_delete=models.SET_NULL, null=True)
    videos = models.ManyToManyField(Video)

    def __str__(self):
        return str(self.usuario)