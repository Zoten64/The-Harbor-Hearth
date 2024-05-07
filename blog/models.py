from django.db import models

# Create your models here.

class Post(models.Model):
    '''
    Model for news and blog posts
    '''

    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    home_page = models.BooleanField(default=False)