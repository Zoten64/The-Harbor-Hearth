from django.db import models

# Create your models here.

#Code credit:
# - Email field: https://www.geeksforgeeks.org/emailfield-django-models/

class Contact_form(models.Model):
    '''
    Model for contact forms
    '''

    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"