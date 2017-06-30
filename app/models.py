from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Label(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField(default='')
    content = HTMLField(default='')
    short_description = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='static/img/labels', blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title
