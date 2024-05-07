from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review

# Create your views here.
class ReviewList(generic.ListView):
    queryset = Review.objects.filter(approved=True)
    template_name = "review/review.html"
    paginate_by = 6