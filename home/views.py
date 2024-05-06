from django.shortcuts import render
from django.views import generic
from menu.models import Menu
from review.models import Review

# Create your views here.
# Credit to loading multiple models:
# https://forum.djangoproject.com/t/how-do-i-load-multiple-models-items-into-a-single-view/919
def Index(request):
    meals = Menu.objects.filter(category="Meal")
    drinks = Menu.objects.filter(category="Drink")
    desserts = Menu.objects.filter(category="Dessert")
    reviews = Review.objects.filter(featured=True)
    context = {
        'meals' : meals,
        'drinks' : drinks,
        'desserts' : desserts,
        'reviews' : reviews
    }
    return render(request, 'home/index.html', context)
