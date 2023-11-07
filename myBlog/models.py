from django.db import models
from profanity.validators import validate_is_profane
from datetime import datetime , timedelta
from django.utils import timezone

STATUS = (
    (0, 'Draft'),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    body = models.TextField(validators=[validate_is_profane])

    def __str__(self):
        return f"Comment {self.body}"
    
class AddArticle(models.Model):
    title = models.CharField(max_length=300, unique=True, validators=[validate_is_profane])
    new_author = models.CharField(max_length=300, blank=True, validators=[validate_is_profane])
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(validators=[validate_is_profane])

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title 
    
    def old_articles():
        threshold = 30
        threshold_date = timezone.now() - timezone.timedelta(days=threshold)
        AddArticle.objects.filter(created__lt=threshold_date).delete()
