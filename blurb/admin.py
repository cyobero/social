from django.contrib import admin
from .models import Blurb

# Register your models here.

@admin.register(Blurb)
class BlurbAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'body',)
    list_display = ('title', 'author', 'created', 'edited', 'slug',)
    list_filter = ('title', 'author', 'edited',)
