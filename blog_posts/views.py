from django.shortcuts import render
from backend.permissions import IsStaffWriter
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# Create your views here.

from rest_framework import generics
from blog_posts.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetailView(generics.GenericAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# to creat a blogpos the user must be a staff writer or an admin user


class BlogPostCreateView(generics.CreateAPIView):
    permission_classes = [IsStaffWriter | IsAdminUser]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
