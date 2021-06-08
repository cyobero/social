from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import Blurb
from .forms import CreateBlurbForm

# Create your views here.
class BlurbDetailView(DetailView):
    context_object_name = 'blurb'
    template_name = 'blurb/blurb_detail.html'

    def get_queryset(self):
        blurb = Blurb.objects.filter(author__username=self.kwargs['username'],
                                     slug=self.kwargs['slug'])
        return blurb


class CreateBlurbView(CreateView):
    template_name = 'blurb/create_blurb.html'
    form_class = CreateBlurbForm

    def get_initial(self, *args, **kwargs):
        initial = super(CreateBlurbView, self).get_initial(*args, **kwargs)
        initial['author'] = self.request.user
        return initial
