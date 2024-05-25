from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.views import generic
from django.contrib import messages
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
    # Only logged in users can leave a review
    if request.user.is_authenticated:
        user = request.user
        # If the user has already written a review they won't be able to write
        # Another one. However they will be able to edit/delete their review
        # If there is more than 0 reviews from the logged in user the user will
        # be redirected to the /my_reviews page. Otherwise the code continues
        if Review.objects.filter(author=user).count() > 0:
            return redirect(MyReviews)
        
        if request.method == "POST":
            review_post = ReviewForm(request.POST)
            if review_post.is_valid():
                author = request.user
                rating = review_post.cleaned_data['rating']
                title = review_post.cleaned_data['title']
                content = review_post.cleaned_data['content']
                
                #checks one final time if the user has already submitted a
                #review before creating one to prevent duplicates on reload
                if Review.objects.filter(author=user).count() == 0:
                    Review.objects.create(
                        author=author,
                        rating=rating,
                        title=title,
                        content=content,
                    )
                messages.success(request, 'Your review has been submitted')
                #Redirect after post
                return redirect(MyReviews)

        form = ReviewForm
        context = {
            "form" : form 
            }
        return render(request, 'review/write_review.html', context)
    else:
        #If the user accesses this page without being logged in
        #A 403 error will be raised
        raise PermissionDenied()
    
def MyReviews(request):
    if request.user.is_authenticated:
        user = request.user

        try:
            review = Review.objects.get(author=user)
            review_exists = True
        except:
            review = ''
            review_exists = False
        context = {"review" : review,
                   "review_exists" : review_exists}
        return render(request, 'review/my_review.html', context)
    else:
        #If the user accesses this page without being logged in
        #A 403 error will be raised
        raise PermissionDenied()


