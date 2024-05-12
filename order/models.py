from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DELIVERY_METHOD = (("Eat-in: Counter", "EAT-IN-COUNTER"), 
                   ("Eat-in: Table", "EAT-IN-TABLE"), ("Take-Out", "TAKE-OUT"))

STATE = (("Not Started", "NOT-STARTED"), ("In progress", "IN-PROGRESS"),
         ("Finished", "FINISHED"))

class Order(models.Model):
    '''
    Model for adding orders to the database
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             related_name="order_user", blank=True, null=True)
    order_number = models.AutoField(primary_key=True)
    delivery_method = models.CharField(choices=DELIVERY_METHOD, 
                                       default=0)
    order = models.TextField()
    state = models.CharField(choices=STATE, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order number: {self.order_number}"