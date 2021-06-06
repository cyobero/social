from django.shortcuts import render, get_object_or_404
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

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
