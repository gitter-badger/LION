from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class HomeView(PermissionRequiredMixin, TemplateView):
    template_name = "activation/index.html"
    permission_required = 'user.is_staff'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'