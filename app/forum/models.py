from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    comments = []

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    body = models.TextField()
