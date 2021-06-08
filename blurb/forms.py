from django import forms
from .models import Blurb

class CreateBlurbForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateBlurbForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget = forms.HiddenInput()

    class Meta:
        model = Blurb
        fields = ('title', 'body', 'author',)
