from django.db import models

# Create your models here.

RATING = ((1, "1 star"), (2, "2 stars"), (3, "3 stars"), 
          (4, "4 stars"), (5, "5 stars"))

class Review(models.Model):
    '''
    Model for reviews
    '''

    rating = models.IntegerField(choices=RATING)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.title} | {self.rating} stars"