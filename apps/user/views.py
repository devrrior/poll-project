from django.contrib import messages
from django.contrib.auth import login
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView

from .forms import LoginForm, RegisterForm
from .models import User


class LoginView(FormView):
    """
    A view where the user can login
    """
    template_name = 'user/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('poll:dashboard')

    # Pass request for validate my user
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    # If the user is authenticated, then redirect to home page
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class SignUpView(CreateView):
    """
    A view where the user can create a account
    """
    model = User
    form_class = RegisterForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        return self.success_url

    # If the user is authenticated, then redirect to home page
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Account Created successfully')
        return super().form_valid(form)


class HomeView(TemplateView):
    template_name = 'user/home.html'

