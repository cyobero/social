from django.shortcuts import render, HttpResponse
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print("form is valid")
        else:
            print("form ain't valid")
            print(form.errors)
            print(form.non_field_errors)
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})
