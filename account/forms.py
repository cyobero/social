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
    def __init__(self, *args, **kwargs):
        super(UserProfileCreationForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password1', 'password2', 'gender',)


class UpdateProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
        self.fields['birthday'].widget.attrs.update({
            'class': 'form-control',
            'id': 'datepicker',
        })

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'birthday', 'gender',
                  'profile_pic', 'occupation', 'education', 'hobbies',)
