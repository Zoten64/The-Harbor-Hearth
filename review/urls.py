from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='review'),
    path('<uuid:url>/', views.ReviewDetail, name='review_detail')
]