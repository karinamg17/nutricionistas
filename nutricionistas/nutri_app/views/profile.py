
from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, UpdateView

from nutricionistas.users.models import User


class UserPerfilDetailView(LoginRequiredMixin, DetailView):

    model = User
    template_name = 'nutri_app/profile/perfil_detail.html'

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def get_context_data(self, **kwargs):

        context = super(UserPerfilDetailView, self).get_context_data(**kwargs)

        return context


class UserPerfilUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = [
        'first_name', 'last_name', 'nro_telefono',  'nro_telefono',
        'sexo', 'fecha_nacimiento']

    template_name = 'nutri_app/profile/perfil_form.html'
    success_url = reverse_lazy('nutri_app:user_profile_detail')

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.save()

        messages.add_message(self.request, messages.SUCCESS, 'Se ha actualizado el perfil')

        super(UserPerfilUpdateView, self).form_valid(form)

        return redirect(self.success_url)


class UserPhotolUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ['foto_usuario']
    template_name = 'nutri_app/profile/perfil_form.html'
    success_url = reverse_lazy('nutri_app:user_profile_detail')

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        messages.add_message(self.request, messages.SUCCESS, 'Se ha actualizado la foto')

        super(UserPhotolUpdateView, self).form_valid(form)

        return redirect(self.success_url)
