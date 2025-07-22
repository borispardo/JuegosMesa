from django import forms
from .models import Coleccionista

class ColeccionistaForm(forms.ModelForm):
    class Meta:
        model = Coleccionista
        fields = ['nombre', 'telefono', 'direccion', 'correo', 'fecha_registro']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_registro': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
