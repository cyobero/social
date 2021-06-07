from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import UserLoginForm, UserProfileCreationForm
from .models import UserProfile
# Create your views here.
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
    user = request.user
    return render(request, 'account/dashboard.html', {'user': user})


def user_register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'account/register_success.html')
    else:
        form = UserProfileCreationForm()
    return render(request, 'account/register.html', {'form': form})

@login_required
def user_profile(request, username):
    user_profile = get_object_or_404(UserProfile, username=username)
    return render(request, 'account/profile.html', {'user_profile': user_profile})
