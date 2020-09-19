from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic import (ArchiveIndexView, CreateView, DeleteView, DetailView, MonthArchiveView, View, YearArchiveView)
from _1337_Tech_Blog.core.utils import UpdateView
from .models import Post
from .forms import PostForm
from django.urls import reverse, reverse_lazy

from .utils import PostGetMixin
# Create your views here.

def greeting(request):
    return HttpResponse('Welcome to 1337_Tech Blog')


@require_http_methods(['HEAD', 'GET'])
def post_detail(request, year, month, slug, parent_template=None):
    post = get_object_or_404(
        Post, pub_date__year=year,
        pub_date__month=month,
        slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post, 'parent_template': parent_template})

def post_list(request):
    return render(request, 'blog/post_list.html', {'post_list': Post.objects.all(), 'parent_template': parent_template})


class PostList(View):
    template_name = 'blog/post_list.html'
    def get(self, request):
        return render(request, self.template_name, {'post_list': Post.objects.all()})


class PostDetail(PostGetMixin, DetailView):
    model = Post

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post

class PostDelete(PostGetMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog_post_list')