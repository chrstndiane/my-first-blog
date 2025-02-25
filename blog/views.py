from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def say_hello(request):
    return HttpResponse('Hello Django')