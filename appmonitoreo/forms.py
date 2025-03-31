from django import forms
from .models import Gato, RegistroTemperatura

class GatoForm(forms.ModelForm):
    class Meta:
        model = Gato
        fields = ['nombre', 'edad', 'raza', 'peso']

class RegistroTemperaturaForm(forms.ModelForm):
    class Meta:
        model = RegistroTemperatura
        fields = ['gato', 'temperatura']
