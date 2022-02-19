import uuid
from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(default=str(uuid.uuid4())[:8], editable=False, max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

