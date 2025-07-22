from django import forms
from .models import Editorial

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['titulo', 'autor', 'fecha', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': True}),
        }
