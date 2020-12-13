'''
DBA 1337_TECH, AUSTIN TEXAS © MAY 2020
Proof of Concept code, No liabilities or warranties expressed or implied.
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    email = forms.CharField(max_length=32)
    pwd = forms.CharField(max_length=32, min_length=7)

    class Meta:
        model = User
        widgets = {
            'pwd': forms.PasswordInput(),
        }
        fields = ('email', 'pwd',)

    '''
    def save(self):
        new_user = User.objects._create_user(email=self.cleaned_data['user'], is_staff=False, is_superuser=False, password=self.pwd)

    '''

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def get_absolute_url(self):
        return reverse(
            'register_create',
            kwargs={'user': self.user,
                    })
