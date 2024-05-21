from django.shortcuts import render
from django.views import generic
from .models import Order

# Create your views here.
def Order(request):
    context = {
    }
    return render(request, 'order/order.html', context)