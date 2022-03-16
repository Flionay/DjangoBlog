from django_fakery import factory
from django.contrib.auth.models import User
from blog.models import Post,Category,Tag

factory.m(Post, quantity=40)