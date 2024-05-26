"""Order urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_view, name='order'),
    path('confirm/', views.confirm_order, name='confirm_order'),
]
