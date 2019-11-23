from django.db import models
from django.urls import reverse
from datetime import datetime

from .utils import UpdateView

# Create your models here.


class TaskingManager(models.Manager):

    def get_by_natural_key(self, slug):
        return self.get(slug=slug)


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True, help_text='A label for URL config.')


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('organizer_tag_detail', kwargs={'slug': self.slug})

class Tasking(models.Model):
    name = models.CharField(max_length=32,unique=True, db_index=True)
    slug = models.SlugField(max_length=32,unique=True, db_index=True)
    asignee = models.CharField(max_length=16, db_index=True)
    project_codename = models.CharField(default='SandStorm', max_length=32, db_index=True)
    description = models.TextField()
    assigned_date = models.DateTimeField('date assigned',unique=True, auto_now_add=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    is_complete = models.BooleanField(default=False)

    objects = TaskingManager()
    
    class Meta:
        ordering = ['name']
        get_latest_by = 'assigned_date'

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('organizer_tasking_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('organizer_tasking_update', kwargs={'slug': self.slug})

    def natural_key(self):
        return (self.slug,)


class Startup(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    slug = models.SlugField(max_length=32, unique=True, help_text='A label for URL config.')
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=64)
    tags = models.ManyToManyField(Tag)

    def __str(self):
        return self.name

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'

    def get_absolute_url(self):
        return reverse('organizer_startup_detail', kwargs={'slug', self.slug})

class NewsLink(models.Model):
    title= models.CharField(max_length=64)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=64)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)

    def __str__(self):
        return "{}:{}".format(self.startup, self.title)

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
