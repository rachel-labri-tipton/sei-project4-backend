from django.shortcuts import render
from backend.permissions import IsStaffWriter
from django.shortcuts import render
from rest_framework import filters
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


class BlogPostStaffWriterView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        user = self.request.user
        return BlogPost.objects.filter(author=user)


class BlogPostListDetailfilter(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^categories']

    # features in the filters
    # starts with
    # exact matches
    # full-text-search
    # regex search


# to creat a blogpost the user must be a staff writer or an admin user
