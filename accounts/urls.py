from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    url(r'^create/$', views.SignUpView.as_view(), name='create'),
    #url(r'^check/(?P<pk>[0-9]+)/$', views.CheckView.as_view(), name='check'),
    #url(r'^update/(?P<pk>[0-9]+)/$', views.CorrectView.as_view(), name='update'),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),
    url(r'^profile/$', views.LoginSuccessView.as_view(), name='loginSuccess'),
    url(r'^person/$', views.PersonView.as_view(), name='person')
]