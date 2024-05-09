from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog'),
    path('<uuid:url>/', views.BlogDetail, name='blog_detail')
]