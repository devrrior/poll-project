from django.urls import path

from apps.polls.views import PollCreateView, PollDeleteView

app_name = 'polls'

urlpatterns = [
    path('dashboard/', PollCreateView.as_view(), name='dashboard'),
    path('<int:pk>/delete', PollDeleteView.as_view(), name='delete'),
]
