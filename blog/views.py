import re

from django.http import HttpResponse, request
from django.shortcuts import render, get_object_or_404
from django.views import View
import markdown
# Create your views here.
from markdown.extensions.toc import slugify, TocExtension

from .models import Post,Tag,Category


def index(request):
    post = Post.objects.all()
    tags = Tag.objects.all()
    cates = Category.objects.all()
    return render(request, 'blog/index.html', {'post_list':post,"tags":tags,"cates":cates})


def detail(request, id):
    post = Post.objects.get(id=id)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 记得在顶部引入 TocExtension 和 slugify
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', {'post': post})


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, id):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, id=id)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, id):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, id=id)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})



