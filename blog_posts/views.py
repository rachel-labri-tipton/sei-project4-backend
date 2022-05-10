from django.shortcuts import render
from backend.permissions import IsStaffWriter
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# Create your views here.

from rest_framework import generics
from blog_posts.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# to creat a blogpos the user must be a staff writer or an admin user
