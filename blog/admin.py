from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'abstract', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'created_time', 'modified_time', 'category', 'tags', 'author']


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
