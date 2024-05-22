from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .models import Order
from .forms import OrderEmail, OrderForm

# Create your views here.
def OrderView(request):

    if request.user.is_authenticated:
        status = 'logged in'
        # if the user is logged in the email field will be automatically filled
        # out in the post
        email_form = ''
    else:
        # if the user is not logged in they'll have to enter their email
        email_form = OrderEmail

    order_form = OrderForm
    context = {
        'email' : email_form,
        'order_form' : order_form
    }

    return render(request, 'order/order.html', context)