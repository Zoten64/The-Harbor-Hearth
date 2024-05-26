"""blog views"""
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.


class BlogList(generic.ListView):
    """Lists all the blog posts as previews"""
    queryset = Post.objects.all()
    template_name = "blog/blog_list.html"
    paginate_by = 6


def blog_detail(request, url):
    """Lists a specific blog post in detail"""
    posts = Post.objects.all()
    post = get_object_or_404(posts, url=url)

    context = {
        'post' : post
    }

    return render(request, 'blog/blog_detail.html', context)
