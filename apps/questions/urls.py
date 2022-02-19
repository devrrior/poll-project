from django.urls import path

from apps.questions.views import QuestionCreateView

app_name = 'questions'
urlpatterns = [path('new/', QuestionCreateView.as_view(), name='new')]
