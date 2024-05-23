from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Order
from .forms import OrderEmail, OrderForm

# Create your views here.
def OrderView(request):

    if request.method == 'POST':
        order_post = OrderForm(request.POST)
        email_post = OrderEmail(request.POST)
        if order_post.is_valid() and email_post.is_valid():
            if request.user.is_authenticated:
                email = request.user.email
                user = request.user
            else:
                email = email_post.cleaned_data['email']
                user = None
            order_info = order_post.cleaned_data['order_info']
            delivery_method = order_post.cleaned_data['delivery_method']
            table_number = order_post.cleaned_data['table_number']

            new_order = Order.objects.create(user=user,
                order=order_info,
                                             email=email, 
                                             delivery_method=delivery_method,
                                             table_number=table_number)
            messages.success(request, 'Order placed!')

    order_form = OrderForm
    email_form = OrderEmail
    context = {
        'email' : email_form,
        'order_form' : order_form
    }

    return render(request, 'order/order.html', context)