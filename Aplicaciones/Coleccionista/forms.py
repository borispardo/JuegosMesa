from django import forms
from .models import Coleccionista

class ColeccionistaForm(forms.ModelForm):
    class Meta:
        model = Coleccionista
        fields = ['nombre', 'telefono', 'direccion', 'correo']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.replace(' ', '').isalpha():
            raise forms.ValidationError('El nombre solo debe contener letras y espacios.')
        return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        
        if len(telefono) < 7 or len(telefono) > 15:
            raise forms.ValidationError('El teléfono debe tener entre 7 y 15 caracteres.')
        return telefono

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if correo and not correo.endswith(('.com', '.org', '.net', '.edu')):
            raise forms.ValidationError('El correo debe terminar en .com, .org, .net o .edu')
        return correo
