"""
Database models
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Topic(models.Model):
    """
    Topics contain posts
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    posts = []

class Post(models.Model):
    """
    Posts can be found under its topic.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    comments = []

class Comment(models.Model):
    """
    Comments are replies to posts
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    body = models.TextField()
