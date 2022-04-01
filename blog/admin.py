from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag,PostSummary

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id",'title', 'abstract', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'created_time', 'modified_time', 'category', 'tags', 'author']
    fk_fields = ['category']
    list_per_page = 30
    search_fields=['title']
    list_filter = ['category']


# admin.site.register(Post,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)

admin.site.site_header = 'AngYi博客管理后台'
admin.site.site_title = "AngYi\'s blog"


