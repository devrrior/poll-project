from django import forms

from .models import Poll


class PollCreateForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('name',)

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}
