from django.contrib.auth import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .models import Tag, Tasking
from django.shortcuts import (get_object_or_404, redirect, render)
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from .forms import TagForm, TaskingForm, UploadFileForm
from django.views.generic import (ArchiveIndexView, CreateView, DetailView, ListView, MonthArchiveView, View, YearArchiveView)
from _1337_Tech_Blog.core.utils import UpdateView
from _1337_Tech_Blog.NeutrinoKey.decorators import custom_login_required
from .utils import CreateView
from _1337_Tech_Blog.superhero.decorators import require_authenticated_permission
from _1337_Tech_Blog.organizer import cryptoutils
from .forms import TaskingForm
from .utils import UpdateView
# Create your views here.
def homepage(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'organizer/tag_detail.html', {'tag': tag})

def tasking_detail(request, slug):
    tasking = get_object_or_404(Tasking, slug__iexact=slug)
    return render(request, 'organizer/tasking_detail.html', {'tasking': tasking})


def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})

class TagList(ListView):
    model = Tag
    template_name = 'organizer/tag_list.html'


    #@method_decorator(permission_required('organizer.view_tag', raise_exception=True))
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

def redirect_root(request):
    url_path = reverse('blog_post_list')
    return HttpResponseRedirect(url_path)

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
        else:
            return render(request, 'organizer/tag_form.html', {'form': form})
    else:
        form = TagForm()
    return render(request, 'organizer/tag_form.html', {'form': form})

def tasking_create(request):
    if request.method == 'POST':
        form = TaskingForm(request.POST)
        print("before forms.isvalid()")
        print(form)
        print("\n\n")
        if form.is_valid():
            print(form)
            new_tasking = form.save()
            return redirect(new_tasking)
        else:
            return render(request, 'organizer/tasking_form.html', {'form':form})
    else:
        form = TaskingForm()
    return render(request, 'organizer/tasking_form.html', {'form': form})

def in_contrib_group(user):
    if user.groups.filter(name='contributors').exists():
        return True
    else:
        raise PermissionDenied


@require_authenticated_permission('organizer.view_tasking')
class TaskingList(ListView):
    model = Tasking
    template_name = 'organizer/tasking_list.html'

    @method_decorator(permission_required('organizer.view_tasking',login_url='/login/', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class TagCreate(CreateView):
    form_class = TagForm
    model = Tag
    template_name = 'organizer/tag_form.html'

    @method_decorator(login_required)
    @method_decorator(permission_required('organizer.add_tag', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

@require_authenticated_permission('organizer.add_tasking')
class TaskingCreate(CreateView):
    form_class = TaskingForm
    model = Tasking
    template_name = 'organizer/tasking_form.html'

    #@method_decorator(login_required)
    @method_decorator(permission_required('organizer.view_tasking',login_url='/login/', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

@require_authenticated_permission('organizer.add_tasking')
class TaskingUpdate(UpdateView):
    form_class = TaskingForm
    model = Tasking

class TagUpdate( UpdateView):
    form_class = TagForm
    model = Tag
    template_name_suffix = '_form_update'

    @method_decorator(login_required)
    @method_decorator(permission_required('organizer.add_tag', raise_exception=True))
    @method_decorator(custom_login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UploadFile(CreateView):
    form_class = UploadFileForm
    template_name = 'organizer/upload.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        file = request.FILES.getlist('file_field')
        if form.isValid():
            for f in files:
                ####generate AES-KEY pwd protect with password
                ####TODO: Encrypt
                pass
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
'''
def handle_uploaded_file(f):
    with open('./tmp/' + f, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk):

'''
