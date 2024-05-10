from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    view_orders = models.BooleanField(default=True)
    answer_contact_form = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"