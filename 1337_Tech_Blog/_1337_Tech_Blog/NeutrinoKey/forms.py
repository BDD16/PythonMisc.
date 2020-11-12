from django import forms
from django.core.exceptions import ValidationError
from .models import NewsLink, Startup, Tag, Tasking
from datetime import datetime


class DownloadFileForm(forms.Form):
    url = forms.CharField(max_length=32)
