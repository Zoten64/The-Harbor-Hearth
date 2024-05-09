from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review

# Create your views here.
class ReviewList(generic.ListView):
    queryset = Review.objects.filter(approved=True)
    template_name = "review/review_list.html"
    paginate_by = 6

def ReviewDetail(request, url):
    reviews = Review.objects.filter(approved=True)
    review = get_object_or_404(reviews, url=url)

    context = {
        'review' : review
    }

    return render(request, 'review/review_detail.html', context)