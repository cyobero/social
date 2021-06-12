from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from friendship.models import Friend


# Create your models here.
class Blurb(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-edited',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blurb, self).save(*args, **kwargs)

    def get_absolute_url(self):
        author = self.author.username
        slug = self.slug
        return '/blurb/{}/{}'.format(author, slug)
