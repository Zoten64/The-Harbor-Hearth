from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .models import Order
from .forms import OrderEmail, OrderForm

# Create your views here.


def OrderView(request):
    if request.method == 'POST':
        order_post = OrderForm(request.POST)
        email_post = OrderEmail(request.POST)
        if order_post.is_valid() and email_post.is_valid() or \
            order_post.is_valid() and request.user.is_authenticated:
            if request.user.is_authenticated:
                email = request.user.email
                user = request.user
            else:
                email = email_post.cleaned_data['email']
                user = None
            order_info = order_post.cleaned_data['order_info']
            delivery_method = order_post.cleaned_data['delivery_method']
            table_number = order_post.cleaned_data['table_number']

            order = Order.objects.create(user=user,
                                             order=order_info,
                                             email=email,
                                             state= "Not Started",
                                             delivery_method=delivery_method,
                                             table_number=table_number
                                             )
            print(order.state)
            
            msg = "Your order has been placed. \n" \
            f"Order number: {order.order_number} \n" \
            f"Your order: \n {order.order} \n" \
            "Sincerely, the Harbor Hearth team"
            send_mail(
                    "Your order has been placed",
                    msg,
                    None,
                    [email],
                    fail_silently=False,
                )
            messages.success(request, 'Order placed!')
            return redirect(ConfirmOrder)

    table = request.GET.get('table', '')

    try:
        table = int(table)
        order_form = OrderForm(initial={'table_number': table,
                               'delivery_method' : 'TABLE'})
    except:
        order_form = OrderForm
    email_form = OrderEmail
    context = {
        'email': email_form,
        'order_form': order_form
    }

    return render(request, 'order/order.html', context)

def ConfirmOrder(request):
    return render(request, 'order/order_confirm.html')