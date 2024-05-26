"""Menu models"""
from django.db import models

# Create your models here.

MENU_CATEGORY = (("Meal", "MEAL"), ("Drink", "DRINK"), ("Dessert", "DESSERT"))

class Menu(models.Model):
    '''
    Model to add items to the menu
    '''

    category = models.CharField(choices=MENU_CATEGORY, default=0)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    ingridients = models.TextField(blank=True)
    price = models.FloatField(default=0)
    vegan = models.BooleanField(default=False)
    nuts = models.BooleanField(default=False)
    lactose = models.BooleanField(default=False)
    gluten = models.BooleanField(default=False)
    eggs = models.BooleanField(default=False)

    class Meta:
        ordering = ["category"]

    def __str__(self):
        return f"{self.category} | {self.name}"
