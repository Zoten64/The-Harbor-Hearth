from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review

# Create your views here.
def ReviewList(request):

    reviews = Review.objects.filter(approved=True) 
    context = {
        'reviews' : reviews,
    }
    return render(request, 'review/review.html', context)