"""Urls related to the blog app"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog'),
    path('<uuid:url>/', views.blog_detail, name='blog_detail')
]
