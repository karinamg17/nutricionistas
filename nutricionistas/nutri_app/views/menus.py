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
from nutricionistas.nutri_app.models import MenuLine, TipoComida, Menu


class MenuListView(GroupRequiredMixin, ListView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = Menu
    paginate_by = 25

    template_name = 'nutri_app/menu/menu_list.html'

    def get_context_data(self, **kwargs):
        context = super(MenuListView, self).get_context_data(**kwargs)

        return context


class MenuCreateView(GroupRequiredMixin, CreateView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = Menu
    # form_class = Form
    fields = ['nombre_menu']
    success_url = 'nutri_app:menu_list'
    template_name = 'nutri_app/menu/menu_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('El menú ha sido creado satisfactoriamente'))
        return reverse('nutri_app:tipo_menu_list')

    def get_context_data(self, **kwargs):
        context = super(MenuCreateView, self).get_context_data(**kwargs)

        return context


class MenuUpdateView(GroupRequiredMixin, UpdateView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = Menu
    fields = ['nombre_menu']

    template_name = 'nutri_app/menu/menu_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('El menu ha sido actualizado'))
        return reverse('nutri_app:menu_list')

    def get_context_data(self, **kwargs):
        context = super(MenuUpdateView, self).get_context_data(**kwargs)

        return context


class MenuDeleteView(GroupRequiredMixin, DeleteView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = Menu

    template_name = 'nutri_app/menu/menu_confirm_delete.html'

    # send the user back to their own page after a successful update
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('El tipo de comida ha sido eliminado'))
        return reverse('nutri_app:menu_list')

    def get_context_data(self, **kwargs):
        context = super(MenuDeleteView, self).get_context_data(**kwargs)

        return context


class MenuDetailView(GroupRequiredMixin, DetailView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = Menu
    template_name = 'nutri_app/menu/menu_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MenuDetailView, self).get_context_data(**kwargs)
        return context

    def get_context_data(self, **kwargs):
        context = super(MenuDetailView, self).get_context_data(**kwargs)

        context['menu_line'] = MenuLine.objects.filter(menu_id=self.kwargs['pk'])
        context['menu_id'] = self.kwargs['pk']

        return context


class MenuLineCreateView(GroupRequiredMixin, CreateView):

    # required
    group_required = [u"Admin", u"SuperAdmin"]
    raise_exception = True

    model = MenuLine
    template_name = 'nutri_app/menu/menu_line/menu_line_form.html'

    fields = ['comida', 'tipo_comida']

    def get_context_data(self, **kwargs):
        context = super(MenuLineCreateView, self).get_context_data(**kwargs)
        context['menu_id'] = self.kwargs['menu_id']

        menu = Menu.objects.get(pk=self.kwargs['menu_id'])

        context['menu'] = menu

        return context

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.menu_id = self.kwargs['menu_id']
        self.object.save()

        return super(MenuLineCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'La comida ha sido agregado al menú satisfactoriamente')
        return reverse('nutri_app:menu_detail', kwargs={"pk": self.kwargs['menu_id']})


class MenuLineUpdateView(GroupRequiredMixin, UpdateView):

    # required
    group_required = [u"Admin", u"SuperAdmin"]
    raise_exception = True

    model = MenuLine
    template_name = 'nutri_app/menu/menu_line/menu_line_form.html'

    fields = ['comida', 'tipo_comida']

    def get_context_data(self, **kwargs):
        context = super(MenuLineUpdateView, self).get_context_data(**kwargs)
        context['menu_id'] = self.kwargs['menu_id']
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'El tipo de comida ha sido actualizado')
        return reverse('nutri_app:menu_detail', kwargs={"pk": self.kwargs['menu_id']})


class MenuLineDeleteView(GroupRequiredMixin, DeleteView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = MenuLine

    template_name = 'nutri_app/menu/menu_line/menu_line_confirm_delete.html'

    # send the user back to their own page after a successful update
    def get_success_url(self, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'El tipo de comida ha sido eliminado')
        return reverse('nutri_app:menu_detail', kwargs={"pk": self.kwargs['menu_id']})

    def get_context_data(self, **kwargs):
        context = super(MenuLineDeleteView, self).get_context_data(**kwargs)
        context['menu'] = Menu.objects.get(pk=self.kwargs['menu_id'])

        return context