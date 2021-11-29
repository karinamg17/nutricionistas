from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from model_utils.fields import StatusField
from versatileimagefield.fields import VersatileImageField
import datetime

from dateutil import relativedelta


class User(AbstractUser):
    """Default user for nutricionistas."""

    TIPO_DOCUMENTO_CHOICES = Choices(_('Cédula'), _('Cédula extranjería'), _('Pasaporte'), )
    SEXO_CHOICES = Choices(_('Masculino'), _('Femenino'),)
    
    tipo_documento = StatusField(choices_name='TIPO_DOCUMENTO_CHOICES', default=('Cédula'))
    nro_documento = models.CharField(_('Nro. de documento'), max_length=12, unique=True, default='')
    fecha_nacimiento = models.DateField(_('Fecha de nacimiento'), blank=True, null=True,)
    sexo = StatusField(choices_name='SEXO_CHOICES', default='Masculino')
    nro_telefono = models.CharField(_('Nro. de teléfono'), max_length=12, unique=True, default='')
    ocupación = models.CharField(_('Ocupación'), max_length=100, default='', null=True, blank=True)
    
    accept_terms = models.BooleanField(default=False)

    foto_usuario = VersatileImageField(_(
        'Foto perfil de usuario'),
        upload_to='images/foto_perfil',
        blank=True,
        null=True,
        help_text="Suba un foto en formato jpge o png"
    )

    @property
    def get_user_profile(self):
        user_profile = 'Ninguno'
        if self.groups.filter(name='Administrador').exists():
            user_profile = 'Administrador'

        if self.groups.filter(name='Profesional').exists():
            user_profile = 'Profesional'

        if self.groups.filter(name='Paciente').exists():
            user_profile = 'Paciente'

        return user_profile
    
    @property
    def edad(self):
        retorno = None
        hoy = datetime.date.today()
        if self.fecha_nacimiento:
            retorno = u"%s" % relativedelta.relativedelta(hoy, self.fecha_nacimiento).years
        return retorno
