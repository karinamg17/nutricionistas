import re

from allauth.account.forms import SignupForm
from django import forms as form2
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class DateInput(form2.DateInput):
    input_type = 'date'


class UserProfileForm(form2.ModelForm):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'nro_telefono',  'nro_telefono', 'sexo', 'fecha_nacimiento'
        widgets = {
            'fecha_nacimiento': DateInput(), 'sexo': form2.Select(attrs={'class': 'form-control default-select'}),
        }


class MyCustomSignupForm(SignupForm):
    TIPO_DOCUMENTO_CHOICES = (('Cédula', 'Cédula'), ('Cédula extranjería', 'Cédula extranjería'), ('Pasaporte', 'Pasaporte'),)

    first_name = form2.CharField(max_length=30, label='Nombres')
    last_name = form2.CharField(max_length=30, label='Apellidos')
    tipo_documento = form2.ChoiceField(choices=TIPO_DOCUMENTO_CHOICES)
    nro_documento = form2.CharField(max_length=25, label='Nro de documento de identidad', required=True, )
    accept_terms = form2.BooleanField(label='Acepto los términos y condiciones',)

    def clean_nro_documento(self):
        nro_documento = self.cleaned_data.get("nro_documento")
        # parse digits from the string
        nro_documento_list = re.findall("\d+", nro_documento)
        nro_documento = ''.join(nro_documento_list)

        if User.objects.filter(nro_documento=nro_documento).exists():
            raise form2.ValidationError("Ya existe un cliente con este nro. de documento.")
        return nro_documento

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.tipo_documento = self.cleaned_data['tipo_documento']
        user.nro_documento = self.cleaned_data['nro_documento']
        user.accept_terms = self.cleaned_data['accept_terms']
        user.validate_unique()
        user.save()

        return user
