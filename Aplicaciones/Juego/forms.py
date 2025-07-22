from django import forms
from .models import Juego
from Aplicaciones.Coleccionista.models import Coleccionista
from Aplicaciones.Editorial.models import Editorial

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo', 'genero', 'anio_lanzamiento', 'coleccionista', 'editorial']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'anio_lanzamiento': forms.NumberInput(attrs={'class': 'form-control', 'min': 1970, 'max': 2025}),
            'coleccionista': forms.Select(attrs={'class': 'form-select'}),
            'editorial': forms.Select(attrs={'class': 'form-select'}),
        }
