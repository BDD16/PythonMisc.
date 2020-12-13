'''
DBA 1337_TECH, AUSTIN TEXAS © MAY 2020
Proof of Concept code, No liabilities or warranties expressed or implied.
'''


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from _1337_Tech_Blog.superhero.utils import CreateView
from _1337_Tech_Blog.superhero.models import User
from _1337_Tech_Blog.superhero.forms import RegisterForm
from django.contrib.auth.decorators import permission_required
from django.urls import reverse, reverse_lazy
from .decorators import require_authenticated_permission
from _1337_Tech_Blog.superhero.utils import RegisterMixin

# Create your views here.
@require_authenticated_permission(
    'Blog.add_post')
class RegisterCreate(CreateView, RegisterMixin):
    form_class = RegisterForm
    model = User
    template_name = 'superhero/registration_form.html'
    success_url = 'superhero/registersuccess.html'

    #@method_decorator(login_required)
    #@method_decorator(permission_required('organizer.view_tasking',login_url='/login/', raise_exception=True))
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
