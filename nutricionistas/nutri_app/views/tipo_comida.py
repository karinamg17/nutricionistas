# -*- coding: utf-8 -*-
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import Group
from django.db.models import fields
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from nutricionistas.nutri_app.forms.users_form import (
    UserEditForm,
    UserForm,
    UserPasswdForm,
)
from nutricionistas.nutri_app.models import TipoComida


class TipoComidaListView(GroupRequiredMixin, ListView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = TipoComida
    paginate_by = 25

    template_name = 'nutri_app/menu/tipo_comida/tipo_comida_list.html'

    def get_context_data(self, **kwargs):
        context = super(TipoComidaListView, self).get_context_data(**kwargs)

        return context


class TipoComidaCreateView(GroupRequiredMixin, CreateView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = TipoComida
    # form_class = Form
    fields = ['descripcion', 'kcal', 'observaciones']
    success_url = 'nutri_app:users_list'
    template_name = 'nutri_app/menu/tipo_comida/tipo_comida_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('El tipo de comida ha sido creado satisfactoriamente'))
        return reverse('nutri_app:tipo_comida_list')

    def get_context_data(self, **kwargs):
        context = super(TipoComidaCreateView, self).get_context_data(**kwargs)

        return context


class TipoComidaDetailView(GroupRequiredMixin, DetailView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = TipoComida
    template_name = 'nutri_app/menu/tipo_comida/tipo_comida_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TipoComidaDetailView, self).get_context_data(**kwargs)
        return context


class TipoComidaUpdateView(GroupRequiredMixin, UpdateView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = TipoComida
    fields = ['descripcion', 'kcal', 'observaciones']
   
    template_name = 'nutri_app/menu/tipo_comida/tipo_comida_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('El tipo de comida ha sido actualizado'))
        return reverse('nutri_app:tipo_comida_list')

    def get_context_data(self, **kwargs):
        context = super(TipoComidaUpdateView, self).get_context_data(**kwargs)

        return context


class TipoComidaDeleteView(GroupRequiredMixin, DeleteView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = TipoComida

    template_name = 'nutri_app/menu/tipo_comida/tipo_comida_confirm_delete.html'

    # send the user back to their own page after a successful update
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('El tipo de comida ha sido eliminado'))
        return reverse('nutri_app:tipo_comida_list')

    def get_context_data(self, **kwargs):
        context = super(TipoComidaDeleteView, self).get_context_data(**kwargs)

        return context
