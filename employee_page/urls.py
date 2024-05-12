from . import views
from django.urls import path

urlpatterns = [
    path('', views.EmployeeHome, name='employee_page'),
    path('orders/', views.EmployeeOrders, name='employee_orders'),
    path('contactforms/', views.EmployeeContactForms, name='employee_contact_forms'),
]