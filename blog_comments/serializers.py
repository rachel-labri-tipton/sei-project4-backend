from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import serializers
from blog_comments.models import Comment

from blog_posts.models import BlogPost
from users.models import CommunityUser


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.first_name + author.last_name')
    comments = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="title")

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'comments']


class UserSerializer(serializers.ModelSerializer):
    blogposts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CommunityUser
        fields = ['id', 'username', 'blogposts', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'user', 'blogpost']

    def destroy(self, request, attrs):
        request = self.context.get("request")
        if request.user != attrs['user']:
            raise serializers.ValidationError({
                "You can only delete comments that you made."
            })
        comment_id = self.kwargs['comment_id']
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return Response(status=204)
