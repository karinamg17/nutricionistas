from django.db.models import Count, Sum, Avg
from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from nutricionistas.users.models import User
from nutricionistas.nutri_app.models import Cita


class UserSerializer(serializers.ModelSerializer):

    foto_usuario = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'tipo_documento', 'nro_documento', 'fecha_nacimiento', 'nro_telefono', 'email', 'sexo', 'foto_usuario')


class CitaSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Cita
        fields = '__all__'


class CitaCalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cita
        fields = '__all__'