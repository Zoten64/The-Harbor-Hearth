from . import views
from django.urls import path

urlpatterns = [
    path('', views.DeleteAccount, name='delete_account'),
    path('confirmation/', views.DeleteAccountConfirm, name='delete_account_confirm'),
    ]