from django.db import models

class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre + ' ' + self.codigo + self.descripcion