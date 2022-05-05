from django.shortcuts import render

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

from rest_framework import generics
from blog_posts.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
