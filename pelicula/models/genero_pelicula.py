from turtle import onkey

from django.db import models

from pelicula.models.genero import Genero
from pelicula.models.pelicula import Pelicula


class Genero_Pelicula(models.Model):
    lgenero = models.ForeignKey(Genero, related_name='genero', on_delete=models.CASCADE)
    lpelicula = models.ForeignKey(Pelicula , related_name='pelicula', on_delete=models.CASCADE)


    def __str__(self):
        return '('+ str(self.lgenero) +')' + '('+ str(self.lpelicula) +')'