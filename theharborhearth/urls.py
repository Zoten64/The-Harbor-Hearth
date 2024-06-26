"""
URL configuration for theharborhearth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("home.urls"), name="home-urls"),
    path("menu/", include("menu.urls"), name="menu-urls"),
    path("order/", include("order.urls"), name="order-urls"),
    path("reviews/", include("review.urls"), name="review-urls"),
    path("blog/", include("blog.urls"), name="blog-urls"),
    path("contact/", include("contact.urls"), name="contact-urls"),
    path("accounts/", include("allauth.urls"), name="account-urls"),
    path("employee/", include("employee_page.urls"), name="employee-urls"),
    path("delete_account/", include("deleteacc.urls"), name="delete-account-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    
]
