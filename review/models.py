from django.db import models
import uuid

# Create your models here.

RATING = ((1, "1 star"), (2, "2 stars"), (3, "3 stars"), 
          (4, "4 stars"), (5, "5 stars"))

class Review(models.Model):
    '''
    Model for reviews
    Featured reviews will appear on the home page
    Reviews needs to be approved in order to prevent troll reviews or reviews
    containing inappropriate material
    '''

    rating = models.IntegerField(choices=RATING)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    url = models.UUIDField(unique=True, default=uuid.uuid4, null=True)
    approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.rating} stars"