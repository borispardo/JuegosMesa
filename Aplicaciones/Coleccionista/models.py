from django.db import models

class Coleccionista(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
