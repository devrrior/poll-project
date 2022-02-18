import uuid
from django.db import models


class Answer(models.Model):
    votes = models.IntegerField(default=0)


class Question(models.Model):
    question = models.CharField(max_length=255)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Poll(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(default=str(uuid.uuid4())[:8], editable=False, max_length=8)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
