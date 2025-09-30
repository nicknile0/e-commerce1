from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion = models.TextField(blank = True)
    precio = models.IntegerField(default = 0)
    stock = models.IntegerField(default = 0)
    imagen = models.URLField(blank = True)

    def __str__(self):
        return self.nombre
