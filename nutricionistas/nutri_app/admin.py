from django.contrib import admin
from nutricionistas.nutri_app.models import Cita


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha')
    #inlines = [ServicioCostoAdicionalInline]
