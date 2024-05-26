"""Employee model"""
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    """Allows the admin to mark some users as employees"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
