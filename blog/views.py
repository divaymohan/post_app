from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'from-home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'from-home'
    }
    return render(request, 'blog/about.html', context)


def login(request):
    context = {
        'title': 'from-register'
    }
    return render(request, 'blog/login.html', context)


def register(request):
    context = {
        'title': 'from-register'
    }
    return render(request, 'blog/register.html', context)
