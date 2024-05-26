"""Menu views"""
from django.shortcuts import render
from .models import Menu

# Create your views here.

def menu_list(request):
    """lists the menu"""
    meals = Menu.objects.filter(category="Meal")
    drinks = Menu.objects.filter(category="Drink")
    desserts = Menu.objects.filter(category="Dessert")
    context = {
        'meals' : meals,
        'drinks' : drinks,
        'desserts' : desserts,
    }
    return render(request, 'menu/menu_list.html', context)
