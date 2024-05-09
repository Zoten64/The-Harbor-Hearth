from django.db import models
import uuid

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
        ordering = ["-date"]

    def __str__(self):
        return f"{self.title} | {self.date}"