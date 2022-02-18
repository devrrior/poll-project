from django.urls import path
from apps.users.views import HomeView

app_name = 'users'

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
