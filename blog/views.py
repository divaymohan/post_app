from django.shortcuts import render
posts = [
    {
        'author': 'Divay Mohan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Feb 26 2019'
    },
    {
        'author': 'Diksha Rajput',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'Feb 27 2019'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'from-home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'from-home'
    }
    return render(request, 'blog/about.html', context)
