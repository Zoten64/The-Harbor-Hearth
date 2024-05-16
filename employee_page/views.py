from django.shortcuts import render, get_object_or_404
from order.models import Order
from contact.models import ContactForm
from django.core.paginator import Paginator

# Create your views here.

def EmployeeHome(request):
    context = {}

    return render(request, 'employee_page/employee_home.html', context)

def EmployeeOrders(request, page=1):
    unfinished_orders = Order.objects.filter(state="Not Started")
    in_progress_orders = Order.objects.filter(state="In progress")
    finished_orders = Order.objects.filter(state="Finished")

    context = {"unfinished_orders" : unfinished_orders,
               "in_progress_orders" : in_progress_orders,
               "finished_orders" : finished_orders}

    return render(request, 'employee_page/employee_orders.html', context)

def EmployeeOrderDetail(request, order_number):
    order = Order.objects.all()
    order = get_object_or_404(order, order_number=order_number)

    context = {
        'order' : order
    }

    return render(request, 'employee_page/employee_order_detail.html', context)

def EmployeeContactForms(request):
    contact_forms = ContactForm.objects.all()
    context = {"contact_forms" : contact_forms}

    return render(request, 'employee_page/employee_contact_forms.html', context)