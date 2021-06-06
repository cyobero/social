from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=255,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=255,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserProfileCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2', 'gender', 'profile_pic',)
