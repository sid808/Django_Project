from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Siddharth',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 23, 2021'
    },
    {
        'author': 'Aadarsh',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 24, 2021'
    }
] 
# Create your views here.

def Home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def About(request):
    return render(request, 'blog/about.html', {'title': 'About'})

