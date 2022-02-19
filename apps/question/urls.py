from django.urls import path

from .views import QuestionCreateView

app_name = 'question'
urlpatterns = [path('new/', QuestionCreateView.as_view(), name='new')]
