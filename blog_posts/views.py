from django.shortcuts import render
from backend.permissions import IsStaffWriter
from django.shortcuts import render, HttpResponse
from rest_framework import filters
from rest_framework import serializers, response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from blog_posts.models import BlogPost
from .serializers import BlogPostSerializer
from blog_posts import serializers


class BlogPostListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def destroy(self, request):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            if request.user.is_staff_writer == False:
                raise serializers.ValidationError(
                    {"message": "Only Staff Writers can post or update an article."}
                )
        print("request", request.user.username)
        blogpost = self.get_object()
        self.perform_destroy(blogpost)
        return Response(status=status.HTTP_204_NO_CONTENT)


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
