from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
import _1337_Tech_Blog.settings as settings

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='dj-auth:login', permanent=False)),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='superhero/logged_out.html',
    extra_context={'form': AuthenticationForm}),
    name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='superhero/login.html'), name='login'),
    
]
