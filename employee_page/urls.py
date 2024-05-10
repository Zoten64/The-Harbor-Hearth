from . import views
from django.urls import path

urlpatterns = [
    path('', views.EmployeeHome, name='employee_page'),
]