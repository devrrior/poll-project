from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-lg',}))
    password = forms.CharField(
        widget=forms.PasswordInput(
           attrs={'class': 'form-control form-control-lg',}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request") # store value of request 
        self.user_cache = None # store user
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, username=email, password=password)

            if self.user_cache is None:
                raise forms.ValidationError({'email': ["Email or password are incorrect",]})

        return self.cleaned_data

    def get_user(self):
        return self.user_cache
