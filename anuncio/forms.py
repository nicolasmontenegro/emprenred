from django import forms

from . import models

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = models.Anuncio
        fields = ('titulo','descripcion','etiqueta',)
    