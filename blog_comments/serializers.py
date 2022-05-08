from rest_framework import serializers
from blog_comments.models import Comment

from blog_posts.models import BlogPost
from users.models import CommunityUser


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.first_name + author.last_name')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'comments']


class UserSerializer(serializers.ModelSerializer):
    blogosts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CommunityUser
        fields = ['id', 'username', 'blogposts', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'user', 'blogpost']
