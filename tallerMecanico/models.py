from django.db import models


# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(primary_key=True, max_length=25)

    def __str__(self):
        return self.nombre


class Repuesto(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marcas = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='repuestos', null=True)
    publicar = models.BooleanField(default=False)
    comentario = models.TextField(default='--')

    def __str__(self):
        return self.nombre
