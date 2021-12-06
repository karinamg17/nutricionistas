from django.db import models
from django.db.models.deletion import CASCADE
from nutricionistas.users.models import User


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
