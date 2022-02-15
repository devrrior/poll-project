from django.urls import path
from apps.users.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
