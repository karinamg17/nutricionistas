from django.db import models
from django.db.models.deletion import CASCADE
from nutricionistas.users.models import User


class Cita(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nutri_paciente_cita')
    fecha = models.DateTimeField()
    diagnostico = models.TextField(default='', null=True, blank=True)
    completada = models.BooleanField(default=False)


class IndicadorBioquimico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nutri_paciente_indicadores_bioquimicos')
    fecha = models.DateField()
    colesterol = models.CharField(max_length=10, blank=True, null=True)
    trigliceridos = models.CharField(max_length=10, blank=True, null=True)
    hdl = models.CharField(max_length=10, blank=True, null=True)
    ldl = models.CharField(max_length=10, blank=True, null=True)
    glucosa_ayunas = models.CharField(max_length=10, blank=True, null=True)
    hemoglobina = models.CharField(max_length=10, blank=True, null=True)


class PeriodoMenstrual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nutri_paciente_periodo_mestrual')
    dias_menstruacion = models.CharField(max_length=2, blank=True, null=True)
    fecha_ultima_menstruacion = models.DateField(blank=True, null=True)
    sintomas_antes = models.CharField(max_length=100, blank=True, null=True)
    sintomas_despues = models.CharField(max_length=100, blank=True, null=True)
    embarazo = models.BooleanField(default=False)
    anticonceptivos = models.BooleanField(default=False)
    anticonceptivos_cuales = models.CharField(max_length=100, blank=True, null=True)