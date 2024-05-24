from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views import generic
from .models import Review
from .forms import ReviewForm

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

def WriteReview(request):
    if request.user.is_authenticated:
        user = request.user
        # If the user has already written a review they won't be able to write
        # Another one. However they will be able to edit/delete their review
        # If the review exists the code will run without problems.
        # If the review doesn't exist the code will throw an error
        try:
            review = Review.objects.get(author=user)
            review_exists = True
        except:
            review = ''
            review_exists = False
        
        form = ReviewForm
        context = {
            "review" : review, 
            "review_exists" : review_exists,
            "form" : form 
            }
        return render(request, 'review/write_review.html', context)
    else:
        raise PermissionDenied()

