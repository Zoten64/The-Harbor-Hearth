from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.

class BlogList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/blog_list.html"
    paginate_by = 6

def BlogDetail(request, url):
    posts = Post.objects.all()
    post = get_object_or_404(posts, url=url)

    context = {
        'post' : post
    }

    return render(request, 'blog/blog_detail.html', context)