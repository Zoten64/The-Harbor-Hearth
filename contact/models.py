"""Contact model"""
from django.db import models
from django.contrib.auth.models import User


PREFERRED_CONTACT = (("PHONE", "phone"),("EMAIL", "E-mail"))
# Create your models here.
#Code credit:
# - Email field: https://www.geeksforgeeks.org/emailfield-django-models/

class ContactModel(models.Model):
    '''
    Model for contact forms
    '''
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    preferred_contact = models.CharField(choices=PREFERRED_CONTACT)
    message = models.CharField(max_length=1500)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    answered = models.BooleanField(default=False)
    employee_response = models.CharField(max_length=1500, null=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="contact_employee", null=True)

    def __str__(self):
        return f"{self.name}"
