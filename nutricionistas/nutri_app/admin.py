from django.contrib import admin
from nutricionistas.nutri_app.models import Cita, IndicadorBioquimico, DatosBiomedicos


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha')


@admin.register(DatosBiomedicos)
class DatosBiomedicosAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(IndicadorBioquimico)
class IndicadorBioquimicoAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha')
