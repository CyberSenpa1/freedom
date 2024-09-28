from django.shortcuts import render
from news.models import Post

def news(request):
    posts = Post.objects.all()
    return render(request, 'news/posts.html', 
                  {'posts': posts})