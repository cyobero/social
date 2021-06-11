from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from friendship.models import Friend, FriendshipRequest
from friendship.exceptions import AlreadyFriendsError, AlreadyExistsError


@login_required(login_url='user_login')
def friend_accept(request):
    """Accept friend request."""
    if request.method == 'POST':
        f_request_id = request.POST.get('f_request_id')
        try:
            friend_request = get_object_or_404(FriendshipRequest, id=f_request_id)
            friend_request.accept()
            messages.success(request, "You are now friends!")
        except AlreadyFriendsError:
            messages.error(request, "You are already friends!")
    return redirect('friend_requests')


@login_required(login_url='user_login')
def friend_reject(request):
    """Reject friend request."""
    if request.method == 'POST':
        f_request_id = request.POST.get('f_request_id')
        try:
            friend_request = get_object_or_404(FriendshipRequest, id=f_request_id)
            friend_request.reject()
            messages.success(request, "You rejected %s's friend request." % friend_request.from_user.username)
        except AlreadyFriendsError:
            messages.error(request, "You are already friends!")
    return redirect('friend_requests')


@login_required(login_url='user_login')
def friend_requests(request):
    friend_requests = Friend.objects.requests(request.user)
    return render(request, 'friends/requests.html', {'friend_requests': friend_requests})
