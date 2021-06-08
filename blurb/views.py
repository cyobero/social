from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import Blurb
# Create your views here.


class BlurbDetailView(DetailView):
    context_object_name = 'blurb'
    template_name = 'blurb/blurb_detail.html'

    def get_queryset(self):
        blurb = Blurb.objects.filter(author__username=self.kwargs['username'],
                                     slug=self.kwargs['slug'])
        return blurb
