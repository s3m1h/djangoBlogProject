from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post,Category

# Create your views here.
def detail(request,category_slug, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detail.html',{
        'post':post
    })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'category.html', {
        'category':category
    })
