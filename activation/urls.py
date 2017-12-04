from django.conf.urls import url, include
from activation import views
from django.contrib.auth.views import LoginView

app_name = 'activation'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
]