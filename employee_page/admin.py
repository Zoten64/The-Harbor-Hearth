from django.contrib import admin
from .models import Employee, EmployeeContactAnswer

# Register your models here.

admin.site.register(Employee)
admin.site.register(EmployeeContactAnswer)
