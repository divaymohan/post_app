from django.shortcuts import render
from .models import Post


posts = [
    {
        'author': 'Divay Mohan',
        'title': 'Worker 1',
        'content': 'Worker Specification',
        'date_posted': 'March 4 2019'
    },
    {
        'author': 'Aashish Dahiya',
        'title': 'Worker 2',
        'content': 'Worker Specification',
        'date_posted': 'March 4 2019'
    }
]


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
