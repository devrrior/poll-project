from django.urls import path

from .views import PollCreateView, PollDeleteView, PollDetailView

app_name = 'poll'

urlpatterns = [
    path('dashboard/', PollCreateView.as_view(), name='dashboard'),
    path('<int:pk>/delete', PollDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit', PollDetailView.as_view(), name='edit'),
]

