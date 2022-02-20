from django.db import models

from apps.poll.models import Poll


class Question(models.Model):
    question = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)


class Answer(models.Model):
    answer = (models.CharField(max_length=100))
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

