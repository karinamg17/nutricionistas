from django import forms
from django.forms import fields
from .models import Recetas

class RecetaForm(forms.ModelForm):

    class Meta:
        model = Recetas
        fields = '__all__'