from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Post,Category

# Create your views here.
def detail(request,category_slug, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detail.html',{
        'post':post
    })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    post_list = category.posts.filter(status = Post.ACTIVE)

    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)



    return render(request, 'category.html', {
        'category':category,
        'posts':posts
    })
def search(request):
    query = request.GET.get("query", "")
    posts = Post.objects.filter(Q(status = Post.ACTIVE) & Q(title__icontains=query) | Q(text__icontains=query))
    if is not posts:
        return render(request, 'search.html',{
            'posts':posts,
            'query':query
        })