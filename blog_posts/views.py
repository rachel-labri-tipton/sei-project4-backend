from django.shortcuts import render

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from rest_framework import generics
from blog_posts.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
