"""Database models here"""
import uuid
from django.db import models

# Create your models here.

class Post(models.Model):
    '''
    Model for news and blog posts
    '''

    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    url = models.UUIDField(default=uuid.uuid4, null=True)
    update_date = models.DateTimeField(auto_now=True)
    home_page = models.BooleanField(default=False)

    class Meta:
        """Ordering in the admin panel"""
        ordering = ["-date"]

    def __str__(self):
        """How the instance will be displayed in the admin panel"""
        return f"{self.title} | {self.date}"
