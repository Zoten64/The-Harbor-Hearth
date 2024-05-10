from django.shortcuts import render

# Create your views here.

def EmployeeHome(request):
    context = {}

    return render(request, 'employee_page/employee_home.html', context)