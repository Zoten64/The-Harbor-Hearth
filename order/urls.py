from . import views
from django.urls import path

urlpatterns = [
    path('', views.OrderView, name='order'),
    path('confirm/', views.ConfirmOrder, name='confirm_order'),
]