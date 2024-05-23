from django.db import models
from django.contrib.auth.models import User
from contact.models import ContactModel

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    view_orders = models.BooleanField(default=True)
    answer_contact_form = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"
    

class EmployeeContactAnswer(models.Model):
    question = models.ForeignKey(ContactModel, on_delete=models.CASCADE)
    employee_response = models.CharField(max_length=1500)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, 
                             related_name="contact_employee")