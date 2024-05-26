"""Employee only views"""
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied
from order.models import Order
from contact.models import ContactModel
from .models import Employee
from .forms import Cancel, ChangeStatus, DeleteOrder, ContactResponse


# Create your views here.

def employee_auth(request):
    """
    If true the user is an employee
    Function was made to prevent repitition
    """
    user = request.user
    # If employee object linked to the request user does not exist, raise
    # permission denied. This is to check if the user is an employee
    try:
        employee = Employee.objects.filter(user=user)
    except TypeError as exc:
        raise PermissionDenied() from exc
    if not employee:
        raise PermissionDenied()

    #If everything goes through it will return as true
    return True


def employee_home(request):
    """
    The employee home page
    Displays amount of unfinished orders and unanswered forms
    """
    employee_auth(request)
    #Count the unfinished orders
    unfinished_orders = Order.objects.filter(state="Not Started").count()
    in_progress_orders = Order.objects.filter(state="In Progress").count()
    order_count = unfinished_orders + in_progress_orders
    #count the unanswered forms
    unanswered_contact_forms_count = ContactModel.objects.filter(
        answered=False).count()
    user = request.user
    context = {'user': user,
                'order_count': order_count,
                'contact_count': unanswered_contact_forms_count}
    return render(request, 'employee_page/employee_home.html', context)


def employee_orders(request):
    """Employee only page where they can view orders"""
    employee_auth(request)
    #All the different types of orders are stored in variables
    unfinished_orders = Order.objects.filter(state="Not Started")
    in_progress_orders = Order.objects.filter(state="In Progress")
    finished_orders = Order.objects.filter(state="Finished")
    cancelled_orders = Order.objects.filter(state="Cancelled")

    context = {"unfinished_orders": unfinished_orders,
                "in_progress_orders": in_progress_orders,
                "finished_orders": finished_orders,
                "cancelled_orders": cancelled_orders}

    return render(request, 'employee_page/employee_orders.html', context)


def employee_order_detail(request, order_number):
    """
    Employee only page where they can view order details and change status
    """
    employee_auth(request)
    order = Order.objects.all()
    order = get_object_or_404(order, order_number=order_number)

    if request.method == 'POST':
        #Change order status
        new_status = ChangeStatus(request.POST)
        if new_status.is_valid():
            print("valid")
            order.state = request.POST['state']
            order.save()
            messages.success(request, 'Status change successful')

    form = ChangeStatus

    context = {
        'order': order,
        'form': form,
    }

    return render(request, 'employee_page/employee_order_detail.html',
                    context)


def employee_cancel_order_confirm(request, order_number):
    """Confirmation page for order cancellation"""
    employee_auth(request)
    order = Order.objects.all()
    order = get_object_or_404(order, order_number=order_number)

    if request.method == 'POST':
        #Cancel form has to be valid
        cancel_reason = Cancel(request.POST)
        if cancel_reason.is_valid():
            order.state = 'Cancelled'
            order.cancel_reason = request.POST['cancel_reason']
            order.save()

            #Send email on cancel
            msg = "Your order was cancelled for the following reason:" \
                f"\n{order.cancel_reason}"
            send_mail(
                "Your order was cancelled",
                msg,
                None,
                [order.email],
                fail_silently=False,
            )
            messages.success(request, 'Cancellation successful')

    form = Cancel

    context = {
        'order': order,
        'form': form,
    }
    return render(request, "employee_page/employee_cancel_order.html",
                    context)


def employee_delete_order_confirm(request, order_number):
    """Order deletion confirm page"""
    employee_auth(request)
    order = Order.objects.all()
    order = get_object_or_404(order, order_number=order_number)

    if request.method == 'POST':
        #Deletion form must be valid
        delete = DeleteOrder(request.POST)
        if delete.is_valid():
            order.delete()
            messages.success(request, 'Deletion successful')

    form = DeleteOrder

    context = {
        'order': order,
        'form': form,
    }
    return render(request, "employee_page/employee_delete_order.html",
                    context)


def employee_contact_forms(request):
    """List of all the contact forms"""
    employee_auth(request)
    unanswered_contact_forms = ContactModel.objects.filter(answered=False)
    answered_contact_forms = ContactModel.objects.filter(answered=True)
    context = {"unanswered_contact_forms": unanswered_contact_forms,
                "answered_contact_forms": answered_contact_forms}

    return render(request, 'employee_page/employee_contact_forms.html',
                    context)


def employee_contact_forms_detail(request, id):
    """
    Details page for a specific contact form.
    Employees can answer forms here as well
    """
    employee_auth(request)
    contact_form = ContactModel.objects.all()
    contact_form = get_object_or_404(contact_form, id=id)

    if request.method == 'POST':
        response_data = ContactResponse(request.POST)
        if response_data.is_valid():
            response = response_data.cleaned_data["employee_response"]
            employee = request.user

            #Get all the data from the post and save it
            contact_form.employee_response = response
            contact_form.employee = employee
            contact_form.answered = True
            contact_form.save()

            #Email will be sent upon response
            msg = f"Hello {contact_form.name}! {contact_form.employee} " \
            "has answered your inquiry. \n" \
            f"Your message: \n {contact_form.message} \n" \
            f"Our answer: \n {contact_form.employee_response} \n" \
            "We hope this response was helpful. If you need more " \
            "assistance feel free to reach out again. \n" \
            "Sincerely, the Harbour Hearth Team"

            send_mail(
                "Your inquiry has been answered",
                msg,
                None,
                [contact_form.email],
                fail_silently=False,
            )

            messages.success(request, 'response sent')

    response_form = ContactResponse
    context = {"contact_form" : contact_form,
                "form" : response_form}

    return render(request,
                    'employee_page/employee_contact_forms_detail.html',
                    context)
