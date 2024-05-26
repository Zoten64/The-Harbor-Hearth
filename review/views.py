"""Review views"""
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.views import generic
from django.contrib import messages
from .models import Review
from .forms import ReviewForm, DeleteReviewForm

# Create your views here.
class ReviewList(generic.ListView):
    """List all the reviews. Paginate by 6"""
    queryset = Review.objects.filter(approved=True)
    template_name = "review/review_list.html"
    paginate_by = 6



def review_detail(request, url):
    """View a specific view"""
    reviews = Review.objects.filter(approved=True)
    review = get_object_or_404(reviews, url=url)

    context = {
        'review' : review
    }

    return render(request, 'review/review_detail.html', context)

def write_review(request):
    """
    User can write a review if they're authenticated and
    have not already done so
    """
    # Only logged in users can leave a review
    if request.user.is_authenticated:
        user = request.user
        # If the user has already written a review they won't be able to write
        # Another one. However they will be able to edit/delete their review
        # If there is more than 0 reviews from the logged in user the user will
        # be redirected to the /my_reviews page. Otherwise the code continues
        if Review.objects.filter(author=user).count() > 0:
            return redirect(my_reviews)

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
                return redirect(my_reviews)

        form = ReviewForm
        context = {
            "form" : form 
            }
        return render(request, 'review/write_review.html', context)
    #If the user accesses this page without being logged in
    #A 403 error will be raised
    raise PermissionDenied()

def my_reviews(request):
    """
    User can view their own review if logged in
    """
    if request.user.is_authenticated:
        user = request.user
        #if the review doesn't exist it will raise an exeption
        try:
            review = Review.objects.get(author=user)
            review_exists = True
        except ObjectDoesNotExist:
            review = ''
            review_exists = False
        context = {"review" : review,
                   "review_exists" : review_exists}
        return render(request, 'review/my_review.html', context)
    #If the user accesses this page without being logged in
    #A 403 error will be raised
    raise PermissionDenied()

def edit_review(request):
    """
    User can edit their review if they're authenticated and have
    Written a review
    """
    if request.user.is_authenticated:
        user = request.user
        #Check if the review exists. Exception = it does not exist
        try:
            review = Review.objects.get(author=user)
        except ObjectDoesNotExist:
            return redirect(my_reviews)

        if request.method == "POST":
            review_form = ReviewForm(instance=review, data=request.POST)
            if review_form.is_valid():
                review_form.save()
                messages.success(request, 'Your review has been edited')
                #Redirect after post
                return redirect(my_reviews)
        else:
            review_form = ReviewForm(instance=review)
        context = {
            "form" : review_form 
            }
        return render(request, 'review/edit_review.html', context)

    #If the user accesses this page without being logged in
    #A 403 error will be raised
    raise PermissionDenied()

def delete_review_view(request):
    """If the user is logged in their can delete their own review"""
    if request.user.is_authenticated:
        user = request.user
        #Check if review exists. Exception means it doesn't exist
        try:
            review = Review.objects.get(author=user)
        except ObjectDoesNotExist:
            return redirect(my_reviews)

        if request.method == "POST":
            delete_review = DeleteReviewForm(request.POST)
            if delete_review.is_valid():
                review.delete()
                messages.success(request, 'Deletion successful')

        form = DeleteReviewForm
        context = {"form" : form}
        return render(request, 'review/delete_review.html', context)

    #If the user accesses this page without being logged in
    #A 403 error will be raised
    raise PermissionDenied()
