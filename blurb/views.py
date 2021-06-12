from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Blurb
from .forms import CreateBlurbForm
from comment.models import Comment
from comment.forms import CommentForm
from friendship.models import Friend

# Create your views here.
# class BlurbDetailView(DetailView):
    # context_object_name = 'blurb'
    # template_name = 'blurb/blurb_detail.html'

    # def get_queryset(self):
        # blurb = Blurb.objects.filter(author__username=self.kwargs['username'],
                                     # slug=self.kwargs['slug'])
        # return blurb



def blurb_detail(request, username, slug):
    blurb = get_object_or_404(Blurb, author__username=username,
                              slug=slug)
    # Get comments for this blurb.
    comments = blurb.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data.get('body')
            author = request.user
            Comment(blurb=blurb, body=body, author=author).save()
    else:
        form = CommentForm()
    return render(request, 'blurb/blurb_detail.html', {'blurb': blurb,
                                            'form': form,
                                            'comments': comments})


@login_required(login_url='user_login')
def blurbs_feed(request):
    user = request.user
    friends = Friend.objects.friends(user)
    blurbs = [Blurb.objects.filter(Blurb, author=friend) for friend in friends]
    return render(request, 'blurb/blurbs_feed.html', {'blurbs': blurbs})


class CreateBlurbView(CreateView):
    template_name = 'blurb/create_blurb.html'
    form_class = CreateBlurbForm

    def get_initial(self, *args, **kwargs):
        initial = super(CreateBlurbView, self).get_initial(*args, **kwargs)
        initial['author'] = self.request.user
        return initial
