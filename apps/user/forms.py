from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter a valid email address',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter password',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')  # store value of request
        self.user_cache = None  # store user
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, username=email, password=password
            )

            if self.user_cache is None:
                raise forms.ValidationError(
                    {
                        'email': [
                            'Email or password are incorrect',
                        ]
                    }
                )

        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class RegisterForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Repeat your password',
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
