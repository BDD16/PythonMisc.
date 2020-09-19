from django.conf.urls import url

from .views import homepage, tag_detail, tag_list, tag_create, tasking_create, tasking_detail, TagCreate, TaskingCreate, UploadFile, TaskingList, TagList, TaskingUpdate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(TagList.as_view()), name='organizer_tag_list'),
    url(r'^tag/create/$', login_required(TagCreate.as_view()), name='organizer_tag_create'),
    url(r'^tasking/create/$', login_required(TaskingCreate.as_view()), name='organizer_tasking_create'),
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    url(r'^create/$', login_required(TagCreate.as_view()), name='organizer_tag_create'),
    url(r'^upload/create/$', login_required(UploadFile.as_view()), name='organizer_upload_create'),
    url(r'^tasking/(?P<slug>[\w\-]+)/update/$', TaskingUpdate.as_view(),name='organizer_tasking_update'),
    url(r'^tasking/(?P<slug>[\w\-]+)/$', tasking_detail, name='organizer_tasking_detail'),
    url(r'^tasking/$', login_required(TaskingList.as_view()), name='organizer_tasking_list'),
    ]
