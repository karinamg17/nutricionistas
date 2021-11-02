from django import forms
from django.forms import fields
from .models import *

class RecetaForm(forms.ModelForm):

    class Meta:
        model = Recetas
        fields = '__all__'

class AlimentoForm(forms.ModelForm):

    class Meta:
        model = Alimento
        fields = '__all__'

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = '__all__'