# -*- coding: utf-8 -*-
import datetime
from datetime import date, timedelta, datetime
from json import dumps

from braces.views import GroupRequiredMixin, LoginRequiredMixin
from dateutil.relativedelta import relativedelta
from django import http
from django.contrib import messages
from django.contrib.auth import models
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Case, Count, F, IntegerField, Q, Sum, Value, When
from django.http import request
from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from nutricionistas.nutri_app.models import Cita


class PacienteCalendarTemplateView(LoginRequiredMixin,TemplateView):

    template_name = 'nutri_app/paciente/paciente_calendar.html'

    def get_context_data(self, **kwargs):
        context = super(PacienteCalendarTemplateView, self).get_context_data(**kwargs)

        return context


class CitaPacientePendienteCalJsonView(APIView):

    def get(self, request, *args, **kwargs):

        d = self.request.GET.get('start') + 'T00:00:00'
        h = self.request.GET.get('end') + 'T23:59:59'

        desde = datetime.strptime(d, '%Y-%m-%dT%H:%M:%S')
        hasta = datetime.strptime(h, '%Y-%m-%dT%H:%M:%S')

        citas_qs = Cita.objects.filter(fecha__range=[desde, hasta], user_id=self.request.user.pk, completada=False, cancelada=False)

        citas_schedule = []

        limite_cancelar = date.today() + timedelta(days=1)
        puede_cancelar = True
        
        for c in citas_qs:

            ha = c.fecha + timedelta(minutes=60)
            da = datetime.date(c.fecha)

            
            if not c.completada and da < limite_cancelar:
                puede_cancelar = False

            print(da, limite_cancelar, puede_cancelar)

            citas = {
                'id': c.pk,
                'start': c.fecha.strftime("%Y-%m-%dT%H:%M:%S"),
                'end': ha.strftime("%Y-%m-%dT%H:%M:%S"),
                'allDay': False,
                'title': c.user.first_name,
                'diagnostico': c.diagnostico,
                'cancelada': c.cancelada,
                'completada': c.completada,
                'puede_cancelar': puede_cancelar
            }

            citas_schedule.append(citas)

        # r = { 'data': citas_schedule }

        data = dumps(list(citas_schedule), cls=DjangoJSONEncoder)
        print(data)
        return Response(citas_schedule)


class CitaPacienteCompletadoCalJsonView(APIView):

    def get(self, request, *args, **kwargs):

        d = self.request.GET.get('start') + 'T00:00:00'
        h = self.request.GET.get('end') + 'T23:59:59'

        desde = datetime.strptime(d, '%Y-%m-%dT%H:%M:%S')
        hasta = datetime.strptime(h, '%Y-%m-%dT%H:%M:%S')

        citas_qs = Cita.objects.filter(fecha__range=[desde, hasta], user_id=self.request.user.pk, completada=True)

        citas_schedule = []
        
        for c in citas_qs:

            ha = c.fecha + timedelta(minutes=60)
            
            citas = {
                'id': c.pk,
                'start': c.fecha.strftime("%Y-%m-%dT%H:%M:%S"),
                'end': ha.strftime("%Y-%m-%dT%H:%M:%S"),
                'allDay': False,
                'title': c.user.first_name,
                'diagnostico': c.diagnostico,
                'cancelada': c.cancelada,
                'completada': c.completada,
                'puede_cancelar': False
            }

            citas_schedule.append(citas)

        return Response(citas_schedule)


class CitaPacienteCanceladaCalJsonView(APIView):

    def get(self, request, *args, **kwargs):

        d = self.request.GET.get('start') + 'T00:00:00'
        h = self.request.GET.get('end') + 'T23:59:59'

        desde = datetime.strptime(d, '%Y-%m-%dT%H:%M:%S')
        hasta = datetime.strptime(h, '%Y-%m-%dT%H:%M:%S')

        citas_qs = Cita.objects.filter(fecha__range=[desde, hasta], user_id=self.request.user.pk, cancelada=True)

        citas_schedule = []
        
        for c in citas_qs:

            ha = c.fecha + timedelta(minutes=60)
            
            citas = {
                'id': c.pk,
                'start': c.fecha.strftime("%Y-%m-%dT%H:%M:%S"),
                'end': ha.strftime("%Y-%m-%dT%H:%M:%S"),
                'allDay': False,
                'title': c.user.first_name,
                'diagnostico': c.diagnostico,
                'cancelada': c.cancelada,
                'completada': c.completada,
                'puede_cancelar': False
            }

            citas_schedule.append(citas)

        return Response(citas_schedule)


class DisponibilidadCalJsonView(APIView):

    def get(self, request, *args, **kwargs):

        d = self.request.GET.get('date') + 'T00:00:00'
        h = self.request.GET.get('date') + 'T23:59:59'

        desde = datetime.strptime(d, '%Y-%m-%dT%H:%M:%S')
        hasta = datetime.strptime(h, '%Y-%m-%dT%H:%M:%S')

        citas_qs = Cita.objects.filter(fecha__range=[desde, hasta], user_id=self.request.user.pk, cancelada=False)

        citas_schedule = []
        horas_ocupadas = []
        
        for c in citas_qs:
            hora = "{:02d}:{:02d}".format(c.fecha.hour, c.fecha.minute)
            horas_ocupadas.append(hora)

        horas_disponibles = ['08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00']

        for item in horas_ocupadas:
            if item in horas_disponibles:
                horas_disponibles.remove(item)
        
        
        return Response(horas_disponibles)