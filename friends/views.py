from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from friendship.models import Friend


@login_required
def friend_requests(request):
    friend_requests = Friend.objects.requests(request.user)
    return render(request, 'friends/requests.html', {'friend_requests': friend_requests})
