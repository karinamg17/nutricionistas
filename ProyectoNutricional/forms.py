from django import forms
from django.forms import fields
from .models import Recetas,Alimento, Usuarios

class RecetaForm(forms.ModelForm):

    class Meta:
        model = Recetas
        fields = '__all__'

class AlimentoForm(forms.ModelForm):

    class Meta:
        model = Alimento
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields ='__all__'