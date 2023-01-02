from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post,Category


# Create your views here.
def home(request):
    post_list = Post.objects.filter(status = Post.ACTIVE)
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)


    return render(request, 'frontpage.html', {
        'posts':posts,
        'categories': Category.objects.all()
    })


def about(request):
    return render(request, 'core/about.html')

