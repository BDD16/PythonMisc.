# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .forms import DownloadFileForm
from django.views.generic import (ArchiveIndexView, CreateView, DetailView, ListView, MonthArchiveView, View, YearArchiveView)
# Create your views here.
class DownloadFile(ListView):
    form_class = DownloadFileForm
    template_name = 'organizer/download.html'

    @method_decorator(permission_required('NeutrinoKey.view_download',login_url='/login/', raise_exception=True))
    @require_authenticated_permission('NeutrinoKey.can_download')
    def download(self, request, *args, **kwargs):
        if form.isValid():
            filename = os.path.basename(self.url)
            r = requests.get(self.url, stream=True)
            response['Content-Disposition'] = f'attachment; filename={filename}'
            return response
        if form.isValid():
            for f in files:
                ####generate AES-KEY pwd protect with password
                ####TODO: Encrypt
                pass
            return self.form_valid(form)
        else:
            return self.form_invalid(form)