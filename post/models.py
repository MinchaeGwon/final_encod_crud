from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner = models.CharField(max_length=10)
    body = models.TextField()

