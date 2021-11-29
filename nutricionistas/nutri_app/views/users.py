# -*- coding: utf-8 -*-
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import Group
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
from nutricionistas.users.models import User
from nutricionistas.users.filters import UserFilter


class UserListView(GroupRequiredMixin, ListView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = User
    paginate_by = 25
    
    template_name = 'nutri_app/users/users_list.html'

    page = {
        'title': _('User'),
        'subtitle': _('List')
    }

    def get_queryset(self):
        qs = self.model.objects.all()
        self.users_filtered_list = UserFilter(self.request.GET, queryset=qs)
        return self.users_filtered_list.qs

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['page'] = self.page

        context['filter'] = self.users_filtered_list

        return context


class UserCreateView(GroupRequiredMixin, CreateView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = User
    form_class = UserForm
    success_url = 'nutri_app:users_list'
    template_name = 'nutri_app/users/user_form.html'

    page = {
        'title': _('User'),
        'subtitle': _('Add')
    }

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page

        return context

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data['password1'])
        self.object.username = form.cleaned_data['username']
        self.object.email = form.cleaned_data['username']
        self.object.save()
        #self.object.groups.add(Group.objects.get(name='Usuarios'))
        self.object.save()

        messages.add_message(self.request,
                             messages.SUCCESS, _('The user was created successfully'))

        super(UserCreateView, self).form_valid(form)

        return redirect(self.success_url)


class UserDetailView(GroupRequiredMixin, DetailView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = User
    template_name = 'nutri_app/users/user_detail.html'

    page = {
        'title': _('User'),
        'subtitle': _('Detail')
    }

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class UserUpdateView(GroupRequiredMixin, UpdateView):

    # required
    group_required = u"Administrador"
    raise_exception = True

    model = User
    form_class = UserEditForm
    success_url = 'nutri_app:users_list'
    template_name = 'nutri_app/users/user_form.html'

    page = {
        'title': _('User'),
        'subtitle': _('Update')
    }

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        
        context['page'] = self.page

        return context

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.save()

        messages.add_message(self.request, messages.SUCCESS, _('Los datos del usuario ha sido actualizado'))

        super(UserUpdateView, self).form_valid(form)

        return redirect(self.success_url)


class UserUpdatePasswdView(GroupRequiredMixin, UpdateView):

    # required
    group_required = u"SuperAdmin"
    raise_exception = True

    model = User
    form_class = UserPasswdForm
    success_url = 'nutri_app:users_list'
    template_name = 'nutri_app/users/user_form.html'

    def get_context_data(self, **kwargs):
        context = super(UserUpdatePasswdView, self).get_context_data(**kwargs)
        context['page'] = {
            'title': _('User'),
            'subtitle': _('password change'),
        }

        return context

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data['password1'])
        self.object.save()

        messages.add_message(self.request,
                             messages.SUCCESS, _('La contraseña ha sido actualizada'))

        super(UserUpdatePasswdView, self).form_valid(form)

        return redirect(self.success_url)


class UserDelete(GroupRequiredMixin, DeleteView):

    # required
    group_required = u"SuperAdmin"
    raise_exception = True

    model = User

    template_name = 'nutri_app/users/user_confirm_delete.html'

    page = {
        'title': _('User'),
        'subtitle': _('delete')
    }

    # send the user back to their own page after a successful update
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('El usuario ha sido eliminado'))
        return reverse('nutri_app:users_list')


    def get_context_data(self, **kwargs):
        context = super(UserDelete, self).get_context_data(**kwargs)
        context['page'] = self.page

        return context
