from django.shortcuts import render
from order.models import Order
from contact.models import ContactForm

# Create your views here.

def EmployeeHome(request):
    context = {}

    return render(request, 'employee_page/employee_home.html', context)

def EmployeeOrders(request):
    orders = Order.objects.all()
    context = {"orders" : orders}

    return render(request, 'employee_page/employee_orders.html', context)

def EmployeeContactForms(request):
    contact_forms = ContactForm.objects.all()
    context = {"contact_forms" : contact_forms}

    return render(request, 'employee_page/employee_contact_forms.html', context)