from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from order.models import Order
from contact.models import ContactForm
from .forms import Cancel, ChangeStatus
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.


def EmployeeHome(request):
    context = {}

    return render(request, 'employee_page/employee_home.html', context)


def EmployeeOrders(request, page=1):
    unfinished_orders = Order.objects.filter(state="Not Started")
    in_progress_orders = Order.objects.filter(state="In progress")
    finished_orders = Order.objects.filter(state="Finished")

    context = {"unfinished_orders": unfinished_orders,
               "in_progress_orders": in_progress_orders,
               "finished_orders": finished_orders}

    return render(request, 'employee_page/employee_orders.html', context)


def EmployeeOrderDetail(request, order_number):
    order = Order.objects.all()
    order = get_object_or_404(order, order_number=order_number)

    if request.method == 'POST':
        new_status = ChangeStatus(request.POST)
        if new_status.is_valid():
            order.state = request.POST['state']
            order.save()
            messages.success(request, 'Status change successful')

    form = ChangeStatus

    context = {
        'order': order,
        'form' : form
    }

    return render(request, 'employee_page/employee_order_detail.html', context)


def EmployeeContactForms(request):
    contact_forms = ContactForm.objects.all()
    context = {"contact_forms": contact_forms}

    return render(request, 'employee_page/employee_contact_forms.html', context)


def EmployeeCancelOrderConfirm(request, order_number):
    order = Order.objects.all()
    order = get_object_or_404(order, order_number=order_number)

    if request.method == 'POST':
        cancel_reason = Cancel(request.POST)
        if cancel_reason.is_valid():
            order.state = 'cancelled'
            order.cancel_reason = request.POST['cancel_reason']
            order.save()

            message = "Your order was cancelled for the following reason: \n" \
                        f"{order.cancel_reason}"
            send_mail(
                "Your order was cancelled",
                message,
                None,
                [order.email],
                fail_silently=False,
            )
            messages.success(request, 'Cancellation successful')

    form = Cancel

    context = {
        'order': order,
        'form': form
    }
    return render(request, "employee_page/employee_cancel_order.html",
                  context)
