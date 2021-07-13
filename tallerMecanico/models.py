from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(primary_key=True, max_length=25)

    def __str__(self):
        return self.nombre


class Repuesto(models.Model):
    nombre = models.CharField(primary_key=True, max_length=25)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='repuestos',null=True)

    def __str__(self):
        return self.nombre
