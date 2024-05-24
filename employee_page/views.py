from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from order.models import Order
from .models import Employee
from contact.models import ContactModel
from .forms import Cancel, ChangeStatus, DeleteOrder
from django.contrib import messages
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied


# Create your views here.

def EmployeeAuth(request):
    user = request.user
    try:
        employee = Employee.objects.filter(user=user)
    except:
        raise PermissionDenied()
    if not employee:
        raise PermissionDenied()
    else:
        return True


def EmployeeHome(request):
    if EmployeeAuth(request):
        unfinished_orders = Order.objects.filter(state="Not Started").count()
        in_progress_orders = Order.objects.filter(state="In progress").count()
        order_count = unfinished_orders + in_progress_orders
        unanswered_contact_forms_count = ContactModel.objects.filter(
            answered=False).count()
        user = request.user
        context = {'user': user,
                   'order_count': order_count,
                   'contact_count' : unanswered_contact_forms_count}
        return render(request, 'employee_page/employee_home.html', context)


def EmployeeOrders(request):
    if EmployeeAuth(request):
        unfinished_orders = Order.objects.filter(state="NOT-STARTED")
        in_progress_orders = Order.objects.filter(state="IN-PROGRESS")
        finished_orders = Order.objects.filter(state="FINISHED")
        cancelled_orders = Order.objects.filter(state="CANCELLED")

        context = {"unfinished_orders": unfinished_orders,
                   "in_progress_orders": in_progress_orders,
                   "finished_orders": finished_orders,
                   "cancelled_orders": cancelled_orders}

        return render(request, 'employee_page/employee_orders.html', context)


def EmployeeOrderDetail(request, order_number):
    if EmployeeAuth(request):
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
            'form': form,
        }

        return render(request, 'employee_page/employee_order_detail.html',
                      context)


def EmployeeCancelOrderConfirm(request, order_number):
    if EmployeeAuth(request):
        order = Order.objects.all()
        order = get_object_or_404(order, order_number=order_number)

        if request.method == 'POST':
            cancel_reason = Cancel(request.POST)
            if cancel_reason.is_valid():
                order.state = 'CANCELLED'
                order.cancel_reason = request.POST['cancel_reason']
                order.save()

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


def EmployeeDeleteOrderConfirm(request, order_number):
    if EmployeeAuth(request):
        order = Order.objects.all()
        order = get_object_or_404(order, order_number=order_number)

        if request.method == 'POST':
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


def EmployeeContactForms(request):
    if EmployeeAuth(request):
        unanswered_contact_forms = ContactModel.objects.filter(answered=False)
        answered_contact_forms = ContactModel.objects.filter(answered=True)
        context = {"unanswered_contact_forms": unanswered_contact_forms,
                   "answered_contact_forms": answered_contact_forms}

        return render(request, 'employee_page/employee_contact_forms.html',
                      context)
