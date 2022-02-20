import uuid
from django.db import models

from apps.user.models import User


class Poll(models.Model):
    STATUS_CHOICES = [
        ('published','Published'),
        ('draft', 'Draft'),
    ]

    name = models.CharField(max_length=100)
    code = models.CharField(default=str(uuid.uuid4())[:8], editable=False, max_length=8)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

