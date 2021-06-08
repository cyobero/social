from django.db import models
from django.contrib.auth.models import User

from blurb.models import Blurb

# Create your models here.
class Comment(models.Model):
    blurb = models.ForeignKey(Blurb, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.blurb)
