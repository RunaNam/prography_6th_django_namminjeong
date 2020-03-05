from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedIdentityField, PrimaryKeyRelatedField, DateTimeField
from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'created_at')


class PostDetailSerializer(serializers.ModelSerializer):
    created_at = DateTimeField(format='%Y-%m-%d %H:%M:%S.%f')

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'created_at', 'user')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title', 'description', 'created_at')


class UserSerializer(serializers.ModelSerializer):
    posts = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
