from django.urls import path, include
from rest_framework.routers import DefaultRouter

from nutricionistas.nutri_app.views import (
    profile, users, paciente_calendar, nutricionista_calendar, pacientes, tipo_comida, menus
)

app_name = "nutri_app"


router = DefaultRouter()
router.register(r'pacientes', pacientes.UsersViewSet)
router.register(r'paciente_cita_cal', pacientes.CitaCalViewSet)
router.register(r'paciente_cita/(?P<user_id>\d+)', pacientes.CitaViewSet)
router.register(r'frecuencia_de_consumo/(?P<user_id>\d+)', pacientes.FrecuenciaDeConsumoViewSet)
router.register(r'deportes/(?P<user_id>\d+)', pacientes.DeporteViewSet)
router.register(r'suplementos/(?P<user_id>\d+)', pacientes.SuplementoViewSet)
router.register(r'paciente/indicador_bioquimico/(?P<user_id>\d+)', pacientes.IndicadorBioquimicoViewSet)
router.register(r'paciente/datos_biomedicos', pacientes.DatosBiomedicosViewSet)

urlpatterns = [

    path("api/", include(router.urls)),

    path('users/', users.UserListView.as_view(), name='users_list'),
    path('users/create', users.UserCreateView.as_view(), name='usuario_create'),
    path('users/edit/<int:pk>', users.UserUpdateView.as_view(), name='usuario_edit'),
    path('users/detail/<int:pk>', users.UserDetailView.as_view(), name='usuario_detail'),
    path('users/delete/<int:pk>', users.UserDelete.as_view(), name='usuario_delete'),
    path('users/change_passwd/<int:pk>', users.UserUpdatePasswdView.as_view(), name='usuario_change_passwd'),

    path('pacientes/', pacientes.PacientesTemplateView.as_view(), name='pacientes_list'),
    path('pacientes/detail/<int:pk>', pacientes.PacientesDetailView.as_view(), name='pacientes_detail'),
    path('pacientes/data/calendar/pendiente', nutricionista_calendar.CitasPendienteCalJsonView.as_view(), name='paciente_data_calendar_pendiente'),
    path('pacientes/data/calendar/completado', nutricionista_calendar.CitasCompletadaCalJsonView.as_view(), name='paciente_data_calendar_completado'),

    path('paciente/', paciente_calendar.PacienteCalendarTemplateView.as_view(), name='paciente_calendar'),
    path('paciente/data/calendar/pendiente', paciente_calendar.CitaPacientePendienteCalJsonView.as_view(), name='paciente_data_calendar_pendiente'),
    path('paciente/data/calendar/completado', paciente_calendar.CitaPacienteCompletadoCalJsonView.as_view(), name='paciente_data_calendar_completado'),
    path('paciente/data/calendar/cancelado', paciente_calendar.CitaPacienteCanceladaCalJsonView.as_view(), name='paciente_data_calendar_cancelado'),
    path('paciente/data/calendar/disponibilidad', paciente_calendar.DisponibilidadCalJsonView.as_view(), name='paciente_data_calendar_disponibilidad'),
    
    path('nutricionista/', nutricionista_calendar.NutricionistaCalendarTemplateView.as_view(), name='nutricionista_calendar'),

    path('perfil', profile.UserPerfilDetailView.as_view(), name='user_profile_detail'),
    path('perfil/actualizar', profile.UserPerfilUpdateView.as_view(), name='user_profile_update'),
    path('perfil/actualizar/foto', profile.UserPhotolUpdateView.as_view(), name='user_profile_photo_update'),

    path('menu/', menus.MenuListView.as_view(), name='menu_list'),
    path('menu/create', menus.MenuCreateView.as_view(), name='menu_create'),
    path('menu/edit/<int:pk>', menus.MenuUpdateView.as_view(), name='menu_edit'),
    path('menu/detail/<int:pk>', menus.MenuDetailView.as_view(), name='menu_detail'),
    path('menu/delete/<int:pk>', menus.MenuDeleteView.as_view(), name='menu_delete'),

    path('menu_line/create/<int:menu_id>', menus.MenuLineCreateView.as_view(), name='menu_line_create'),
    path('menu_line/edit/<int:menu_id>/<int:pk>', menus.MenuLineUpdateView.as_view(), name='menu_line_edit'),
    path('menu_line/delete/<int:menu_id>/<int:pk>', menus.MenuLineDeleteView.as_view(), name='menu_line_delete'),

    path('tipo_comida/', tipo_comida.TipoComidaListView.as_view(), name='tipo_comida_list'),
    path('tipo_comida/create', tipo_comida.TipoComidaCreateView.as_view(), name='tipo_comida_create'),
    path('tipo_comida/edit/<int:pk>', tipo_comida.TipoComidaUpdateView.as_view(), name='tipo_comida_edit'),
    path('tipo_comida/detail/<int:pk>', tipo_comida.TipoComidaDetailView.as_view(), name='tipo_comida_detail'),
    path('tipo_comida/delete/<int:pk>', tipo_comida.TipoComidaDeleteView.as_view(), name='tipo_comida_delete'),



]
