from django.urls import path, include
from rest_framework.routers import DefaultRouter

from nutricionistas.nutri_app.views import (
    profile, users, paciente_calendar, nutricionista_calendar, pacientes
)

app_name = "nutri_app"

router = DefaultRouter()
router.register(r'pacientes', pacientes.UsersViewSet)
router.register(r'paciente_cita/(?P<user_id>\d+)', pacientes.CitaViewSet)
router.register(r'paciente_cita_cal', pacientes.CitaCalViewSet)


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
    
    path('nutricionista/', nutricionista_calendar.NutricionistaCalendarTemplateView.as_view(), name='nutricionista_calendar'),

    path('perfil', profile.UserPerfilDetailView.as_view(), name='user_profile_detail'),
    path('perfil/actualizar', profile.UserPerfilUpdateView.as_view(), name='user_profile_update'),
    path('perfil/actualizar/foto', profile.UserPhotolUpdateView.as_view(), name='user_profile_photo_update'),

]
