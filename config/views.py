# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from django.db.models import Count, Sum
from django.views.generic import TemplateView


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        return context
