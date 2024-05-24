from django.db import models
from django.contrib.auth.models import User
from contact.models import ContactModel

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
    