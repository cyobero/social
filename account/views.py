from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import UpdateView
from django.views.generic.edit import UpdateView
from django.core.exceptions import PermissionDenied

from .forms import UserLoginForm, UserProfileCreationForm, UpdateProfileForm
from blurb.models import Blurb
from .models import UserProfile
from friendship.models import Friend, FriendshipRequest
from friendship.exceptions import AlreadyFriendsError, AlreadyExistsError


# Create your views here.
class ProfileUpdateView(UpdateView):
    template_name = 'account/edit_profile.html'
    model = UserProfile
    form_class = UpdateProfileForm

    def get_success_url(self):
        username = self.request.user.username
        return '/account/profile/{}'.format(username)

    def get_object(self, *args, **kwargs):
        obj = super(ProfileUpdateView, self).get_object(*args, **kwargs)
        if obj.pk != self.request.user.pk:
            raise PermissionDenied()
        return obj


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'account/login_success.html')
                else:
                    messages.error(request, 'This account is no longer active.')
                    return render(request, 'account/login.html', {'form': form})
            else:
                messages.error(request, 'Invalid login credentials.')
                return render(request, 'account/login.html', {'form': form})
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'account/logged_out.html')


@login_required(login_url='user_login')
def dashboard(request):
    user = get_object_or_404(UserProfile, instance=request.user)
    return render(request, 'account/dashboard.html', {'user': user})


def user_register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'account/register_success.html')
    else:
        form = UserProfileCreationForm()
    return render(request, 'account/register.html', {'form': form})


def user_profile(request, username):
    context = {
        'user_profile': get_object_or_404(UserProfile, username=username),
        'blurbs': Blurb.objects.filter(author__username=username),
        'f_requests': FriendshipRequest.objects.filter(to_user=request.user),
    }
    context['friends'] = context['user_profile'].get_friends_profiles()
    # Add friend
    if request.method == 'POST':
        to_user = get_object_or_404(User, username=username)
        from_user = request.user
        try:
            Friend.objects.add_friend(from_user, to_user)
            messages.success(request, "Sent {} a friend request".format(to_user.username))
        except AlreadyFriendsError:
            messages.error(request, 'You are already friends with {}'.format(username))
        except AlreadyExistsError:
            messages.error(
                request, 'A friend request has already been sent and is pending.')

    return render(request, 'account/profile.html', context)
