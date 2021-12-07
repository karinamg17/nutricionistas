from django.db import models
from nutricionistas.users.models import User
from model_utils import Choices
from model_utils.fields import StatusField


class Cita(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nutri_paciente_cita')
    fecha = models.DateTimeField()
    diagnostico = models.TextField(default='', null=True, blank=True)
    completada = models.BooleanField(default=False)
    cancelada = models.BooleanField(default=False)

    class Meta:
        ordering = ('-fecha',)


class IndicadorBioquimico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nutri_paciente_indicadores_bioquimicos')
    fecha = models.DateField()
    colesterol = models.CharField(max_length=10, blank=True, null=True)
    trigliceridos = models.CharField(max_length=10, blank=True, null=True)
    hdl = models.CharField(max_length=10, blank=True, null=True)
    ldl = models.CharField(max_length=10, blank=True, null=True)
    glucosa_ayunas = models.CharField(max_length=10, blank=True, null=True)
    hemoglobina = models.CharField(max_length=10, blank=True, null=True)


class DatosBiomedicos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nutri_paciente_datos_biomedicos')
    antecedentes = models.JSONField(default=dict)
    ginecologicos = models.JSONField(default=dict)
    medicamentos = models.JSONField(default=dict)
    preferencias_alimentarias = models.JSONField(default=dict)
    comidas = models.JSONField(default=dict)
    habitos = models.JSONField(default=dict)
    estilo_de_vida = models.JSONField(default=dict)
    actividad_fisica = models.JSONField(default=dict)


class FrecuenciaDeConsumo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nutri_paciente_frecuencia_consumo')
    alimento = models.CharField(max_length=100, blank=True, null=True)
    frecuencia = models.CharField(max_length=30, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)


class Deporte(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nutri_paciente_deportes')
    deporte = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    dias_semanas = models.CharField(max_length=10, blank=True, null=True)
    dias_descanso = models.CharField(max_length=10, blank=True, null=True)
    duracion = models.CharField(max_length=10, blank=True, null=True)
    horario = models.CharField(max_length=50, blank=True, null=True)
    merienda_pre = models.CharField(max_length=50, blank=True, null=True)
    merienda_post = models.CharField(max_length=50, blank=True, null=True)


class Suplemento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nutri_paciente_suplementos')
    nombre_suplemento = models.CharField(max_length=50, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    veces_por_dia = models.CharField(max_length=50, blank=True, null=True)
    dias_a_la_semana = models.CharField(max_length=50, blank=True, null=True)
    dosis = models.CharField(max_length=50, blank=True, null=True)


class TipoComida(models.Model):
    descripcion = models.TextField(default='', blank=True, null=True)
    kcal = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.descripcion


class Menu(models.Model):
    nombre_menu = models.CharField(max_length=100,)

    def __str__(self):
        return self.nombre_menu


class MenuLine(models.Model):
    COMIDAS_CHOICES = Choices('Comida 1', 'Comida 2', 'Comida 3', 'Comida 4', 'Comida 5', 'Comida 6', 'Colación')

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='nutri_menu_lines', default=1)
    comida = StatusField(choices_name='COMIDAS_CHOICES', default='Comida 1')
    tipo_comida = models.ForeignKey(TipoComida, on_delete=models.CASCADE, related_name='nutri_menu_tipo_comidas')
