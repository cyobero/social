from django import forms
from .models import Blurb

class CreateBlurbForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateBlurbForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
        self.fields['author'].widget = forms.HiddenInput()

    class Meta:
        model = Blurb
        fields = ('title', 'body', 'author',)
