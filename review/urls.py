from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='review'),
    path('write/', views.WriteReview, name='write_review'),
    path('my_review/', views.MyReviews, name='my_review'),
    path('my_review/edit/', views.EditReview, name='edit_review'),
    path('my_review/delete/', views.DeleteReview, name='delete_review'),
    path('<uuid:url>/', views.ReviewDetail, name='review_detail'),
]