from django.db import models
from _1337_Tech_Blog.organizer.models import Startup, Tag, Tasking
from django.urls import reverse, reverse_lazy

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, help_text='A label for URL config', unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')
    tasking = models.ManyToManyField(Tasking, related_name='tasking')

    def __str__(self):
        return "{} on {}".format(self.title, self.pub_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'year': self.pub_date.year, 'month': self.pub_date.strftime('%b').lower(),
                                                  'day': self.pub_date.day, 'slug': self.slug})

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'
        permissions = (
            ("view_future_post",
            "Can view unpublished Post"),
            ("add_tasking",
             "Can add task"),
            )