from . import views
from django.urls import path

urlpatterns = [
    path('', views.EmployeeHome, name='employee_page'),
    path('orders/', views.EmployeeOrders, name='employee_orders'),
    path('orders/<int:order_number>', views.EmployeeOrderDetail, name='employee_order_detail'),
    path('contactforms/', views.EmployeeContactForms, name='employee_contact_forms'),
]