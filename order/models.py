from django.db import models

# Create your models here.

DELIVERY_METHOD = (("Eat-in: Counter", "EAT-IN-COUNTER"), 
                   ("Eat-in: Table", "EAT-IN-TABLE"), ("Take-Out", "TAKE-OUT"))

class Order(models.Model):
    '''
    Model for adding orders to the database
    '''
    order_number = models.AutoField(primary_key=True)
    delivery_method = models.CharField(choices=DELIVERY_METHOD, 
                                       default=0)
    order = models.TextField()
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order number: {self.order_number}"