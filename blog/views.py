from django.http import HttpResponse, request
from django.shortcuts import render
from django.views import View
import markdown
# Create your views here.
from .models import Post


def index(request):
    post = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list':post})


def detail(request, id):
    post = Post.objects.get(id=id)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', {'post': post})
