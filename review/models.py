"""Reviews model"""
import uuid
from django.db import models
from django.contrib.auth.models import User

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
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="review_user", blank=True, null=True)
    content = models.TextField(max_length=1000)
    url = models.UUIDField(unique=True, default=uuid.uuid4)
    approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.rating} stars"
