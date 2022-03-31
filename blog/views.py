import json
import re

from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import HttpResponse, request
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import serializers
import markdown
# Create your views here.
# from django.core import serializers
from markdown.extensions.toc import slugify, TocExtension

from .models import Post, Tag, Category


def index(request):
    post = Post.objects.all()
    tags = Tag.objects.all()
    cates = Category.objects.all()

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(list(post), 8)

    # 取出当前需要展示的页码, 默认为1
    page_num = request.GET.get('page', default='1')
    # 根据页码从分页器中取出对应页的数据
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger as e:
        # 不是整数返回第一页数据
        posts = paginator.page('1')
        page_num = 1
    except EmptyPage as e:
        # 当参数页码大于或小于页码范围时,会触发该异常
        print('EmptyPage:{}'.format(e))
        if int(page_num) > paginator.num_pages:
            # 大于 获取最后一页数据返回
            posts = paginator.page(paginator.num_pages)
        else:
            # 小于 获取第一页
            posts = paginator.page(1)

    # 这部分是为了再有大量数据时，仍然保证所显示的页码数量不超过10，
    page_num = int(page_num)
    if page_num < 6:
        if paginator.num_pages <= 10:
            dis_range = range(1, paginator.num_pages + 1)
        else:
            dis_range = range(1, 11)
    elif (page_num >= 6) and (page_num <= paginator.num_pages - 5):
        dis_range = range(page_num - 5, page_num + 5)
    else:
        dis_range = range(paginator.num_pages - 9, paginator.num_pages + 1)

    # data = {'page': page, 'paginator': paginator, 'dis_range ': dis_range}
    # return data
    print(dis_range)
    return render(request, 'blog/index.html', {'post_list': posts,
                                               'dis_range': dis_range,
                                               "tags": tags,
                                               "cates": cates,
                                               'count': paginator.count})


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


def archive(request):
    post_list = Post.objects.all().order_by('-created_time')

    month_count = Post.objects.annotate(month=TruncMonth('created_time')).values('month').annotate(
        c=Count('id'))
    # print(list(month_count)[0]['month'])
    year_list = list(month_count)
    year_list.sort(key=lambda x: x['month'], reverse=True)
    # print(year_list[1]['month'].month)
    year_month = [(item['month'].year, item['month'].month, item['c']) for item in year_list]
    return render(request, 'blog/archive.html', context={'year_month': year_month})

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

# 测试ajax
# 根据年月获取文章

class PostSerializer(serializers.ModelSerializer):
    tag_name = serializers.CharField(source='tags.name')
    cate_name = serializers.CharField(source='category.name')

    class Meta:
        model = Post
        fields = '__all__'


def getpost_yearmonth(request):
    month = int(request.GET.get('month'))
    year = int(request.GET.get('year'))

    post = Post.objects.get_queryset().filter(
        created_time__year=year,
        created_time__month=month)
    posts = PostSerializer(instance=post,many=True)
    # print(posts.data)
    return response_success(message='后台响应成功', data_list=posts.data)



def response_success(message, data=None, data_list=[]):
    return HttpResponse(json.dumps({
        'code': 200,  # code由前后端配合指定
        'message': message,  # 提示信息
        'data': data,  # 返回单个对象
        'dataList': data_list  # 返回对象数组
    }), 'application/json')


# 后端统计图表的接口

def posts_of_days(request):
    # Post.objects.all().annotate('created_time')
    post_day_num = Post.objects.extra(select={'day': 'date( created_time )'}).values('day').annotate(available=Count('created_time'))
    data = serializers.serialize("json", post_day_num)
    return json.dumps(data)

