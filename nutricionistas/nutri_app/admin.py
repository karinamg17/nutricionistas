from django.contrib import admin
from nutricionistas.nutri_app.models import (
    Cita, 
    IndicadorBioquimico, 
    DatosBiomedicos,
    TipoComida,
    Menu,
    MenuLine
)


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha')


@admin.register(DatosBiomedicos)
class DatosBiomedicosAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(IndicadorBioquimico)
class IndicadorBioquimicoAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha')


@admin.register(TipoComida)
class TipoComidaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'kcal')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_menu')


@admin.register(MenuLine)
class MenuLineAdmin(admin.ModelAdmin):
    list_display = ('comida', 'tipo_comida')
