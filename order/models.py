from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DELIVERY_METHOD = (("COUNTER", "Eat-in: Pick up at counter"), 
                   ("TABLE", "Eat-in: Table delivery"), 
                   ("TAKE-OUT", "Take-Out"))

STATE = (("NOT-STARTED", "Not Started"), ("IN-PROGRESS", "In Progress"),
         ("FINISHED", "finished"), ("CANCELLED", "Cancelled"))

class Order(models.Model):
    '''
    Model for adding orders to the database
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             related_name="order_user", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    order_number = models.AutoField(primary_key=True)
    delivery_method = models.CharField(choices=DELIVERY_METHOD, 
                                       default=0)
    table_number = models.IntegerField(blank=True, null=True)
    order = models.TextField()
    state = models.CharField(choices=STATE, default=0)
    date = models.DateTimeField(auto_now_add=True)
    cancel_reason = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return f"Order number: {self.order_number}"