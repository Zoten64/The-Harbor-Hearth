from . import views
from django.urls import path

urlpatterns = [
    path('', views.Order.as_view(), name='order'),
]