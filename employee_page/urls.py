"""Employee urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_home, name='employee_page'),
    path('orders/', views.employee_orders, name='employee_orders'),
    path('orders/<int:order_number>', views.employee_order_detail,
         name='employee_order_detail'),
    path('orders/<int:order_number>/cancel',
        views.employee_cancel_order_confirm, name='employee_cancel_order'),
    path('orders/<int:order_number>/delete',
        views.employee_delete_order_confirm, name='employee_delete_order'),
    path('contactforms/', views.employee_contact_forms,
         name='employee_contact_forms'),
    path('contactforms/<int:id>', views.employee_contact_forms_detail,
         name='employee_contact_forms_details'),
]
