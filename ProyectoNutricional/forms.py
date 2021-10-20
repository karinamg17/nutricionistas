from django import forms
from django.forms import fields
from .models import Recetas,Alimento

class RecetaForm(forms.ModelForm):

    class Meta:
        model = Recetas
        fields = '__all__'

class AlimentoForm(forms.ModelForm):

    class Meta:
        model = Alimento
        fields = '__all__'