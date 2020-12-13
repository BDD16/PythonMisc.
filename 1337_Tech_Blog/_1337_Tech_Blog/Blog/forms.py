'''
DBA 1337_TECH, AUSTIN TEXAS © MAY 2020
Proof of Concept code, No liabilities or warranties expressed or implied.
'''

from django import forms
from django.contrib.auth import get_user
from django.db import IntegrityError, connections

from django.db import models
from django.db.models import QuerySet

from .models import Post, SecureDataAtRestPost, SpanningForeignKey
from _1337_Tech_Blog.organizer.models import SecureNote
from _1337_Tech_Blog.NeutrinoKey.models import DEK, KEK


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()

    def save(self, request, commit=True):
        post = super().save(commit=False)
        # if not post.pk:
        # post.author = get_user(request)
        if commit:
            post.author = post.author.id
            print(post.author_id())
            with connections['superHeros'].cursor():
                post.save()
            self.save_m2m()
        return post


class SecurePostForm(forms.ModelForm):
    class Meta:
        model = SecureDataAtRestPost
        fields = '__all__'

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()

    def save(self, request, commit=True):
        self.fields['author'].queryset = QuerySet(using='superHeros')
        post = super().save(commit=False)
        if not post.pk:
            post.author = get_user(request)
        if commit:
            # print(post)
            print("PK" + str(self.instance.pk))
            if self.instance.pk != None:
                x = self.instance.pk
                print("about to edit the secure note")
                post = post.__class__.objects._encrypt_update_Secure_Note(password=request.user.password,
                                                                          secure_text=post.secure_text, postobj=post,
                                                                          request=request)
                print("We just Edited the Secure Note")
            else:
                post = post.__class__.objects._encrypt_Secure_Note(password=request.user.password,
                                                                   secure_text=post.secure_text, postobj=post,
                                                                   request=request)

            # post.save_m2m()
            print(dir(post))
            print("REQUEST")
            print(dir(request))
            # self.save(request=request,commit=False)
            # self.data_dek = post.data_dek
            # self.data_kek = post.data_kek
            # self.save(request=request,commit=False)
            # self.save_m2m()
        return post
