from . import views
from django.urls import path

urlpatterns = [
    path('', views.Menu.as_view(), name='menu'),
]