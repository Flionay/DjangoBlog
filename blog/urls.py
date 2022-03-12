from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>', views.detail, name="detail"),
    path('categories/<int:id>/', views.category, name='category'),
    path('tag/<int:id>/', views.tag, name='tag'),
]
