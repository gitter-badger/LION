from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.urls import reverse
from accounts.models import User 
from accounts.forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(TemplateView):
    template_name = "accounts/index.html"

class SignUpView(CreateView):
    model = User
    form_class = UserForm
    template_name = "accounts/create.html"

    def get_success_url(self):
        u = self.object
        u.set_password(u.rawpassword)
        u.save()
        return reverse('accounts:check', kwargs={'pk' : self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(SignUpView, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs 

class CheckView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/check.html"

class CorrectView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "accounts/create.html"
    def get_success_url(self):
        return reverse('accounts:check', kwargs={'pk' : self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CorrectView, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs 

class SuccessView(TemplateView):
    template_name = "accounts/success.html"

class LoginSuccessView(TemplateView):
    template_name = 'accounts/loginsuccess.html'

class PersonView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/person.html'