from django.db import models

# Create your models here.
class Order(models.Model):
    '''
    Model for adding orders to the database
    '''
    order_number = models.AutoField(primary_key=True)
    order = models.TextField()
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order number: {self.order_number}"