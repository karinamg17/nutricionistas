# -*- coding: utf-8 -*-
import datetime
from datetime import date
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
from rest_framework import generics, mixins, viewsets

from nutricionistas.nutri_app.models import Cita
from nutricionistas.nutri_app.serializers import CitaCalSerializer, CitaSerializer, UserSerializer
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

    template_name = 'nutri_app/nutricionista/pacientes_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PacientesDetailView, self).get_context_data(**kwargs)

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

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')

        cita_qs = Cita.objects.filter(user_id=1)

        return cita_qs
