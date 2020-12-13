'''
DBA 1337_TECH, AUSTIN TEXAS © MAY 2020
Proof of Concept code, No liabilities or warranties expressed or implied.
'''
from django.core import exceptions
from django.db import ConnectionRouter, ConnectionHandler
from django.db.models import ForeignKey, QuerySet
from django.db import models

from django.urls import reverse, reverse_lazy
import _1337_Tech_Blog.settings as settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from _1337_Tech_Blog.organizer.models import Startup, Tag, Tasking, SecureNote, Librarian
from _1337_Tech_Blog.organizer.models import SecureNote

# Create your models here.
connections = ConnectionHandler()
router = ConnectionRouter()


class SpanningForeignKey(ForeignKey):

    def validate(self, value, model_instance):
        if self.remote_field.parent_link:
            return
        # Call the grandparent rather than the parent to skip validation
        super(ForeignKey, self).validate(value, model_instance)
        if value is None:
            return

        using = router.db_for_read(self.remote_field.model, instance=model_instance)
        qs = self.remote_field.model._default_manager.using(using).filter(
            **{self.remote_field.field_name: value}
        )

        qs = qs.complex_filter(self.get_limit_choices_to())
        if not qs.exists():
            raise exceptions.ValidationError(
                self.error_messages['invalid'],
                code='invalid',
                params={
                    'model': self.remote_field.model._meta.verbose_name,
                    'pk': value,
                    'field': self.remote_field.field_name, 'value': value,
                },  # 'pk' is included for backwards compatibility
            )


class PostQueryset(models.QuerySet):

    def published(self):
        return self.filter(
            pub_date__lte=date.today())


'''
Base Post Manager for unencrypted text model
input None
'''


class BasePostManager(models.Manager):

    def get_queryset(self):
        return (
            PostQueryset(
                self.model,
                using=self._db,
                hints=self._hints))
        # .select_related('author__username'))

    def get_by_natural_key(self, pub_date, slug):
        return self.get(
            pub_date=pub_date,
            slug=slug)


class SecurePostManager(models.Manager):

    def get_queryset(self):
        return PostQueryset(
            self.model,
            using=self._db,
            hints=self._hints)

    def get_by_natrual_key(self, pub_date, slug):
        return self.get(
            pub_date=pub_date,
            slug=slug)


PostManager = BasePostManager.from_queryset(
    PostQueryset)


class SecureDataAtRestPost(SecureNote):
    # title = models.CharField(max_length=64)
    # slug = models.SlugField(max_length=64, help_text='A label for URL config', unique_for_month='pub_date')
    author = models.ForeignKey(
        get_user_model(),
        related_name='secureblog_posts',
        on_delete=models.CASCADE,
        default=1)
    # pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='secureblog_posts')
    # startups = models.ManyToManyField(Startup, related_name='blog_posts')
    tasking = models.ManyToManyField(Tasking, related_name='securetasking')
    is_encrypted = models.BooleanField(default=True)

    objects = Librarian()

    class Meta:
        verbose_name = '[Secure] blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'
        permissions = (
            ("view_future_post",
             "Can view unpublished Post"),
            ("add_tasking",
             "Can add task"),
        )

    def __str__(self):
        return "{} on {}".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse(
            'blog_securepost_detail',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})

    def get_archive_month_url(self):
        return reverse(
            'blog_securepost_archive_month',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month})

    def get_archive_year_url(self):
        return reverse(
            'blog_securepost_archive_year',
            kwargs={'year': self.pub_date.year})

    def get_delete_url(self):
        return reverse(
            'blog_securepost_delete',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})

    def get_update_url(self):
        return reverse(
            'blog_securepost_update',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})

    def natural_key(self):
        return (
            self.pub_date,
            self.slug)

    natural_key.dependencies = [
        # 'organizer.startup',
        # 'NeutrinoKey.DEK',
        # 'NeutrinoKey.KEK',
        # 'organizer.tag',
        'user.user',
    ]

    def formatted_title(self):
        return self.title.title()

    def short_text(self):
        if len(self.text) > 20:
            short = ' '.join(self.text.split()[:20])
            short += ' ...'
        else:
            short = self.text
        return short


'''
class Post of models.Model type class extension.  includes title, slug, author, text, pub_date, tags, and tasking
'''


class Post(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, help_text='A label for URL config', unique_for_month='pub_date')
    author = SpanningForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='blog_posts',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        unique=False
    )
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    # startups = models.ManyToManyField(Startup, related_name='blog_posts')
    tasking = models.ManyToManyField(Tasking, related_name='tasking')

    objects = PostManager()

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

    def __str__(self):
        return "{} on {}".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse(
            'blog_post_detail',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})

    def get_archive_month_url(self):
        return reverse(
            'blog_post_archive_month',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month})

    def get_archive_year_url(self):
        return reverse(
            'blog_post_archive_year',
            kwargs={'year': self.pub_date.year})

    def get_delete_url(self):
        return reverse(
            'blog_post_delete',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})

    def get_update_url(self):
        return reverse(
            'blog_post_update',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})

    def natural_key(self):
        return (
            self.pub_date,
            self.slug)

    natural_key.dependencies = [
        # 'organizer.startup',
        'organizer.tag',
        'user.user',
    ]

    def formatted_title(self):
        return self.title.title()

    def short_text(self):
        if len(self.text) > 20:
            short = ' '.join(self.text.split()[:20])
            short += ' ...'
        else:
            short = self.text
        return short

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)
