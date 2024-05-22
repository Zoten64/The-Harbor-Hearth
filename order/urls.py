from . import views
from django.urls import path

urlpatterns = [
    path('', views.OrderView, name='order'),
]