from django.db import models
from Aplicaciones.Coleccionista.models import Coleccionista
from Aplicaciones.Editorial.models import Editorial

class Juego(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    anio_lanzamiento = models.IntegerField()

    coleccionista = models.ForeignKey(Coleccionista, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
