from django.db import models

class Editorial(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
