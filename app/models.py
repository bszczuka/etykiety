from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Label(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField(default=slugify(''))
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title
