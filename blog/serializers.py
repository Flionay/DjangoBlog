from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    tags = serializers.CharField(source='tags.name')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Post
        fields = '__all__'

