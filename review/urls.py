"""Review URLS"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewList.as_view(), name='review'),
    path('write/', views.write_review, name='write_review'),
    path('my_review/', views.my_reviews, name='my_review'),
    path('my_review/edit/', views.edit_review, name='edit_review'),
    path('my_review/delete/', views.delete_review_view, name='delete_review'),
    path('<uuid:url>/', views.review_detail, name='review_detail'),
]
