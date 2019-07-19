from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})

def about_us(request):
    return render(request, 'about_us.html', {})

def single_post(request):
    single_p = Post.objects.filter(id=4)
    return render(request, 'post_page.html', {'single_post':single_p})