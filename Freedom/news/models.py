from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=300, name='title')
    body = models.TextField()
    slug = models.SlugField(max_length=300, name='slug')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']
        indexes = [
        models.Index(fields=['-publish']),
        ]