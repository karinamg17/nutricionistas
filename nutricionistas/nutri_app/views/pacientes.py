# -*- coding: utf-8 -*-
import datetime
from datetime import date
import json

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
from rest_framework import generics, mixins, viewsets

from nutricionistas.nutri_app.models import Cita, IndicadorBioquimico, DatosBiomedicos, FrecuenciaDeConsumo, Deporte, Suplemento
from nutricionistas.nutri_app.serializers import (
    CitaCalSerializer,
    CitaSerializer, IndicadorBioquimicoSerializer,
    UserSerializer, DatosBiomedicosSerializer, FrecuenciaDeConsumoSerializer,
    DeporteSerializer, SuplementoSerializer
)
from nutricionistas.users.models import User


class PacientesTemplateView(GroupRequiredMixin, TemplateView):

    # required
    group_required = [u"Administrador"]
    raise_exception = True

    template_name = 'nutri_app/nutricionista/pacientes.html'

    def get_context_data(self, **kwargs):
        context = super(PacientesTemplateView, self).get_context_data(**kwargs)

        return context


class PacientesDetailView(GroupRequiredMixin, DetailView):

    # required
    group_required = [u"Administrador"]
    raise_exception = True

    model = User
    context_object_name = "paciente"

    template_name = 'nutri_app/nutricionista/pacientes_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PacientesDetailView, self).get_context_data(**kwargs)

        p, created = DatosBiomedicos.objects.get_or_create(user_id=self.kwargs['pk'])

        if created:
            data_indicadores = []

            #  registro antecedentes
            indicadores = ['Hipertensión', 'Diabetes Mellitus', 'ECV', 'Enfermedades de Tiroides', 'Cáncer', 'Estreñimiento',
                           'Diarreas', 'Vomitos', 'Problemas de Peso', 'Ansiedad-Depresión']

            for x in indicadores:
                ind = {}
                ind['indicador'] = x
                ind['personal'] = False
                ind['familiar'] = False

                data_indicadores.append(ind)

            #

            p.antecedentes = data_indicadores

            # registro ginecologicos
            data_indicadores = []

            indicadores = ['Anticonceptivos', '¿Cuáles?', 'Embarazo actual', 'Días de menstruación', 'Fecha de ultima menstruación',
                           'Sintomas Antes', 'Sintomas Durante']

            for x in indicadores:
                ind = {}
                ind['indicador'] = x
                ind['valor'] = ''

                data_indicadores.append(ind)

            p.ginecologicos = data_indicadores

            # preferencias_alimentarias
            data_indicadores = []

            indicadores = ['¿Presenta alguna alergia alimentaria?', 
                           '¿Cúal presenta?',
                           '¿Presenta alguna intolerancia alimentaria?', 
                           '¿Cúal presenta?.',
                           '¿Dónde mayormente come? En casa o trabajo',
                           '¿Cocina o compra sus alimentos?', '¿Cómo califica su alimentación?',
                           '¿Cómo califica su apetito?',
                           '¿Presenta ansiedad por la comida?', '¿Qué consume para la ansiedad?',
                           '¿Le añade sal a la comida ya preparada?'
                           ]

            for x in indicadores:
                ind = {}
                ind['indicador'] = x
                ind['valor'] = 'No'

                data_indicadores.append(ind)

            p.preferencias_alimentarias = data_indicadores

            # Habitos
            data_indicadores = []

            indicadores = ['Desayuno', 'Merienda mañana', 'Almuerzo', 'Merienda Tarde',  'Cena', 'Colación Nocturna', 'Otro']

            for x in indicadores:
                ind = {}
                ind['indicador'] = x
                ind['valor'] = 'Si'

                data_indicadores.append(ind)

            p.comidas = data_indicadores

            # Habitos
            data_indicadores = []

            indicadores = ['Alcohol', 'Tabaco', 'Drogas']

            for x in indicadores:
                ind = {}
                ind['indicador'] = x
                ind['valor'] = 'No'
                ind['frecuencia'] = ''
                ind['tipo'] = ''
                ind['cantidad'] = ''

                data_indicadores.append(ind)

            p.habitos = data_indicadores

            # estilo_de_vida
            data_indicadores = []

            indicadores = [
                'Muy ligera (trabajo de escritorio, choferes)',
                'Ligera (trabajo de poco esfuerzo)',
                'Moderada (carpinteros,estudiantes, área médica, maestro)',
                'Pesada (mecánicos, obreros, albañiles, deportistas)'
                'Exhaustiva (campesinos, deportistas de alto rendimiento)',
                '¿Realiza Ejercicio?',
                'Fecha de Ingreso',
            ]

            for x in indicadores:
                ind = {}
                ind['indicador'] = x
                ind['valor'] = 'No'
                ind['frecuencia'] = ''
                ind['tipo'] = ''
                ind['cantidad'] = ''

                data_indicadores.append(ind)

            p.estilo_de_vida = data_indicadores

            # actividad_fisica
            data_indicadores = []

            indicadores = [
                'Muy ligera (trabajo de escritorio, choferes)',
                'Ligera (trabajo de poco esfuerzo)',
                'Moderada (carpinteros,estudiantes, área médica, maestro)',
                'Pesada (mecánicos, obreros, albañiles, deportistas)Exhaustiva (campesinos, deportistas de alto rendimiento)',
                '¿Realiza Ejercicio?',
                'Fecha de Ingreso'
            ]

            for x in indicadores:
                ind = {}
                ind['indicador'] = x
                ind['valor'] = 'No'

                data_indicadores.append(ind)

            p.actividad_fisica = data_indicadores

            p.save()

        context['datos_biomedicos_id'] = p.pk
        context['antecedentes'] = json.dumps(p.antecedentes)
        context['preferencias_alimentarias'] = json.dumps(p.preferencias_alimentarias)
        context['comidas'] = json.dumps(p.comidas)
        context['habitos'] = json.dumps(p.habitos)
        context['actividad_fisica'] = json.dumps(p.actividad_fisica)
        
        context['estilo_de_vida'] = json.dumps(p.estilo_de_vida)
        
        context['ginecologicos'] = json.dumps(p.ginecologicos)

        return context


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CitaCalViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaCalSerializer


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

    def get_queryset(self, **kwargs):
        user_id = self.kwargs['user_id']

        cita_qs = Cita.objects.filter(user_id=user_id)

        return cita_qs


class IndicadorBioquimicoViewSet(viewsets.ModelViewSet):
    queryset = IndicadorBioquimico.objects.all()
    serializer_class = IndicadorBioquimicoSerializer

    def get_queryset(self, **kwargs):
        user_id = self.kwargs['user_id']

        indicador_bioquimico_qs = IndicadorBioquimico.objects.filter(user_id=user_id)

        return indicador_bioquimico_qs


class FrecuenciaDeConsumoViewSet(viewsets.ModelViewSet):
    queryset = FrecuenciaDeConsumo.objects.all()
    serializer_class = FrecuenciaDeConsumoSerializer

    def get_queryset(self, **kwargs):
        user_id = self.kwargs['user_id']

        frecuencia_de_consumo_qs = FrecuenciaDeConsumo.objects.filter(user_id=user_id)

        return frecuencia_de_consumo_qs


class DeporteViewSet(viewsets.ModelViewSet):
    queryset = Deporte.objects.all()
    serializer_class = DeporteSerializer

    def get_queryset(self, **kwargs):
        user_id = self.kwargs['user_id']

        deporte_qs = Deporte.objects.filter(user_id=user_id)

        return deporte_qs


class SuplementoViewSet(viewsets.ModelViewSet):
    queryset = Suplemento.objects.all()
    serializer_class = SuplementoSerializer

    def get_queryset(self, **kwargs):
        user_id = self.kwargs['user_id']

        suplemento_qs = Suplemento.objects.filter(user_id=user_id)

        return suplemento_qs


class DatosBiomedicosViewSet(viewsets.ModelViewSet):
    queryset = DatosBiomedicos.objects.all()
    serializer_class = DatosBiomedicosSerializer
