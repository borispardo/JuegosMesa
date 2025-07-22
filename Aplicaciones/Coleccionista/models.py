from django.core.validators import RegexValidator, EmailValidator
from django.db import models

class Coleccionista(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{7,15}$',
                message='Ingrese un número de teléfono válido (7 a 15 dígitos, puede iniciar con +).'
            )
        ]
    )
    direccion = models.CharField(max_length=255)
    correo = models.EmailField(
        max_length=254,
        validators=[EmailValidator(message="Ingrese un correo electrónico válido.")]
    )
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
