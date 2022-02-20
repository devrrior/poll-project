from django.urls import path

from .views import QuestionCreateView, QuestionEditView

app_name = 'question'
urlpatterns = [
    path('new/', QuestionCreateView.as_view(), name='new'),
    path('<int:pk>/edit', QuestionEditView.as_view(), name='edit'),
]
