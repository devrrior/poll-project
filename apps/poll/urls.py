from django.urls import path

from .views import PollCreateView, PollDeleteView, PollDetailView, PollPublishView

app_name = 'poll'

urlpatterns = [
    path('dashboard/', PollCreateView.as_view(), name='dashboard'),
    path('<int:pk>/delete', PollDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit', PollDetailView.as_view(), name='edit'),
    path('<int:pk>/publish', PollPublishView.as_view(), name='publish'),
]

