from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from .models import Comment

@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blurb', 'created',)
    ordering = ('-created', 'blurb', 'author',)
