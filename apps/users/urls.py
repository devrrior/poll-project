from django.urls import path
from apps.users.views import HomeView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', HomeView.as_view(), name='home')
]
